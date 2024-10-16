from flask import Flask, render_template, request
import requests

app = Flask(__name__)

NEWS_API_KEY = 'ba858a26a4d9406bbe79bebff7b36e9a'

@app.route('/')
def index():
    query = request.args.get('query', 'empresas')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={NEWS_API_KEY}'
    response = requests.get(url)
    news_data = response.json().get('articles', [])
    return render_template('index.html', news=news_data, query=query)

if __name__ == '__main__':
    app.run(debug=True)