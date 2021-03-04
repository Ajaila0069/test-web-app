from flask import Flask
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
import json
import os
import random

with open("imlinks.json", "r") as f:
    imgs = f.read()

imgdict = json.loads(imgs)

print(type(imgdict))

server = Flask(__name__)
cors = CORS(server, resources={r"/": {"origins" : "*"}})
api = Api(server)

parser = reqparse.RequestParser()
parser.add_argument("character", type=str)

class image(Resource):
    def post(self):
        args = parser.parse_args(strict=True)
        try:
            print(args["character"])
            images = imgdict[args["character"]]
            return {"name" : args["character"], "image" : random.choice(images)}
        except KeyError:
            return {"error" : "invalid character"}

api.add_resource(image, '/', methods=["POST"])

if __name__ == "__main__":
    server.run(debug=True, port=5000)
