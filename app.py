import urllib.request
import json
import html

with urllib.request.urlopen('http://stephanus.tlg.uci.edu/Iris/Wotd') as response:
    resp = response.read()

string = resp.decode('utf-8')
data = json.loads(string)
greek_chars = [html.unescape(char) for char in data['word'].split(';')]
data['word'] = ''.join(greek_chars)

print(data)


