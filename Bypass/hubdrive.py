import requests
API="https://pbx1botapi.vercel.app/api/hubdrive?url="
def match(url): return "hubdrive" in url
def bypass(url): return requests.get(API+url,timeout=20).text
