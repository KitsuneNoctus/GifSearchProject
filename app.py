from flask import Flask, render_template, request
#import tenorApi
import requests
import json


app = Flask(__name__)
#Help from Kevin
@app.route('/', methods=['GET', 'POST'])
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    #reference used https://realpython.com/api-integration-in-python/
    query = request.form.get('Gif')
    # if request.method == 'POST':
    #     query = request.form.get('Gif')
    #     top_10gifs = tenorApi.findFunc(query)
    #     results = top_10gifs['results']

    apiKey = "O2KCLOOCB0K2"
    limit = 10
        #Referece to https://tenor.com/gifapi/documentation#quickstart-search

        # params = {
        # "query": query,
        # "apiKey": apiKey
        # }
    gif_request = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (query, apiKey, limit))
    if gif_request.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(gif_request.content)
        #Got help from a fellow student Ben for this part
        results = top_10gifs['results']
        #return top_10gifs
    else:
        top_10gifs = None
    # #Referece to https://tenor.com/gifapi/documentation#quickstart-search


    # TODO: Make 'params' dict with query term and API key
    #Referece to https://tenor.com/gifapi/documentation#quickstart-search



    # # TODO: Make an API call to Tenor using the 'requests' library
    #
    # # TODO: Get the first 10 results from the search results
    #
    # # TODO: Render the 'index.html' template, passing the gifs as a named parameter

    return render_template("index.html", gifs=results)

if __name__ == '__main__':
    app.run(debug=True)
