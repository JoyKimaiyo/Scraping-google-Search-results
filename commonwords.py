import requests
from bs4 import BeautifulSoup
import gspread
from google.oauth2.service_account import Credentials
import time
from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

def google_search(query, num_pages=2):
    search_results = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    for page in range(num_pages):
        start = page * 10
        url = f"https://www.google.com/search?q={query}&start={start}"
        print(f"Fetching page {page + 1} results...")
        
        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            
            for g in soup.find_all('div', class_='g'):
                title = g.find('h3')
                if title and title.text:
                    title_text = title.text
                    link_tag = g.find('a', href=True)
                    if link_tag:
                        link = link_tag['href']
                        search_results.append((title_text, link))
            time.sleep(2)  # Add delay to prevent rate limiting
        except Exception as e:
            print(f"Error fetching page {page + 1}: {e}")
    
    return search_results

def extract_keywords(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]
    word_counts = Counter(filtered_words)
    common_words = word_counts.most_common(10)  # Top 10 common words
    return common_words

def fetch_page_content(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching page content from {url}: {e}")
        return ""

def main():
    # Define the scopes
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

    # Authenticate using the service account with specified scopes
    credentials = Credentials.from_service_account_file('creds.json', scopes=SCOPES)
    gc = gspread.authorize(credentials)

    # Open the Google Sheet by name
    sh = gc.open('spread scraper').sheet1

    # Scrape Google search results for "artificial intelligence" from 2 pages
    query = "artificial intelligence"
    results = google_search(query, num_pages=2)

    if not results:
        print("No results found.")
        return

    # Prepare data to update the sheet
    data = [["Title", "Link", "Keywords"]]  # Header row

    for title, link in results:
        page_content = fetch_page_content(link)
        keywords = extract_keywords(page_content)
        keywords_str = ', '.join([word for word, count in keywords])
        data.append([title, link, keywords_str])
    
    # Clear the sheet before updating
    sh.clear()

    # Update the sheet with new data
    sh.update('A1', data)

    print("Google Sheet updated successfully.")

if __name__ == "__main__":
    main()
