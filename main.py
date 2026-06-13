#Creating CSV Files in Python

import csv

with open("vulnerabilities.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Hostname", "CVE", "Severity", "Status"])
    writer.writerow(["Server01", "CVE-2025-59287", "Critical", "Closed"])
    writer.writerow(["Server96", "CVE-2025-21298", "Critical", "Closed"])
    writer.writerow(["Server97", "CVE-2025-21298", "Critical", "Closed"])
    writer.writerow(["Server98", "CVE-2025-21298", "Critical", "Closed"])
    writer.writerow(["Server99", "CVE-2025-21298", "Critical", "Closed"])


#Reading from a CSV File in Python
import csv

def vulnerability_tracker(file_path):
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        headers = next(reader)
        vulns = [row for row in reader]

        print(headers)
        print(vulns)
    
vulnerability_tracker("vulnerabilities.csv")
