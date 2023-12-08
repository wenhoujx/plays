# this file downloads the audit logs from github
import requests

token = "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"
# Define the GitHub organization or repository
org_name = "claritype"
repo_name = "ct"

# Define the API endpoint for audit logs

api_url = f"https://api.github.com/enterprises/{org_name}/audit-log?per_page=100"

# Make a GET request to fetch audit logs
response = requests.get(api_url, headers={"Authorization": f"Bearer {token}"})

# Check if the request was successful
if response.status_code == 200:
    # Download the audit logs
    print(response)
    print("Audit logs downloaded successfully.")
else:
    print(f"Failed to fetch audit logs. Status code: {response.status_code}")
