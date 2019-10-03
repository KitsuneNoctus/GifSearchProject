import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask, render_template, request
#import tenorApi
import requests
import json
TENOR_API_KEY = os.getenv("TENOR_API_KEY")

app = Flask(__name__)
@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    #reference used https://realpython.com/api-integration-in-python/

    results = top_ten()
    gif_urls = results['results']
    return render_template("index.html", gifs=gif_urls)
    #     top_10gifs = tenorApi.findFunc(query)
    #     results = top_10gifs['results']
        #Referece to https://tenor.com/gifapi/documentation#quickstart-search

        # params = {
        # "query": query,
        # "apiKey": apiKey
        # }
#Help from Kevin / My own work.
#This goes to another page that displays results
@app.route('/results', methods=['POST'])
def results():
    """result."""
    # TODO: Extract query term from url
    #reference used https://realpython.com/api-integration-in-python/
    query = request.form.get('Gif')
    results = findFunc(query)
    gif_urls = results['results']
    return render_template("results.html", gifs=gif_urls)



    #Referece to https://tenor.com/gifapi/documentation#quickstart-search

    # # TODO: Make an API call to Tenor using the 'requests' library
    #
    # # TODO: Get the first 10 results from the search results
    #
    # # TODO: Render the 'index.html' template, passing the gifs as a named parameter


#Again from / using tenor website code examples
def top_ten():
    apiKey = TENOR_API_KEY
    limit = 10
    top_requests = requests.get("https://api.tenor.com/v1/trending?key=%s&limit=%s" % (apiKey, limit))
    if top_requests.status_code == 200:
        trending_gifs = json.loads(top_requests.content)
    else:
        trending_gifs = None

    return trending_gifs

def findFunc(search_term):
    apiKey = TENOR_API_KEY
    limit = 10
    gif_request = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apiKey, limit))
    if gif_request.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(gif_request.content)
        #Got help from a fellow student Ben for this part
        #results = top_10gifs['results']

        #return top_10gifs
    else:
        top_10gifs = None

    return top_10gifs


if __name__ == '__main__':
    app.run(debug=True)
