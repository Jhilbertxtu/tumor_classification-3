from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash
from metamind.api import set_api_key

set_api_key("k3U0ZYw5U7BiQWnXYCAJGzKHmSk42VSNUoVebKxPC9jlchnXzk")

app =Flask('tumor_classification')

@app.route('/')
def show_entries():
    return render_template('index.html')






if __name__ == '__main__':
	app.run()
