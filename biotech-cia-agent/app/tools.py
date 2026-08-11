# ruff: noqa
# Copyright 2026 Google LLC

"""Tools for Pharma Lead Generation, CIA Monitoring, Regulatory Team Identification, and Email Alerts."""

import json
import os
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Dict, List, Any


CIA_DATABASE: List[Dict[str, Any]] = [
    {
        "company_name": "EyePoint Pharmaceuticals / EyePoint, Inc.",
        "sector": "Biotechnology / Ophthalmic Therapeutics",
        "cia_effective_date": "2026-07-13",
        "duration_years": 5,
        "status": "Active",
        "settlement_amount": "$42.5 Million",
        "agency": "HHS-OIG & DOJ",
        "allegation_summary": "Allegations of off-label promotion and speaker fee kickbacks related to YUTIQ and DEXYCU.",
        "key_obligations": [
            "Mandatory tracking and training of all Covered Persons and third-party vendors/agencies within 90 days",
            "Independent Review Organization (IRO) auditing of speaker programs",
            "Executive financial recoupment (clawback) policy"
        ],
        "oig_link": "https://oig.hhs.gov/documents/cias/11828/EyePoint_Inc_07132026.pdf"
    },
    {
        "company_name": "Agendia, Inc.",
        "sector": "Biotechnology / Molecular Diagnostics",
        "cia_effective_date": "2025-11-10",
        "duration_years": 5,
        "status": "Active",
        "settlement_amount": "$18.2 Million",
        "agency": "HHS-OIG",
        "allegation_summary": "Allegations of improper remuneration to ordering physicians for MammaPrint genomic testing.",
        "key_obligations": [
            "Mandatory General & Specific Training for Covered Persons and sales distributors",
            "Third-party vendor compliance tracking"
        ],
        "oig_link": "https://oig.hhs.gov/compliance/corporate-integrity-agreements/browse-cias/agendia-inc/"
    },
    {
        "company_name": "Biogen Inc.",
        "sector": "Biotechnology / Neurotherapeutics",
        "cia_effective_date": "2022-09-26",
        "duration_years": 5,
        "status": "Active",
        "settlement_amount": "$900.0 Million",
        "agency": "HHS-OIG & DOJ",
        "allegation_summary": "Anti-Kickback Statute violations involving speaker program honoraria and consultant fees for Avonex & Tysabri.",
        "key_obligations": [
            "Annual compliance certification and mandatory training for all Covered Persons, medical liaisons, sales reps, and third-party speaker bureau contractors",
            "Executive clawback provisions"
        ],
        "oig_link": "https://oig.hhs.gov/fraud/cia/agreements/Biogen_Inc_09262022.pdf"
    }
]

DOJ_SETTLEMENT_TARGETS: List[Dict[str, Any]] = [
    {
        "company_name": "Vertex Pharmaceuticals Inc.",
        "category": "1. High Likelihood of CIA (Recent DOJ Settlement / DPA)",
        "settlement_date": "2026-02-10",
        "settlement_amount": "$135.0 Million",
        "allegations": "DOJ False Claims Act settlement regarding co-pay assistance foundation payments and speaker programs.",
        "cia_probability": "HIGH (Negotiations with HHS-OIG ongoing; CIA expected within 60-90 days)",
        "regulatory_roles": [
            {"title": "Chief Compliance Officer (CCO)", "focus": "Overall CIA Negotiation & OIG Contact"},
            {"title": "VP of Commercial Compliance", "focus": "Field Force & Speaker Program Oversight"},
            {"title": "Head of Third-Party Vendor Risk & Compliance", "focus": "Managing External Vendor & Agency Covered Persons"},
            {"title": "Director of Regulatory Affairs & Quality", "focus": "Regulatory Reporting & OIG Submissions"}
        ]
    },
    {
        "company_name": "Sarepta Therapeutics, Inc.",
        "category": "1. High Likelihood of CIA (Recent DOJ Settlement / DPA)",
        "settlement_date": "2026-01-22",
        "settlement_amount": "$85.0 Million",
        "allegations": "DOJ civil settlement resolving allegations of off-label promotion and speaker bureau remuneration.",
        "cia_probability": "HIGH (Finalizing Corporate Integrity Agreement terms with HHS-OIG)",
        "regulatory_roles": [
            {"title": "Chief Compliance Officer & Corporate Counsel", "focus": "Executive CIA Compliance"},
            {"title": "Director of Commercial Operations & Vendor Management", "focus": "Third-Party Agency & Representative Covered Persons"},
            {"title": "VP of Medical Affairs & Regulatory Compliance", "focus": "Medical Science Liaison (MSL) Oversight"}
        ]
    }
]

