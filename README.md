The library we're going to be using is called g-spread, so let's jump straight in. Now, the first thing we need to do is configure our Google account.

Log into your Google account and navigate to console.developers.google.com.


Click on "Create New Project". You'll be presented with a screen where you can name your project. Let's call this one "g-spread-scraper". Click "Create" to save the project.


Once the project is created, we need to enable two APIs on our project before we can proceed. Navigate to the "APIs & Services" > "Library" section.

Search for "Google Drive API" and select it. Choose your project and click "Enable". Repeat the same process for the "Google Sheets API".

Next, navigate to "APIs & Services" > "Credentials" section.

Click on "Create Credentials" and select "Service Account".

Give the service account a name, such as "g-spread-scraper", and click "Create". Click "Continue" and then "Done".

Once the service account is created, click on the pencil icon to edit it. 

Go to "Add Key" and select "Create New Key". Choose JSON as the format and click "Create". This will download a JSON file containing your credentials.
Put this JSON file in the same folder as your script. You can rename it if you want; for example, "creds.json".


Open the JSON file. You'll find a "client_email" inside. Copy this email address.
Now, go to Google Sheets and create a new sheet. Give it a name, such as "Spread Scraper", and save it.
Click on "Share", add the service account email address you copied earlier, uncheck "Notify people", and then click "Share".
That's all the steps needed to configure your Google Sheets account. Now you're ready to use the g-spread library!


https://github.com/JoyKimaiyo/Scraping-google-Search-results/assets/106971527/c90fe714-79eb-4fa1-b8f1-955bf60ba6d2


