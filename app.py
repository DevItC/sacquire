from sacquire import FBAcquire
from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html', media_preview=None, media_url=None)

@app.route('/api', methods=['POST'])
def api():
    url = request.form['URL']
    fb = FBAcquire()
    fb.URL = url
    return jsonify(fb.data)


if __name__=='__main__':
    app.run(host='0.0.0.0', port=80)
