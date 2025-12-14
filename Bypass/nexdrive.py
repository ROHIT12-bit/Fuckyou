import requests
API="https://pbx1botsapi2.vercel.app/api/nexdrive?url="
def match(url): return "nexdrive" in url
def bypass(url): return requests.get(API+url,timeout=20).text
