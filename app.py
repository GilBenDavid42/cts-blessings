from flask import Flask, render_template, request
from os import listdir
import os


app = Flask(__name__, static_url_path='/static')


@app.template_filter()
def list_directory(dir):
    return listdir(dir)


# Preview page gets the custom blessing gift file
@app.route('/preview/<string:file>')
def preview(file):
    return render_template("preview.html", file=file)


# Result page gets the edited file blob id
@app.route('/result', methods=['POST'])
def result():
    print("x")
    print(request.form)
    return render_template("result.html", editedAnimationUrl=request.form["animationUrl"])


# Default routing
@app.route('/<path>')
def index(path):
    return render_template(path + ".html")


# Run the flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
