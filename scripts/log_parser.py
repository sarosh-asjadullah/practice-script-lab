"""
Script: log_parser.py
Purpose: Efficiently filters large log files for CRITICAL artifacts without exhausting RAM.
"""

# Define paths
input_file = "audit.log"
output_file = "investigation.txt"

# By nesting the 'with' statements, we read and write at the same time
with open(input_file, "r") as search_file, open(output_file, "w") as report_file:
    
    # This loop 'streams' the file line-by-line (Memory Efficient!)
    for line in search_file:
        if "CRITICAL" in line:
            # We write it immediately to the new file
            report_file.write(line)

print(f"[+] Extraction complete. Results saved to {output_file}")
