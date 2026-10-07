"""Open a GitHub issue with the checker's report."""
import os
import sys

import requests

report_file = sys.argv[1] if len(sys.argv) > 1 else "report.txt"
report = open(report_file).read()
repo = os.environ["GITHUB_REPOSITORY"]      # "owner/repo"
token = os.environ["GITHUB_TOKEN"]

resp = requests.post(
    f"https://api.github.com/repos/{repo}/issues",
    headers={
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    },
    json={
        "title": "IP plan check failed",
        "body": "The address plan check found problems:\n\n" + report,
    },
)
resp.raise_for_status()
print("Opened issue", resp.json()["html_url"])
