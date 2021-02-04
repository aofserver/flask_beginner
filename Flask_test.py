'''This Project make by Sarawut nacwijit'''

from flask import Flask, send_file, render_template, request
from flask_cors import CORS
from pathlib import Path


# Create the application instance
app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
app.url_map.strict_slashes = False
cors = CORS(app, resources={r"*": {"origins": "*"}})

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = str(Path(__file__).parent)

# Create a URL route in our application for "/"
@app.route('/')
def hello():
    return "<h1> Hello World. </h1>" ,200

# return Json
@app.route('/test', methods=['GET'])
def test():
    return {"reply":"test"} ,200

# return file in local
@app.route('/getimage', methods=['GET'])
def get_image():
    filename = BASE_DIR + "/templates/test.png"
    return send_file(filename) ,200


@app.route('/gethtml', methods=['GET'])
def get_html():
    filename = "/templates/test.html"
    return send_file("templates/test.html") ,200


@app.route('/API', methods=['GET', 'POST'])
def parse_request():
    header = request.headers
    print(header)
    data = request.json
    print(data)
    return {"test":True} ,200


@app.route('/user/<username>')
def profile(username):
    return "username's {}.".format(username) ,200


if __name__ == '__main__':
    # app.run(port=8000)     #localhost:8000/
    app.run(debug=True)     #localhost:5000/

