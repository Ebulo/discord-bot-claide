from googlesearch import search
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


def getNews(topic):
    api_key = "96a24fcb4d304307938060377016e9fc"
    url = f"http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"
    req = requests.get(url)
    json_format = req.json()['articles']

    news_list = []
    c = 1
    for i in json_format:
        article = f"{str(c)} + '. ', {i['title']}, {i['url']}, {i['urlToImage']}"
        news_list.append(article)
        # news_list.append("\n")
        c += 1
        if c == 8:
            break
    return news_list

print(getNews("topic"))