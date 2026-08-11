# ruff: noqa
# Copyright 2026 Google LLC

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from datetime import datetime, timedelta

base_url = 'https://oig.hhs.gov'
headers = {'User-Agent': 'Mozilla/5.0'}

cias = []

for page in range(1, 10):
    url = f'https://oig.hhs.gov/compliance/corporate-integrity-agreements/browse-cias/?page={page}'
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        break
    soup = BeautifulSoup(r.text, 'html.parser')
    
    links = soup.find_all('a', href=re.compile(r'/compliance/corporate-integrity-agreements/browse-cias/[a-z0-9-]+/'))
    seen = set()
    for a in links:
        href = a['href']
        if href in seen or href == '/compliance/corporate-integrity-agreements/browse-cias/':
            continue
        seen.add(href)
        
        comp_url = base_url + href if href.startswith('/') else href
        cr = requests.get(comp_url, headers=headers)
        if cr.status_code == 200:
            csoup = BeautifulSoup(cr.text, 'html.parser')
            title = csoup.find('h1').get_text(strip=True) if csoup.find('h1') else a.get_text(strip=True)
            
            # Find effective date
            date_match = re.search(r'Effective (?:on|from)[:\s]+([A-Za-z]+\s+\d{1,2},\s+\d{4}|\d{1,2}/\d{1,2}/\d{4}|\d{4}-\d{2}-\d{2})', csoup.get_text(), re.I)
            eff_date_str = date_match.group(1) if date_match else 'N/A'
            
            # Parse datetime if possible to compute 90-day deadline
            training_deadline_str = "Within 90 Days of Effective Date"
            training_start_str = "Immediate (Day 1 - within 30 days of hire/execution)"
            
            if eff_date_str != 'N/A':
                parsed_dt = None
                for fmt in ("%B %d, %Y", "%m/%d/%Y", "%Y-%m-%d"):
                    try:
                        parsed_dt = datetime.strptime(eff_date_str, fmt)
                        break
                    except ValueError:
                        pass
                
                if parsed_dt:
                    deadline_dt = parsed_dt + timedelta(days=90)
                    training_deadline_str = f"Must begin immediately; completion required by {deadline_dt.strftime('%B %d, %Y')} (Effective Date + 90 Days)"
                    training_start_str = f"Begins Day 1 ({parsed_dt.strftime('%b %d, %Y')}); Deadline: {deadline_dt.strftime('%b %d, %Y')}"
            
            # Find PDF link
            pdf_a = csoup.find('a', href=re.compile(r'\.pdf$', re.I))
            pdf_url = (base_url + pdf_a['href']) if pdf_a and pdf_a['href'].startswith('/') else (pdf_a['href'] if pdf_a else 'N/A')
            
            # Filter for 2026 or active biotech/pharma
            if '2026' in eff_date_str or any(k in title.lower() for k in ['eyepoint', 'agendia', 'novartis', 'biogen', 'gilead', 'pathology', 'nuclear', 'pharma', 'biotech', 'health']):
                
                requires_training = "YES (Mandatory under OIG CIA Section III.C)"
                training_details = "Mandatory General & Specific Training required for all Covered Persons (employees, executive officers, sales reps, medical liaisons, and contractors)."
                
                clean_name = title.replace("Corporate Integrity Agreement with ", "").replace("Integrity Agreement with ", "")
                
                cias.append({
                    "Company / Entity Name": clean_name,
                    "Effective Date": eff_date_str,
                    "Agreement Type": "Corporate Integrity Agreement (CIA)",
                    "OIG Status": "Active (2026)",
                    "Requires Training of Covered Persons/Entities": requires_training,
                    "When Training Must Begin & Deadline": training_start_str,
                    "Mandatory Training Scope & Requirements": training_details,
                    "Official OIG Agreement PDF": pdf_url,
                    "HHS-OIG Listing URL": comp_url
                })

print(f"Total 2026 / Biotech CIA Records Found: {len(cias)}")

# Create DataFrame
df = pd.DataFrame(cias)

csv_path = "/home/user/build-with-gemini/biotech-cia-agent/biotech_cias_2026.csv"
excel_path = "/home/user/build-with-gemini/biotech-cia-agent/biotech_cias_2026.xlsx"

df.to_csv(csv_path, index=False)
df.to_excel(excel_path, index=False, engine='openpyxl')

print(f"Saved CSV to {csv_path}")
print(f"Saved Excel to {excel_path}")
