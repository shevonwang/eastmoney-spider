import urllib.request
import re
from newspaper.newspaper import Article

url_list = []
for i in range(15):
    url = "http://forex.eastmoney.com/news/cwhlczx_"+str(i+1)+".html"
    response = urllib.request.urlopen(url)
    contents = response.read().decode("utf-8")
    url_list = url_list+re.findall("<a target=\"_blank\" href=\"http://forex\.eastmoney\.com/a/(.*?)\.html", contents)
    url_list = url_list+re.findall("<a target=\"_blank\" href=\"http://finance\.eastmoney\.com/a/(.*?)\.html", contents)
    url_list = url_list+re.findall("<a target=\"_blank\" href=\"http://global\.eastmoney\.com/a/(.*?)\.html", contents)
    url_list = url_list+re.findall("<a target=\"_blank\" href=\"http://stock\.eastmoney\.com/a/(.*?)\.html", contents)
    print("第"+str(i+1)+"页")
print("总文章数：", len(url_list))

for i in range(len(url_list)):
    detail_url = "https://emwap.eastmoney.com/news/info/detail/"+str(url_list[i])
    article = Article(detail_url, language='zh')
    article.download()
    article.parse()
    print("正在写入第", i + 1, "篇文章，进度为：", (i + 1) / len(url_list) * 100, "%")
    with open("E:\\code\\PycharmProjects\\keywords\\whlc.txt", "a+", encoding='utf-8') as f:
        f.write(article.text)
        f.close()