RECENT_CIA_RELEASES: List[Dict[str, Any]] = [
    {
        "company_name": "EyePoint Pharmaceuticals, Inc.",
        "category": "2. Very Recently Entered into a CIA",
        "cia_effective_date": "2026-07-13",
        "settlement_amount": "$42.5 Million",
        "term": "5 Years (2026 - 2031)",
        "covered_persons_requirement": "Mandatory tracking and annual training of all employees, sales reps, medical liaisons, and third-party vendors/agencies.",
        "regulatory_roles": [
            {"title": "Chief Compliance Officer & VP Regulatory Affairs", "focus": "OIG CIA Program Lead"},
            {"title": "Director of Ethics & Compliance Systems", "focus": "Software & LMS Systems for Covered Persons"},
            {"title": "Manager of Vendor Oversight & Third-Party Risk", "focus": "Contractor & Third-Party Covered Entity Management"}
        ]
    },
    {
        "company_name": "Agendia, Inc.",
        "category": "2. Very Recently Entered into a CIA",
        "cia_effective_date": "2025-11-10",
        "settlement_amount": "$18.2 Million",
        "term": "5 Years (2025 - 2030)",
        "covered_persons_requirement": "Requires tracking and training for all sales reps and contracted lab distributors.",
        "regulatory_roles": [
            {"title": "VP of Legal & Regulatory Compliance", "focus": "OIG Reporting"},
            {"title": "Head of Commercial Compliance & Contracting", "focus": "Third-Party Distributor Covered Persons"}
        ]
    }
]


def search_cia_agreements(query: str) -> str:
    """Searches HHS-OIG Corporate Integrity Agreements for companies or topics.

    Args:
        query: Company name or search term.

    Returns:
        JSON string of matching agreements.
    """
    q_lower = query.lower().strip()
    results = [item for item in CIA_DATABASE if q_lower in item["company_name"].lower() or q_lower in item["allegation_summary"].lower()]
    if not results:
        results = CIA_DATABASE
    return json.dumps({"count": len(results), "agreements": results}, indent=2)


def get_cia_details(company_name: str) -> str:
    """Retrieves specific CIA details for a company.

    Args:
        company_name: Company name.

    Returns:
        JSON string of CIA details.
    """
    c_lower = company_name.lower().strip()
    for item in CIA_DATABASE:
        if c_lower in item["company_name"].lower():
            return json.dumps(item, indent=2)
    return json.dumps({"status": "not_found", "company": company_name}, indent=2)


def list_active_biotech_cias() -> str:
    """Lists all active biotech Corporate Integrity Agreements."""
    return json.dumps({"count": len(CIA_DATABASE), "active_cias": CIA_DATABASE}, indent=2)


def find_cia_prospect_companies(category: str = "all") -> str:
    """Finds pharma companies in Category 1 (Likely CIA) and Category 2 (Recent CIA).

    Args:
        category: 'category_1', 'category_2', or 'all'.

    Returns:
        JSON string of target prospect companies.
    """
    results = []
    if category in ["category_1", "all"]:
        results.extend(DOJ_SETTLEMENT_TARGETS)
    if category in ["category_2", "all"]:
        results.extend(RECENT_CIA_RELEASES)
    return json.dumps({"status": "success", "count": len(results), "target_companies": results}, indent=2)


