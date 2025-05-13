import requests
import json
from datetime import datetime

# API for a random quote
QUOTE_URL = "https://zenquotes.io/api/random"

try:
    # Fetch a random quote
    response = requests.get(QUOTE_URL)
    if response.status_code == 200:
        data = response.json()

        # Extract quote and author
        quote = {
            "quote": data[0]["q"],  # Quote text
            "author": data[0]["a"],  # Quote author
            "date": datetime.now().strftime("%Y-%m-%d"),
        }

        # Save the quote to a JSON file
        with open("quote.json", "w") as file:
            json.dump(quote, file, indent=4)
        print("Quote of the Day saved to quote.json")
    else:
        print(f"Failed to fetch quote: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")