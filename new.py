import bs4
import urllib.request as req
url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"
})

with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
# print(data)
root = bs4.BeautifulSoup(data, "html.parser")
# print(root.title)
titles = root.find_all("div", class_="title")
# print(titles.a.string)
for title in titles:
    if title.a != None:
        print(title.a.string)
