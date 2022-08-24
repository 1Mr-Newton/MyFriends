from flask import Flask, render_template, redirect, request, url_for, session


app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
  return render_template('home.html')




@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_foun(e):
  return render_template('500.html', 500)




if __name__ == "__main__":app.run(debug=True)