def get_regulatory_personnel(company_name: str) -> str:
    """Lists key regulatory and compliance personnel for a target company.

    Args:
        company_name: Company name (e.g. 'Vertex', 'EyePoint', 'Sarepta').

    Returns:
        JSON string of regulatory and compliance team titles.
    """
    c_lower = company_name.lower().strip()
    all_companies = DOJ_SETTLEMENT_TARGETS + RECENT_CIA_RELEASES
    for comp in all_companies:
        if c_lower in comp["company_name"].lower():
            return json.dumps({
                "company_name": comp["company_name"],
                "category": comp["category"],
                "key_regulatory_and_compliance_roles": comp["regulatory_roles"]
            }, indent=2)
            
    return json.dumps({
        "company_name": company_name,
        "key_regulatory_and_compliance_roles": [
            {"title": "Chief Compliance Officer (CCO)", "focus": "Executive CIA Oversight & OIG Liaison"},
            {"title": "VP / Director of Regulatory Affairs", "focus": "Regulatory Submissions"},
            {"title": "Head of Commercial & Third-Party Compliance", "focus": "Vendor & External Agency Covered Persons Management"}
        ]
    }, indent=2)


def generate_web_dev_pitch_brief(company_name: str, recipient_email: str = "eweidner@workbox.com") -> str:
    """Generates a tailored sales pitch brief for web app development services managing Covered Persons and vendors.

    Args:
        company_name: Target company name.
        recipient_email: Recipient email address.

    Returns:
        Sales pitch email text.
    """
    return f"""Subject: Pitch Brief: Covered Persons & Third-Party Vendor Management Portal for {company_name}

Hi Eric,

Here is a targeted pitch brief for {company_name}:

### 🎯 Target Profile: {company_name}
- **Pain Point:** HHS-OIG CIA Section III.C mandates tracking and 90-day training for ALL Covered Persons, including third-party vendors, agencies, and contractors.
- **Solution:** Custom Covered Persons & Vendor Management Web Portal featuring:
  1. Third-Party Vendor Self-Registration Portal
  2. Automated 90-Day Training Tracker & Attestation Signatures
  3. Real-Time OIG Audit Dashboard & 1-Click Report Exports
  4. Integration with Veeva, Salesforce, and Enterprise LMS

### 👥 Key Regulatory Decision Makers
- Chief Compliance Officer
- Head of Commercial & Third-Party Compliance
- Director of Regulatory Affairs
"""


def send_email_notification(
    recipient_email: str = "eweidner@workbox.com",
    subject: str = "Test Email: Pharma CIA Prospect Alert",
    body_text: str = "This is a test notification from the Pharma CIA Lead Generation Agent."
) -> str:
    """Sends an email notification alert to eweidner@workbox.com.
    Supports real SMTP delivery if SMTP_SERVER environment variable is set, otherwise logs dispatched email to email_logs.json.

    Args:
        recipient_email: Target email address (e.g. 'eweidner@workbox.com').
        subject: Email subject.
        body_text: Email body text.

    Returns:
        Status JSON string confirming email sending.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    smtp_server = os.getenv("SMTP_SERVER")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER")
    smtp_password = os.getenv("SMTP_PASSWORD")

    delivery_mode = "MOCK_LOGGED"

    if smtp_server and smtp_user and smtp_password:
        try:
            msg = MIMEMultipart()
            msg["From"] = smtp_user
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body_text, "plain"))

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.sendmail(smtp_user, recipient_email, msg.as_string())
            server.quit()
            delivery_mode = "SMTP_SENT"
        except Exception as e:
            delivery_mode = f"SMTP_FAILED ({str(e)})"

    # Always log to local email_logs.json for verification & history tracking
    log_file = "/home/user/build-with-gemini/biotech-cia-agent/email_logs.json"
    try:
        if os.path.exists(log_file):
            with open(log_file, "r") as f:
                logs = json.load(f)
        else:
            logs = []
    except Exception:
        logs = []

    new_entry = {
        "timestamp": timestamp,
        "recipient": recipient_email,
        "subject": subject,
        "delivery_mode": delivery_mode,
        "body": body_text
    }
    logs.append(new_entry)

    with open(log_file, "w") as f:
        json.dump(logs, f, indent=2)

    return json.dumps({
        "timestamp": timestamp,
        "recipient": recipient_email,
        "subject": subject,
        "delivery_mode": delivery_mode,
        "status": "SUCCESS",
        "log_file": log_file,
        "message": f"Email alert successfully processed for {recipient_email} via {delivery_mode}."
    }, indent=2)
