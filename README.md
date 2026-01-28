# DFIR Python Automation Lab

This repository contains a series of Python scripts developed to automate common tasks in **Digital Forensics and Incident Response (DFIR)**. The goal of this project is to build a library of tools that assist in artifact triage, log analysis, and evidence processing.

## 🛠 Features & Tools

| Script | Forensic Use Case | Key Python Concepts |
| --- | --- | --- |
| `asset_profile.py` | Generates a snapshot report of a suspect machine’s metadata. | Variables, F-Strings, Booleans |
| `firewall_check.py` | Automatically cross-references IP addresses against threat intel blocklists. | Lists, Input Sanitization, Logic |
| `failed_login_counter.py` | Detects potential Brute Force attacks by analyzing login status lists. | For Loops, Counters, Alerts |
| `log_cleaner.py` | Normalizes messy log data for consistent analysis. | String Methods (`.strip`, `.split`) |
| `log_parser.py` | Carves specific critical artifacts out of raw system logs. | File I/O (Read/Write), Context Managers |
| `ip_extractor.py` | Extracts all IP addresses from unstructured text files or email headers. | Regular Expressions (Regex) |

## 🚀 Getting Started

### Prerequisites

* Python 3.x installed.
* A terminal or IDE (VS Code recommended).

### How to use

1. Clone the repository:
```bash
git clone https://github.com/sarosh-asjadullah/practice-script-lab.git

```


2. Navigate to the script directory:
```bash
cd scripts

```


3. Run a specific tool:
```bash
python3 firewall_check.py

```



## 📈 Learning Objectives

This project was built while following the Google Cybersecurity Professional Certificate curriculum to bridge the gap between basic Python programming and practical security operations. URL for YouTube Video
```bash
https://youtu.be/4pe1fn3Gus0?si=_Ky1ppYuan016mrB

```
* **Automation:** Reducing manual effort in log review.
* **Data Integrity:** Ensuring forensic data is parsed without modification.
* **Scalability:** Handling thousands of entries that would be impossible to review by hand.

---

