import requests

url = 'https://raw.github.com/faafeefoo/testing/master/sample_text'
r = requests.get(url)
# To print contents on-screen
print(r.text)
# To save as a file
with open("sample_output.txt", 'wb') as f:
    f.write(r.content)
