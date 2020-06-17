from googlesearch import search

def search_data(query):
    results = []
    c = 0

    for i in search(query, tld='com', lang='en', num=10, start=0, stop=None, pause=2.0):
        results.append(i)
        c += 1
        if c == 10:
            break
    
    return results
