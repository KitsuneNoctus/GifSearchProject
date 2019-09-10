from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    #reference used https://realpython.com/api-integration-in-python/
    query = request.args.get('Gif')
    # TODO: Make 'params' dict with query term and API key
    apiKey = 	O2KCLOOCB0K2
    limit = 10
    #TEST search
    search_term = "Smiling"
    #Referece to https://tenor.com/gifapi/documentation#quickstart-search
    params = {"":""}
    gif_request = requests.get("https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (search_term, apiKey, limit))
    if gif_request.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_10gifs = json.loads(gif_request.content)
        print top_10gifs
    else:
        top_10gifs = None
    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    named_Parameter = []

    return render_template("index.html",top_10gifs)

if __name__ == '__main__':
    app.run(debug=True)
