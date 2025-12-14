import requests
API="https://pbx1botapi.vercel.app/api/pixelcdn?url="
def match(url): return "pixelcdn" in url
def bypass(url): return requests.get(API+url,timeout=20).text
