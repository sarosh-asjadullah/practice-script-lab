"""
Script: asset_profile.py
Purpose: Creates a standardized forensic profile for a suspect workstation.
"""

# 1. Input Section (Makes the script reusable)
hostname: str = input("Enter Hostname: ")
ip_address: str = input("Enter IP Address: ")
# We convert input to a boolean by checking if it equals 'yes'
status_input = input("Is the host infected? (yes/no): ").lower()
is_infected: bool = status_input == "yes"

# 2. Case Information
case_id: int = 101

# 3. Logic & Output
print("-" * 30) # Visual separator for the report
if is_infected:
    print(f"[ALERT] CASE-ID: {case_id}")
    print(f"Status: CRITICAL - Infection Detected")
    print(f"Device: {hostname} ({ip_address})")
else:
    print(f"[INFO] CASE-ID: {case_id}")
    print(f"Status: CLEAR - No Infection Detected")
    print(f"Device: {hostname} ({ip_address})")
print("-" * 30)
