import time
import requests

# URL of your web service
url = "https://pastpaperapi.onrender.com"

# Function to send a GET request to your service
def keep_alive():
    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Failed to ping the service: {e}")