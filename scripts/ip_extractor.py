

"""
DFIR Tool: IP Pattern Extractor
Description: Scans unstructured data for valid IPv4 addresses using high-fidelity regex.
"""
#Import Regex Module
import re 

# Define paths

input_file = ".\\audit.log"
output_file =".\\ip_found"

#Opens file handle to read file
with open (input_file,"r") as search_file:
    data = search_file.read()
ip_list = re.findall(r"(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)",data)

ip_string = "\n".join(ip_list)

with open(output_file, "w") as report_file:
    report_file.write(ip_string)

print(f"The extracted IP has been written to {output_file}")


