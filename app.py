from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

# Route for main page
@app.route('/<path>')
def index(path):
    return render_template(path + ".html")


# Run the flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
