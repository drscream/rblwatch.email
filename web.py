from flask import Flask
from flask import render_template
from flask import request
from rblwatch.rblwatch import RBLSearch

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/', methods=['POST'])
def show_user_profile():
	print(request.form)
	searcher = RBLSearch(request.form['ip'])
	return render_template('result.html', results=searcher.listed)

if __name__ == '__main__':
	app.debug = True
	app.run()
