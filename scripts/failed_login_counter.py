attempts = ["fail", "success", "fail", "fail", "success", "fail"]
total_failed_login = 0
for i in attempts:
    if i == "fail":
        total_failed_login = total_failed_login+1
if total_failed_login > 3:
    print("\nALERT: Possible Brute Force.")
# This can be further modified by reading security evtx file and exctracting action and then putting it in attempts and then predicting brute force
