import requests


def get_comments(owner, repo, token, comments_url):
    headers = {'Authorization': f'token {token}'}
    comments_response = requests.get(comments_url, headers=headers)
    if comments_response.status_code == 200:
        return comments_response.json()
    else:
        print(f"Failed to retrieve comments from {comments_url} . Status code: {comments_response.status_code}")
        return None
