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


# def getNews(topic):
#     api_key = "96a24fcb4d304307938060377016e9fc"
#     url = f"http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"
#     req = requests.get(url)
#     json_format = req.json()['articles']

#     news_list = []
#     c = 0
#     for i in json_format:
#         if c == 8:
#             return news_list
#             break
#         # article = f"{str(c)}. {i['title']} {i['url']} | {i['urlToImage']}               "
#         article = i['title']
#         news_list.append(article)
#         # news_list.append("\n")
#         c = c + 1
#     return news_list


def getNews(topic):
    api_key = "96a24fcb4d304307938060377016e9fc"

    url = f"http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey={api_key}"
    req = requests.get(url)
    json_format = req.json()['articles']

    news = []
    a = 0
    for i in json_format:
        if a == 4:
            break
        news.append([i['title'] + " | Link: " + str(i['url']) + " | Image: " + str(i['urlToImage'])])
        a = a + 1
    return news
