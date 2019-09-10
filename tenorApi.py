import requests
import json

#got code via help from clasmate Kevin, gave help at least
apiKey ="O2KCLOOCB0K2"
limit = 10

def findFunc(search_term):
    #TEST search

    #Referece to https://tenor.com/gifapi/documentation#quickstart-search
    #params = {"":""}
    gif_request = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apiKey, limit))
    if gif_request.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(gif_request.content)
        return top_10gifs
    else:
        top_10gifs = None
