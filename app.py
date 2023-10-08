from flask import Flask, request, redirect,render_template
import string
import random

app = Flask(__name__)

# store all the short url by {shorturl:long_url}
url_mappings = {}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        long_url = request.form['long_url']
        short_code = generate_short_code()
        store_mapping(short_code, long_url)
        short_url = request.host_url + short_code
        return f'Short URL: <a href="{short_url}">{short_url}</a>'
    return render_template("index.html")



@app.route('/<short_code>')
def redirect_to_original(short_code):
    long_url = get_original_url(short_code)
    if long_url:
        return redirect(long_url)
    return 'Short URL not found.'

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def store_mapping(short_code, long_url):
    url_mappings[short_code] = long_url

def get_original_url(short_code):
    return url_mappings.get(short_code, None)

if __name__ == '__main__':
    app.run(debug=True)
