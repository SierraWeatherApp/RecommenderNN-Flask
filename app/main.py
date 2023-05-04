from flask import Flask, request
import numpy as np
import trainedModels

app = Flask(__name__)


@app.route('/ping')
def hello_world():
    return 'pong', 200


@app.route('/rec')
def request_rec():
    params = request.args.getlist('inputs', type=float)
    params = np.array(params).reshape(1, -1)
    response = trainedModels.getRecommended(params)

    return response, 200


if __name__ == '__main__':
    app.run()
