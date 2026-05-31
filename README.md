# PostgreSQL Conditional Error Blind SQL Injection Exploitation Tool (PoC)

This repository contains a specialized Proof of Concept (PoC) automation script designed to extract data via **Conditional Error-Based Blind SQL Injection**. The tool is specifically engineered to solve web application security challenges on the PortSwigger Web Security Academy platform targeting PostgreSQL databases.

---

## 🔬 Vulnerability Analysis & Technical Mechanics

When an application isolates database errors from front-end feedback but behaves differently depending on runtime unhandled exceptions, it becomes vulnerable to Conditional Error extraction. This script automates that precise validation cycle:

1. **Conditional Error Injection**: The script injects a conditional query into the `TrackingId` cookie wrapper.
2. **Boolean-to-Error Evaluation**: 
   - The query evaluates whether the specific character at the given password substring index matches the guess.
   - If the condition is **true**, the query triggers a severe database runtime exception (or severe backend malfunction), causing the web application to fail and respond with an **HTTP 500 Internal Server Error**.
   - If the condition is **false**, the query runs safely, and the server returns a standard HTTP 200 OK.
3. **Status Code Triage**: Instead of monitoring response latency, the script performs a zero-wait evaluation of `response.status_code == 500`. If triggered, the character is instantly verified.
4. **Brute-Force Automation**: Systematically loops through a pre-defined alphanumeric spectrum (`a-z`, `0-9`) up to a string capacity boundary of 20 characters.

---

## 📋 Requirements & Installation

This automated scanner relies on basic Python 3 functionalities and requires the standard `requests` module for HTTP session generation.

1. Clone or download this repository into your dedicated local folder:
```bash
git clone https://github.com
cd Conditional-Error-SQLi-Bruteforcer
```

2. Setup the required Python dependencies:
```bash
pip install requests
```

---

## 🚀 Configuration & Deployment

> ⚠️ **IMPORTANT LAB NOTICE**: PortSwigger Web Security Academy lab target instances run on unique ephemeral subdomains. You **must** manually check and update the environment endpoint before executing the payload cycle.

1. Edit the script file and place your active target URL inside the global `url` string variable:
```python
url = "https://<YOUR-ACTIVE-LAB-ID>.web-security-academy.net/"
```

2. Fire up your terminal and run the python automated exploit:
```bash
python errorblindbruteforcer.py
```

### Telemetry Logs:
The program will display a clean, index-by-index trace showing every confirmed character string segment and a live composition tracker of the administrator's password structure until finalization.

---

## ⚖️ Legal & Educational Disclaimer

**IMPORTANT NOTICE:** This utility is engineered exclusively for educational cybersecurity research, academic capture-the-flag (CTF) environments, and authorized security posture auditing. 

Executing targeted brute-force automation tools against live corporate production environments or unauthorized external hosts without explicit written confirmation from the infrastructure owner is illegal and strictly actionable. The author is not responsible for any operational impact or misuse of this technical layout.
