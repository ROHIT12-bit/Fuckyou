import requests
API="https://pbx1botapi.vercel.app/api/neo?url="
def match(url): return "neo" in url
def bypass(url): return requests.get(API+url,timeout=20).text
