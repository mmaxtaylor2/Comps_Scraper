import sys

def accretion_dilution(
    buyer_eps,
    target_eps,
    target_price,
    premium,
    cash_portion,
    stock_portion,
    buyer_share_price,
    buyer_shares_out,
    target_shares_out
):
    # Convert EPS to total earnings
    buyer_earnings = buyer_eps * buyer_shares_out
    target_earnings = target_eps * target_shares_out

    # Purchase price including premium
    offer_price = target_price * (1 + premium)

    # Deal value
    deal_value = offer_price * target_shares_out

    # Stock issuance
    equity_funded = deal_value * stock_portion
    shares_issued = equity_funded / buyer_share_price

    # New share count
    pro_forma_shares = buyer_shares_out + shares_issued

    # Pro forma EPS (correct method)
    pro_forma_eps = (buyer_earnings + target_earnings) / pro_forma_shares

    # Accretion / Dilution
    ad_percent = ((pro_forma_eps - buyer_eps) / buyer_eps) * 100

    return {
        "Offer Price ($/share)": round(offer_price, 2),
        "Deal Value ($B)": round(deal_value / 1e9, 2),
        "Shares Issued (M)": round(shares_issued / 1e6, 2),
        "Pro Forma Shares (B)": round(pro_forma_shares / 1e9, 3),
        "Pro Forma EPS ($)": round(pro_forma_eps, 2),
        "Accretion/Dilution (%)": round(ad_percent, 2)
    }


if __name__ == "__main__":
    print("Running Accretion/Dilution...")

    # Example: Nike acquiring ONON
    results = accretion_dilution(
        buyer_eps = 3.20,
        target_eps = 0.45,
        target_price = 30,
        premium = 0.25,
        cash_portion = 0.60,
        stock_portion = 0.40,
        buyer_share_price = 100,
        buyer_shares_out = 1200e6,   # 1.2B shares
        target_shares_out = 250e6    # 250M shares
    )

    print("\nAccretion/Dilution Model Output\n")
    for k, v in results.items():
        print(f"{k}: {v}")

