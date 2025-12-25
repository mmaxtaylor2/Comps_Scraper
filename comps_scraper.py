#!/opt/anaconda3/bin/python3
import requests
import pandas as pd
from bs4 import BeautifulSoup

import sys
tickers = [t.upper() for t in sys.argv[1:]] if len(sys.argv) > 1 else ["NKE", "LULU", "UAA", "ONON"]


headers = {"User-Agent": "Mozilla/5.0"}

def get_finviz_data(ticker):
    url = f"https://finviz.com/quote.ashx?t={ticker}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"Ticker": ticker, "Error": "Request blocked"}

    soup = BeautifulSoup(response.text, "html.parser")
    table = soup.find("table", class_="snapshot-table2")

    if table is None:
        return {"Ticker": ticker, "Error": "No data"}

    data = {"Ticker": ticker}
    cells = table.find_all("td")

    for i in range(0, len(cells) - 1, 2):
        data[cells[i].text.strip()] = cells[i+1].text.strip()

    return data

def clean_num(x):
    if isinstance(x, str):
        x = x.replace("%", "").replace("B", "e9").replace("M", "e6").replace(",", "")
    try:
        return float(x)
    except:
        return None

if __name__ == "__main__":
    print("Running scraper...")
    df = pd.DataFrame([get_finviz_data(t) for t in tickers])

    # Convert fields to numbers for multiples
    for col in ["Market Cap", "Enterprise Value", "EBITDA", "Sales"]:
        if col in df.columns:
            df[col] = df[col].apply(clean_num)

    # Calculate multiples
    if "Enterprise Value" in df.columns and "EBITDA" in df.columns:
        df["EV/EBITDA"] = df["Enterprise Value"] / df["EBITDA"]

    if "Enterprise Value" in df.columns and "Sales" in df.columns:
        df["EV/Revenue"] = df["Enterprise Value"] / df["Sales"]

    # Clean output
    keep = ["Ticker", "Market Cap", "Enterprise Value", "Sales", "EBITDA", "EV/Revenue", "EV/EBITDA"]
    df = df[[c for c in keep if c in df.columns]]

    print(df)
    df.to_csv("comps_output.csv", index=False)
    print("Saved to comps_output.csv")
