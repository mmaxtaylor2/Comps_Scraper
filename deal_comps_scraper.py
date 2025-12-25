import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

# CLI tickers: python3 deal_comps_scraper.py NKE LULU UAA
tickers = sys.argv[1:] if len(sys.argv) > 1 else ["NKE","LULU","UAA","ONON","DECK","CROX"]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0"
}

# Terms that imply an M&A situation
keywords = ["acquire", "acquisition", "takeover", "merger", "purchase", "buyout", "merge"]

def scan_google_news(ticker):
    url = f"https://news.google.com/rss/search?q={ticker}+acquisition"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"Ticker": ticker, "M&A Flag": "Unavailable", "Headline": "Feed blocked", "Keyword Triggered": "-", "Signal Score": 0}

    soup = BeautifulSoup(response.text, "xml")
    items = soup.find_all("item")

    if not items:
        return {"Ticker": ticker, "M&A Flag": "No", "Headline": "No M&A headlines found", "Keyword Triggered": "-", "Signal Score": 1}

    # Check top 5 headlines
    for item in items[:5]:
        title = item.title.text.lower()
        for word in keywords:
            if word in title:
                return {
                    "Ticker": ticker,
                    "M&A Flag": "Yes",
                    "Headline": item.title.text.strip(),
                    "Keyword Triggered": word,
                    "Signal Score": 3
                }

    return {"Ticker": ticker, "M&A Flag": "No", "Headline": "No M&A signals in recent headlines", "Keyword Triggered": "-", "Signal Score": 1}


if __name__ == "__main__":
    print("Scanning Google News for M&A indicators...\n")
    results = [scan_google_news(t) for t in tickers]
    df = pd.DataFrame(results)
    print(df)
    df.to_csv("deal_comps_raw.csv", index=False)
    print("\nSaved to deal_comps_raw.csv")

