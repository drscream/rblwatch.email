from flask import Flask
from flask import render_template
from flask import request
from werkzeug.contrib.fixers import ProxyFix
from rblwatch.rblwatch import RBLSearch
from IPy import IP

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def show_result():
	try:
		ip       = IP(request.form['ip'])
		searcher = RBLSearch(ip)
		return render_template('result.html', results=searcher.listed)
	except ValueError:
		return render_template('index.html', error="IP Address format was invalid")


@app.route('/contact/')
def show_contact():
	return render_template('contact.html')

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
	app.run()
