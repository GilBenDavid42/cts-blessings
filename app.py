from flask import Flask, render_template, request
from os import listdir, remove, mkdir
import uuid
import base64

app = Flask(__name__, static_url_path='/static')


@app.template_filter()
def list_directory(dir):
    return listdir(dir)


# Preview page gets the custom blessing gift file
@app.route('/preview/<string:files_str>')
def preview(files_str):
    return render_template("preview.html", files=files_str.split('|')[:-1])


# Result page gets the edited file blob id
@app.route('/result', methods=['POST'])
def result():
    animations_data = request.form.getlist('animationData')
    files_name = []
    for animation_data in animations_data:
        file_name = animation_data
        file_ext = ""
        if file_name.startswith("data:"):
            file_ext = ".png"
            animation_data = base64.decodestring(animation_data.split(",")[1].encode())
        elif file_name.startswith('blob:'):
            file_ext += ".gif"

        if file_ext:
            file_name = "static/temp-files/" + str(uuid.uuid1()) + file_ext
            with open(file_name, "wb") as file:
                file.write(animation_data)
        files_name.append(file_name)

    return render_template("result.html", editedAnimationUrls=files_name)


# Default routing
@app.route('/<path>')
def index(path):
    return render_template(path + ".html")


# Run the flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
