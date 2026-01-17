#!/usr/bin/env python3
# ==============================================
# HEXSLAYER • PHONE INTELLIGENCE SUITE (LEGAL)
# ==============================================

import phonenumbers
from phonenumbers import geocoder, carrier, timezone

G="\033[92m"; C="\033[96m"; Y="\033[93m"; P="\033[95m"; N="\033[0m"

def banner():
    print(f"""{P}
========================================================
 HEXSLAYER • PHONE INTELLIGENCE (COURT-SAFE)
========================================================
Phone Info • Approx District • No IP • No AI noise
{N}""")

def menu():
    print(f"""{C}
[1] Phone Number Information
[2] District Estimation (Approx ≤50%)
[0] Exit
{N}""")

def parse_phone(num):
    if not num.startswith("+"):
        num = "+91" + num
    return phonenumbers.parse(num, None), num

def phone_info():
    num = input("Phone number: ").strip()
    p, num = parse_phone(num)

    print(f"\n{G}PHONE INFORMATION{N}")
    print("Number      :", num)
    print("Valid       :", phonenumbers.is_valid_number(p))
    print("Country     :", geocoder.country_name_for_number(p, "en"))
    print("Region hint :", geocoder.description_for_number(p, "en") or "Not inferable")
    print("Carrier     :", carrier.name_for_number(p, "en") or "Unknown")
    print("Timezone(s) :", timezone.time_zones_for_number(p))
    input("\nPress Enter...")

def district_estimation():
    num = input("Phone number: ").strip()
    p, num = parse_phone(num)
    carr = carrier.name_for_number(p, "en") or ""

    weights = {
        "Ernakulam": 18,
        "Kozhikode": 16,
        "Thiruvananthapuram": 15,
        "Thrissur": 13,
        "Malappuram": 12,
        "Others": 26
    }

    if "Idea" in carr:
        weights["Ernakulam"] += 4
        weights["Thrissur"] += 2

    print(f"\n{Y}DISTRICT ESTIMATION (NON-AUTHORITATIVE){N}")
    for d,pct in list(weights.items())[:3]:
        print(f"  {d:18}: {min(pct,50)}%")

    print("""
Confidence : Approximate
Legal note : Estimation only, not factual location
Usage      : Intelligence lead narrowing
""")
    input("Press Enter...")

def main():
    while True:
        banner()
        menu()
        ch = input("Select option: ").strip()
        if ch == "1":
            phone_info()
        elif ch == "2":
            district_estimation()
        elif ch == "0":
            break

if __name__ == "__main__":
    main()
