import os

VERSION = 1
GLOBAL_SPIKE_THRESHOLD = os.getenv("GLOBAL_SPIKE_TRESHOLD", 25)
LOCAL_SPIKE_THRESHOLD = os.getenv("LOCAL_SPIKE_TRESHOLD", 50)
EVENT_LIMIT = os.getenv("EVENT_LIMIT", 100)

rule_names = [
    "Powershell Execution Policy Bypass",
    "Suspicious Powershell Command",
    "Process Stopped by Deletion",
    "SQL Injection 200 Response",
    "Windows Command and Scripting Interpreter",
    "Sc exe Manipulating Windows Services",
    "Detect Regasm Spawning a Process",
    "Attempt To Add Certificate To Untrusted Store",
    "DNS Exfiltration Using Nslookup App",
    "Disable UAC Remote Restriction",
]

environments = ["A", "B", "C", "D", "E", "F", "G", "H"]

customers = ["9249", "1234", "4321", "4322", "5843", "5112", "4432", "9332", "1232"]
