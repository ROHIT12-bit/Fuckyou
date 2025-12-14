import requests
API="https://pbx1botapi.vercel.app/api/extraflix?url="
def match(url): return "extraflix" in url
def bypass(url): return requests.get(API+url,timeout=20).text
