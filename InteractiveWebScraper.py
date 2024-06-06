import requests
from bs4 import BeautifulSoup

def fetch_quotes():
    url = "http://quotes.toscrape.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        
        quote_list = []
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            quote_list.append((text, author))
        
        return quote_list
    else:
        print(f"Failed to retrieve quotes. Status code: {response.status_code}")
        return []

def display_quotes(quotes):
    for i, (text, author) in enumerate(quotes, 1):
        print(f"{i}. {text} - {author}\n")

def main():
    print("Fetching quotes from the web...")
    quotes = fetch_quotes()
    
    if quotes:
        print("\nQuotes:\n")
        display_quotes(quotes)
    else:
        print("No quotes found.")

if __name__ == "__main__":
    main()
