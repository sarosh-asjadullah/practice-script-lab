"""
Script: failed_login_counter.py
Purpose: Analyzes a list of login events and flags potential brute-force attacks.
"""

# 1. Configuration
attempts = ["fail", "success", "fail", "fail", "success", "fail", "locked"]
total_failed_login = 0
THRESHOLD = 3

# 2. Logic with Enumeration (Tracking the 'line number')
# enumerate() gives us both the index (position) and the value
for index, status in enumerate(attempts):
    if status == "fail":
        total_failed_login += 1
        print(f"Log Entry {index}: Failed attempt recorded.")
    elif status == "locked":
        print(f"Log Entry {index}: ALERT - Account already locked.")

# 3. Final Triage
print("-" * 20)
print(f"Total Failures: {total_failed_login}")

if total_failed_login > THRESHOLD:
    print("RESULT: CRITICAL ALERT - Brute Force Threshold Exceeded!")
else:
    print("RESULT: Normal activity detected.")
