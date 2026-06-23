# Requires requests; install with: pip install requests

import requests

# Send a GET request to a website
response = requests.get("https://www.google.com")

# Print the HTTP status code
print(f"HTTP Status Code: {response.status_code}")

# Requires colorama; install with: pip install colorama

from colorama import Fore, Style, init

# Initialize Colorama
init()

print(Fore.GREEN + "Hello, this text is green!" + Style.RESET_ALL)