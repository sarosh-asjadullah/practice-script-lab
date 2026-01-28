import re

"""
DFIR Tool: IP Pattern Extractor
Description: Scans unstructured data for valid IPv4 addresses using high-fidelity regex.
"""

import re

input_file = ".\\audit.log"
output_file =".\\ip_found"
with open (input_file,"r") as search_file:
    data = search_file.read()
ip_list = re.findall(r"(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)",data)

ip_string = "\n".join(ip_list)

#print(ip_string) 

with open(output_file, "w") as report_file:
    report_file.write(ip_string)

print(f"The extracted IP has been written to {output_file}")

this is what i have coded
