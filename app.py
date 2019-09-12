from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static', template_folder='templates')

# Route for main page
@app.route('/')
def index():
    return render_template("index.html")


# Run the flask server
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
