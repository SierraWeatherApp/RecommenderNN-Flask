from flask import Flask, render_template, request
import numpy as np
import trainedModels

app = Flask(__name__)


@app.route('/ping')
def hello_world():
    return 'pong', 200


@app.route('/rec')
def test():
    params = request.args.getlist('inputs', type=float) #Import params
    params = np.array(params).reshape(1, -1)     #Reshape data to fit model
    response = trainedModels.getRecommended(params)
    #if len(params) != 11:
    #    return "Not 11 args", 400

    return response, 200


if __name__ == '__main__':
    app.run()
