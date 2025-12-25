import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup

# If no tickers passed, default set
tickers = sys.argv[1:] if len(sys.argv) > 1 else ["NKE", "LULU", "DECK", "CROX", "VFC"]

# Headers to avoid simple blocks
headers = {"User-Agent": "Mozilla/5.0"}

# Keywords that indicate *real* M&A signals
CONFIRM_MA = [
    "acquires", "acquisition of", "merger", "merger agreement",
    "takeover bid", "buyout offer", "acquire", "acquired",
    "strategic alternatives", "exploring sale", "engages bankers",
    "evaluating buyers", "receives offer", "receives bids"
]

# Words to reject (false positives)
REJECT = [
    "stake", "stake increase", "stake purchase", "insider purchase",
    "valuation", "target price", "analyst upgrade", "undervalued",
    "activist stake", "investor stake", "portfolio", "raises position"
]

def check_news(ticker):
    url = f"https://news.google.com/search?q={ticker}+merger+OR+acquisition+OR+buyout"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    raw = soup.get_text(" ", strip=True)

    # Default return if nothing found
    result = {
        "Ticker": ticker,
        "M&A Signal": "No",
        "News Flag": "No",
        "Headline": "No verified M&A activity",
        "Signal Score": 0,
        "Notes": "Clean — no deal language detected"
    }

    # Reject false positives first
    if any(x in raw.lower() for x in REJECT):
        result["Notes"] = "Rejected — non-M&A/irrelevant article"
        return result

    # Check for strong confirmation signals
    for kw in CONFIRM_MA:
        if kw in raw.lower():
            result["M&A Signal"] = "Yes"
            result["News Flag"] = "Yes"
            result["Signal Score"] = 3
            result["Headline"] = f"M&A keyword match: '{kw}'"
            result["Notes"] = "Deal-language detected — review recommended"
            return result

    return result


if __name__ == "__main__":
    print("Running M&A monitoring scan...\n")
    results = [check_news(t) for t in tickers]
    df = pd.DataFrame(results)
    print(df.to_string(index=False))
    df.to_csv("deal_monitor_output.csv", index=False)
    print("\nSaved to deal_monitor_output.csv")

