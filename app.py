from flask import Flask, render_template, request
from os import listdir, remove, mkdir
import uuid
import shutil
import base64
from threading import Thread
from time import sleep

app = Flask(__name__, static_url_path='/static')


@app.template_filter()
def list_directory(dir):
    return listdir(dir)


# Preview page gets the custom blessing gift file
@app.route('/preview/<string:files_str>')
def preview(files_str):
    return render_template("preview.html", files=files_str.split('|')[:-1])


def rm_temp_file(file_name):
    sleep(60 * 10)  # Ten minutes before removing file
    remove("static/custom-blessing-gifts/temp-files/" + file_name)


# Result page gets the edited file blob id
@app.route('/result', methods=['POST'])
def result():
    print(request.form)
    animationData = request.form["animationData"];

    file_name = str(uuid.uuid1())
    if animationData.startswith("data:"):
        file_name += ".png"
        print(animationData)
        animationData = base64.decodestring(animationData.split(",")[1].encode())
    else:
        file_name += ".gif"

    with open("static/temp-files/" + file_name, "wb") as file:
        file.write(animationData)

    rm_temp_file_thread = Thread(target=rm_temp_file, args=(file_name,))
    return render_template("result.html", editedAnimationUrl=file_name)


# Default routing
@app.route('/<path>')
def index(path):
    return render_template(path + ".html")


# Run the flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
