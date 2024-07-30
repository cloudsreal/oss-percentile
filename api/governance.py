import base64

import requests


def get_governance(owner, repo, token):
    governance_url = f"https://api.github.com/repos/{owner}/{repo}/contents/GOVERNANCE.md"
    headers = {'Authorization': f'token {token}'}
    governance_response = requests.get(governance_url, headers=headers)
    if governance_response.status_code == 200:
        return base64.b64decode(governance_response.json()["content"]).decode("utf-8")
    governance_url = f"https://api.github.com/repos/{owner}/{repo}/contents/governance.md"
    headers = {'Authorization': f'token {token}'}
    governance_response = requests.get(governance_url, headers=headers)
    if governance_response.status_code == 200:
        return base64.b64decode(governance_response.json()["content"]).decode("utf-8")
    print(f"Failed to retrieve governance. Status code: {governance_response.status_code}")
    return None
