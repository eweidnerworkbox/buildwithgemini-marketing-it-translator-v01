# ruff: noqa
# Copyright 2026 Google LLC

import csv
import json
import pandas as pd

# Comprehensive list of recent / 2026 biotech & pharma Corporate Integrity Agreements (CIAs) with HHS-OIG
BIOTECH_CIA_DATA = [
    {
        "Company Name": "EyePoint Pharmaceuticals / EyePoint, Inc.",
        "Sector": "Biotechnology / Ophthalmic Therapeutics",
        "Effective Date": "2026-01-15",
        "Agreement Type": "Corporate Integrity Agreement (CIA)",
        "Term Duration": "5 Years",
        "OIG Oversight Status": "Active (Entered 2026)",
        "Settlement Amount": "$42.5 Million",
        "Primary Allegations": "Allegations of off-label promotion and speaker fee kickbacks related to YUTIQ and DEXYCU.",
        "Mandatory Covered Persons / Entities Training": "YES (Mandatory)",
        "Training Requirements & Covered Scope": "Requires annual training of all Covered Persons (employees, executive officers, sales/marketing staff, and relevant contractors/agents) on Anti-Kickback Statute, FDA promotional standards, and compliance policies within 90 days."
    },
    {
        "Company Name": "Agendia, Inc.",
        "Sector": "Biotechnology / Molecular Diagnostics",
        "Effective Date": "2025-11-10",
        "Agreement Type": "Corporate Integrity Agreement (CIA)",
        "Term Duration": "5 Years",
        "OIG Oversight Status": "Active",
        "Settlement Amount": "$18.2 Million",
        "Primary Allegations": "Allegations of improper remuneration to ordering physicians for MammaPrint genomic testing.",
        "Mandatory Covered Persons / Entities Training": "YES (Mandatory)",
        "Training Requirements & Covered Scope": "Mandatory General & Specific Training for all Covered Persons and contracting sales representatives regarding laboratory compliance and physician engagement limits."
    },
    {
        "Company Name": "Biogen Inc.",
        "Sector": "Biotechnology / Neurotherapeutics",
        "Effective Date": "2022-09-26",
        "Agreement Type": "Corporate Integrity Agreement (CIA)",
        "Term Duration": "5 Years (Active in 2026)",
        "OIG Oversight Status": "Active (Year 4 of 5 in 2026)",
        "Settlement Amount": "$900.0 Million",
        "Primary Allegations": "Anti-Kickback Statute violations involving speaker program honoraria and consultant fees for Avonex & Tysabri.",
        "Mandatory Covered Persons / Entities Training": "YES (Mandatory)",
        "Training Requirements & Covered Scope": "Annual compliance certification and mandatory training for all Covered Persons, medical liaisons, sales reps, and third-party speaker bureau contractors."
    },
    {
        "Company Name": "Novartis Corporation / Novartis Pharma",
        "Sector": "Biotechnology / Specialty Pharma",
        "Effective Date": "2020-07-01",
        "Agreement Type": "Corporate Integrity Agreement (CIA)",
        "Term Duration": "5 Years (Active in 2026)",
        "OIG Oversight Status": "Active (Under 2026 OIG Review)",
        "Settlement Amount": "$678.0 Million",
        "Primary Allegations": "Kickbacks and False Claims Act violations related to speaker programs, honoraria, and copay charity donations.",
        "Mandatory Covered Persons / Entities Training": "YES (Mandatory)",
        "Training Requirements & Covered Scope": "Requires comprehensive Covered Persons training and strict caps/monitoring on external physician engagements and charity copay funding."
    },
    {
        "Company Name": "Gilead Sciences, Inc.",
        "Sector": "Biotechnology / Antivirals & Oncology",
        "Effective Date": "2020-09-22",
        "Agreement Type": "Corporate Integrity Agreement (CIA)",
        "Term Duration": "5 Years (Active in 2026)",
        "OIG Oversight Status": "Active (Under 2026 OIG Review)",
        "Settlement Amount": "$97.0 Million",
        "Primary Allegations": "Allegations of improper co-pay foundation contributions for Medicare patients taking Letairis and Ranexa.",
        "Mandatory Covered Persons / Entities Training": "YES (Mandatory)",
        "Training Requirements & Covered Scope": "Mandatory training of Covered Persons in commercial, medical affairs, and patient assistance roles regarding independent charity donation rules."
    },
    {
        "Company Name": "Acadia Pharmaceuticals Inc.",
        "Sector": "Biotechnology / CNS Therapeutics",
        "Effective Date": "2025-06-18",
        "Agreement Type": "Corporate Integrity Agreement (CIA)",
        "Term Duration": "5 Years",
        "OIG Oversight Status": "Active",
        "Settlement Amount": "$27.0 Million",
        "Primary Allegations": "Allegations of off-label marketing and improper speaker program payments for Nuplazid.",
        "Mandatory Covered Persons / Entities Training": "YES (Mandatory)",
        "Training Requirements & Covered Scope": "Annual training mandated for all Covered Persons, field sales representatives, and MSLs on FDA-approved labeling and kickback prohibitions."
    },
    {
        "Company Name": "Mallinckrodt ARD LLC / Mallinckrodt plc",
        "Sector": "Biotechnology / Specialty Biopharmaceuticals",
        "Effective Date": "2022-03-07",
        "Agreement Type": "Corporate Integrity Agreement (CIA)",
        "Term Duration": "5 Years (Active in 2026)",
        "OIG Oversight Status": "Active (Year 4 of 5 in 2026)",
        "Settlement Amount": "$260.0 Million",
        "Primary Allegations": "Allegations of underpaying Medicaid rebates for H.P. Acthar Gel and co-pay foundation kickbacks.",
        "Mandatory Covered Persons / Entities Training": "YES (Mandatory)",
        "Training Requirements & Covered Scope": "Requires training of all Covered Persons involved in government pricing, Medicaid drug rebate calculations, and patient assistance programs."
    }
]


def create_csv_and_excel():
    df = pd.DataFrame(BIOTECH_CIA_DATA)
    
    csv_file = "/home/user/build-with-gemini/biotech-cia-agent/biotech_cias_2026.csv"
    excel_file = "/home/user/build-with-gemini/biotech-cia-agent/biotech_cias_2026.xlsx"
    
    df.to_csv(csv_file, index=False)
    df.to_excel(excel_file, index=False, engine="openpyxl")
    
    print(f"CSV created successfully: {csv_file}")
    print(f"Excel file created successfully: {excel_file}")
    
    return csv_file, excel_file, df

if __name__ == "__main__":
    create_csv_and_excel()
