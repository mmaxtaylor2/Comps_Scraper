Comps & M&A Monitoring Toolkit 

A Python-based toolkit for pulling peer valuation multiples, screening for potential M&A activity, and running simplified 
accretion/dilution math for hypothetical transactions. 

Project Overview: 
This project was developed to simulate the type of work performed in equity research, investment banking, and corporate development.
It integrates:
  Comparable valuation scraping (Finviz HTML parsing)
  Headline-based deal signal monitoring via news queries
  Simple accretion/dilution impact and share issuance math 

Repository Structure: 
  Comps_scraper.py: Pulls valuation data
  ma_monitor.py: Scans headlines for deal keywords
  accretion_calc.py: Quick accretion/dilution rough-cut model based on price, deal value, and share issuance
  output/: Stores CSVs generated from each module for tracking and review

Key Findings: 
  Valuation spreads across the peer set can highlight mispriced assets relative to sector averages.
  News flow with acquisition or stake-related language can flag companies entering strategic transition periods. 
  Keywords alone do not confirm transactions; signals require human review and supporting context. 
  Rough-cut accretion results help determine whether implied deal structures would be dilutive based on share issuance. 

Key Takeaways: 
  Comparable analysis is most useful when standardized EV-based metrics are used across the entire peer set. 
  Headline scanning is not definitive, but it is directionally valuable for sourcing potential deal activity. 
  Early-stage accretion/dilution checks help frame feasibility before a full model is justified. 
  Automating repeatable screens saves time versus manual web review, especially for coverage lists of 8-25 tickers.  
