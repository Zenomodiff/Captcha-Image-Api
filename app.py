from math import ceil
from random import randint, choice
from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    return '''
	            <!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
      <h1 class="project-name">Welcome to Captcha Image API 🔑</h1>
      <h2 class="project-tagline">An API returns random Captcha Images</h2
<h2 id="usage">Usage:</h2>
<ul>
<p>The Endpoint Of The API</p>
  <li><code class="language-plaintext highlighter-rouge">/captcha</code> will return Random Captcha Filled Images</li>
</ul>
    </main>
  </body>
</html>

 '''

@app.route('/captcha', methods=['GET'])
def mahadev_pic():
	im_index = randint(0,1000)
	file = f'imgs/image{im_index}.png'
	return send_file(file, mimetype='image/png')

if __name__ == '__main__':
	app.run(threaded=True, port=5000)
