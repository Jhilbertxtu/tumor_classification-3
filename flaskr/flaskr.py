from flask import Flask,request,session,g,redirect,url_for,abort,render_template,flash

app =Flask('tumor_classification')

@app.route('/')
def show_entries():
    return render_template('index.html')

if __name__ == '__main__':
	app.run()
