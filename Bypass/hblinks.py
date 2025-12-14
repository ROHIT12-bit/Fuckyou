import requests
API="https://pbx1botsapi2.vercel.app/api/hblinks?url="
def match(url): return "hblinks" in url
def bypass(url): return requests.get(API+url,timeout=20).text
