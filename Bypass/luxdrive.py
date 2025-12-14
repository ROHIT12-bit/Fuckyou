import requests
API="https://pbx1botapi.vercel.app/api/luxdrive?url="
def match(url): return "luxdrive" in url
def bypass(url): return requests.get(API+url,timeout=20).text
