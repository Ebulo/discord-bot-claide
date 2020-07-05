from googlesearch import search
from newspaper import Article
import requests


def search_data(query):
    results = []
    c = 0

    for i in search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0):
        results.append(i)
        c += 1
        if c == 10:
            break

    return results


def search_data_test(query):
    links = []
    c = 0

    results = []

    for i in search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0):
        links.append(i)
        c += 1
        if c == 4:
            break
    
    for link in links:
        article = Article(link)
        article.download()
        article.parse()
        data = article.text
        results.append({'title':data[:40] + "..", 'desc': data.replace("\n", " ").replace("  ", " ").replace("   ", " ").replace("    ", " ")[:500] + "....", 'url': link})

    return results


# def getNews(topic):
#     api_key = "96a24fcb4d304307938060377016e9fc"

#     url = f"http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"
#     req = requests.get(url)
#     json_format = req.json()['articles']

#     news = []
#     a = 0
#     for i in json_format:
#         if a == 4:
#             break
#         news.append([i['title'] + " | Link: " + str(i['url']) + " | Image: " + str(i['urlToImage'])])
#         a = a + 1
#     return news


def getNews():
    api_key = "96a24fcb4d304307938060377016e9fc"

    url = f"http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"
    req = requests.get(url)
    json_format = req.json()['articles']

    news = []

    a = 0
    for i in json_format:
        if a == 4:
            break
        news.append({'title': str(i['title']), 'url': str(i['url']), 'image': str(i['urlToImage']), 'desc': str(i['description'])})
        a = a + 1
    return news
