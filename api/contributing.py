import base64

import requests


def get_contributing(owner, repo, token):
    contributing_url = f"https://api.github.com/repos/{owner}/{repo}/contents/CONTRIBUTING.md"
    headers = {'Authorization': f'token {token}'}
    contributing_response = requests.get(contributing_url, headers=headers)
    if contributing_response.status_code == 200:
        return base64.b64decode(contributing_response.json()["content"]).decode("utf-8")
    contributing_url = f"https://api.github.com/repos/{owner}/{repo}/contents/contributing.md"
    contributing_response = requests.get(contributing_url, headers=headers)
    if contributing_response.status_code == 200:
        return base64.b64decode(contributing_response.json()["content"]).decode("utf-8")
    print(f"Failed to retrieve contributing. Status code: {contributing_response.status_code}")
    return None
