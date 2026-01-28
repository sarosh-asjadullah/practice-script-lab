"""
Script: log_parser.py
Purpose: Efficiently filters large log files for CRITICAL artifacts without exhausting RAM.
"""

with open(".\\audit.log","r") as file:

    file_text = file.read()
#print(file_text)

lines = file_text.split("\n")

critical_lines = []

for i in lines:

    if "CRITICAL" in i:

        critical_lines.append(i)

critcal_text =""

#print(critical_lines)

for i in critical_lines:

    critcal_text = i + "\n" + critcal_text



#print(critcal_text)



with open(".\\investigation.txt","w") as file:

    file.write(critcal_text)
