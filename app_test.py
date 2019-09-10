from flask import Flask, render_template, request
import tenorApi
import json

app = Flask(__name__)
#Help from Kevin
@app.route('/', methods=['GET', 'POST'])
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    #reference used https://realpython.com/api-integration-in-python/
    if request.method == 'POST':
        query = request.form.get('Gif')
        return tenorApi.findFunc(query)

    #TODO: Make 'params' dict with query term and API key
    #Referece to https://tenor.com/gifapi/documentation#quickstart-search

    # TODO: Make an API call to Tenor using the 'requests' library

    # TODO: Get the first 10 results from the search results

    # TODO: Render the 'index.html' template, passing the gifs as a named parameter
    #named_Parameter = []

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
