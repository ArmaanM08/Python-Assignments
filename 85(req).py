import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Example Usage
url = "https://jsonplaceholder.typicode.com/posts/1"
print(fetch_data(url))