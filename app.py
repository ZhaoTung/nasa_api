from flask import Flask, render_template, request
import urllib.request
import json

app = Flask(__name__)

@app.route('/')
def main():
    apodurl = 'https://api.nasa.gov/planetary/apod?'
    key = 'IhPDteqpCVmrbDaRXp5bY820KvCUcxUhmeiRVexV'
    apodurlobj = urllib.request.urlopen(apodurl + 'api_key=' + key)
    apodread = apodurlobj.read()
    dnasa = json.loads(apodread.decode('utf-8'))

    imgUrl = dnasa['url']
    return render_template('home_page.html', imgUrl=imgUrl)

@app.route('/key', methods=['POST'])
def key():
        key = request.form['apikey']
        imgUrl = buildURL(apodurl, key)
        return render_template('home_page.html', imgUrl=imgUrl)


if __name__ == '__main__':
    app.run(debug=True)
