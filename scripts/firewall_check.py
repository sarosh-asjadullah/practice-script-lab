#Enhanced Logic
"""
Script: firewall_check.py
Purpose: Simulates a firewall check by comparing input against a threat intelligence list.
"""
print("\nChecking Ip on FW1")
# 1. Expanded Threat Intel List (Block List)
block_list = ["1.1.1.1", "8.8.4.4", "192.168.5.5", "10.0.0.7", "45.33.22.11"]

# 2. Capture and Sanitize Input
# .strip() removes accidental spaces like " 1.1.1.1 "
ip_address = input("Enter IP Address to check: ").strip()

# 3. Enhanced Logic Flow
if ip_address in block_list:
    print(f"[!] BLOCK: {ip_address} is found in the Threat Intel block list.")
    
elif ip_address.startswith("192.168."):
    print(f"[+] ALLOW: {ip_address} is internal network traffic.")

else:
    print(f"[*] NEUTRAL: {ip_address} is unknown but not blocked. Proceed with caution.")
