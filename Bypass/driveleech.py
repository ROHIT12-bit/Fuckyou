import requests
API="https://pbx1botapi.vercel.app/api/driveleech?url="
def match(url): return "driveleech" in url
def bypass(url): return requests.get(API+url,timeout=20).text
