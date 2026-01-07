## Comps & M&A Monitoring Toolkit

A Python-based toolkit designed to support comparable company analysis and early-stage M&A screening. The project automates peer valuation collection, monitors news flow for potential deal signals, and performs simplified accretion/dilution checks to assess transaction feasibility before deeper modeling.

## Problem Context

Comparable analysis and M&A monitoring are often performed manually through repeated web searches, spreadsheet updates, and ad hoc news reviews. This project was built to automate the most repeatable components of that workflow, allowing analysts to quickly identify valuation dispersion, flag potential deal activity, and frame preliminary transaction economics before committing to full-scale valuation or merger modeling.

## Project Overview

The toolkit simulates workflows commonly used in:

- Equity research and sector coverage  
- Investment banking and M&A screening  
- Corporate development and strategic finance  

It integrates three core components:

- Automated peer valuation data collection  
- Headline-based monitoring for potential deal signals  
- First-pass accretion/dilution logic for hypothetical transactions  

The output is intended to support **screening and prioritization**, not replace detailed valuation or merger models.

## Core Components

### Comparable Valuation Scraper
- Pulls peer valuation multiples via HTML parsing (Finviz)
- Standardizes metrics across the peer set
- Exports structured CSV outputs for review and tracking

### M&A Signal Monitor
- Scans news headlines for acquisition- and stake-related keywords
- Flags companies entering potential strategic transition periods
- Designed as a directional signal, not a confirmation mechanism

### Accretion / Dilution Calculator
- Performs rough-cut accretion/dilution math
- Incorporates share issuance assumptions and deal value inputs
- Helps frame whether a transaction structure is directionally accretive or dilutive

## Repository Structure

Comps-MA-Monitoring-Toolkit/
├── comps_scraper.py # Pulls peer valuation multiples
├── ma_monitor.py # Scans headlines for deal-related signals
├── accretion_calc.py # First-pass accretion/dilution logic
├── output/ # Generated CSVs for analysis and tracking
└── README.md # Documentation
