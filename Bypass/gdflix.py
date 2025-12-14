import requests
API="https://pbx1botapi.vercel.app/api/gdflix?url="
def match(url): return "gdflix" in url
def bypass(url): return requests.get(API+url,timeout=20).text
