# The package of the files list
import os
from flask import Flask, request

app = Flask(__name__)


# Service get counts
@app.route('/', methods = ['GET', 'POST'])
def handle_req():

    if request.method == 'GET':
        with open("/opt/smart-panda/counts.txt", "r") as f:
            count = f.read()
            return str(count + '\n')

    if request.method == 'POST':
        with open("/opt/smart-panda/counts.txt", "r+") as f:
            count = f.read()
            count = [int(x) for x in count.split()]
            a = count
            count = sum(count)
            count += 1
            count_str = str(count)
            f.seek(0)
            f.truncate()
            f.write(count_str)
        return "Panda Added \n"
