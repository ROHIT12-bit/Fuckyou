import requests
API="https://pbx1botapi.vercel.app/api/hubcdn?url="
def match(url): return "hubcdn" in url
def bypass(url): return requests.get(API+url,timeout=20).text
