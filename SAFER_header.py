import requests

url = "https://safer.fmcsa.dot.gov/CompanySnapshot.aspx"

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept Encoding': 'gzip, deflate, br',
    'Accept Language': 'en-US,en;q=0.9',
    'Cache Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'https://safer.fmcsa.dot.gov/',
    'Upgrade Insecure Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
print(response.text)
