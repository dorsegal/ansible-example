# The package of the files list
import os
import random


# The package of the api server
from flask import Flask
from flask import send_file


app = Flask(__name__)

images_path = '/opt/img-panda/resources/'
images = os.listdir(images_path)


# Service get random image
@app.route('/')
def url_request():
    return send_file(images_path + rnd())


def rnd():
    random_image = random.choice(images)
    return random_image


