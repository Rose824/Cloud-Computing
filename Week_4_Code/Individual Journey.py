# Reference URL:
# https://docs.docker.com/compose/environment-variables/
# https://stackoverflow.com/questions/59177135/how-to-generate-a-url-from-json-object

###in docker file:
# start from base
FROM ubuntu:18.04
LABEL maintainer="Your Name <youremailaddress@provider.com>"
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app
CMD [ "python", "./app.py" ]

#Write Python code to process JSON file data and flush out output to index.html

import os
from flask import Flask, render_template, abort, url_for, json, jsonify
import json
app = Flask(__name__,template_folder='.'
# read file
with open('file.json', 'r') as myfile:
    data = myfile.read()
@app.route("/")
def index():
    return render_template('index.html', title="page", jsonfile=json.dumps(data))
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


#in html file:
<!DOCTYPE html>
<html>
<body>
<h2>JSON Data</h2>
<p id="demo"></p>
<script>
 var jsonfile ={{ jsonfile|tojson }};
 var obj = JSON.parse(jsonfile);;
document.getElementById("demo").innerHTML = obj;
</script>
</body>
</html>