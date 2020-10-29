from flask import Flask, request, jsonify
from api_response import APIResponse
from shortener import Shortener

app = Flask(__name__)


@app.route ('/shorten_url', methods=['POST'])
def shorten_url():
    data = request.json
    long_url = data["url"]
    shortener = Shortener(long_url)
    short_url = shortener.shorten_url()
    api_response = APIResponse(200, short_url)
    return jsonify(api_response.serialize())


if __name__ == "__main__":
    app.run(debug=True)
