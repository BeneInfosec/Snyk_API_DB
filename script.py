import requests
from bs4 import BeautifulSoup
import json

# Set the search keyword
keyword = input("Enter a keyword to search vulnerabilities: ").strip()

def main():
    page = 0 
    try:
        while true:
            # Set the URL based on the page number
            if page == 0:
                url = f"https://security.snyk.io/vuln?search={keyword}"
            else:
                url = f"https://security.snyk.io/vuln/{page}?search={keyword}"
            
            print(f"Fetching data from: {url}")
            
            # Send the HTTP GET request
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP request errors

            # Parse the HTML to find the <script> tag
            soup = BeautifulSoup(response.text, "html.parser")
            not_found_results = soup.find(string=lambda text: "No results found" in text if text else False)
            
            if not_found_results:
                print("No results found.")
                break

            script_tag = soup.find("script", {"id": "__NUXT_DATA__"})
            if not script_tag:
                print("No more results or an error occurred.")
                break

            # Extract and parse JSON data
            raw_json = script_tag.string
            nuxt_data = json.loads(raw_json)

            # Debugging: Print the structure of nuxt_data
            print(json.dumps(nuxt_data, indent=4))

            page += 1  # Increment page number for the next iteration

    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
    except json.JSONDecodeError as e:
        print("Error parsing JSON:", e)

if __name__ == "__main__":
    main()
