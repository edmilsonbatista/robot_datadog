import xml.etree.ElementTree as ET
import json
import time

tree = ET.parse('output.xml')
root = tree.getroot()

results = {
    "timestamp": int(time.time()),
    "passed": 0,
    "failed": 0,
    "tests": []
}

for suite in root.iter('test'):
    name = suite.attrib['name']
    status = suite.find('status').attrib['status']
    results['tests'].append({
        "name": name,
        "status": status
    })
    if status == "PASS":
        results["passed"] += 1
    else:
        results["failed"] += 1

with open("robot-results.json", "w") as f:
    json.dump(results, f)