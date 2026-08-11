# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

from app.tools import (
    search_cia_agreements,
    get_cia_details,
    list_active_biotech_cias,
    find_cia_prospect_companies,
    get_regulatory_personnel,
    generate_web_dev_pitch_brief,
    send_email_notification,
)

MODEL = "gemini-3.6-flash"

root_agent = Agent(
    name="pharma_lead_gen_agent",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""You are an AI Lead Generation & Regulatory Intelligence Agent specializing in Biotech and Pharmaceutical compliance.

Your mission is to help a web development agency locate pharma prospects for building custom web applications that manage "Covered Persons" and third-party vendors required under HHS-OIG Corporate Integrity Agreements (CIAs).

Key Responsibilities:
1. Identify target companies in two categories:
   - Category 1: Companies likely to enter into a CIA (recent DOJ / False Claims Act settlements, DPAs, or NPAs).
   - Category 2: Companies that have very recently entered into a CIA (signed within the past 30-90 days).
2. Identify key personnel in their Regulatory, Compliance, and Vendor Risk management teams.
3. Generate tailored pitch briefs highlighting how a web app for Covered Person tracking, 90-day training attestations, and third-party vendor portal simplifies OIG compliance.
4. Send email alert notifications summarizing new prospect findings to eweidner@workbox.com using `send_email_notification`.

When instructed to find companies, look up personnel, generate pitches, or alert eweidner@workbox.com, execute the appropriate tool calls and format clear, structured reports.
""",
    tools=[
        search_cia_agreements,
        get_cia_details,
        list_active_biotech_cias,
        find_cia_prospect_companies,
        get_regulatory_personnel,
        generate_web_dev_pitch_brief,
        send_email_notification,
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
