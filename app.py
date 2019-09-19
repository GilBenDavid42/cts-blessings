from flask import Flask, render_template
from os import listdir
import os


app = Flask(__name__, static_url_path='/static')


@app.template_filter()
def list_directory(dir):
    return listdir(dir)


# Preview page routing
@app.route('/preview/<string:file>')
def preview(file):
    return render_template("preview.html", file=file)


# Default routing
@app.route('/<path>')
def index(path):
    return render_template(path + ".html")


# Run the flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
