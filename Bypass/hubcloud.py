import requests
API="https://pbx1botapi.vercel.app/api/hubcloud?url="
def match(url): return "hubcloud" in url
def bypass(url): return requests.get(API+url,timeout=20).text
