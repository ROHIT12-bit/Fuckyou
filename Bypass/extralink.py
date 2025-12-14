import requests
API="https://pbx1botapi.vercel.app/api/extralink?url="
def match(url): return "extralink" in url
def bypass(url): return requests.get(API+url,timeout=20).text
