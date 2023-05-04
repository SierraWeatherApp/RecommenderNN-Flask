from keras.models import load_model
import numpy as np

head_labels = ['head_beanie', 'head_cap', 'head_empty']
shirt_labels = ['shirt_hoodie', 'shirt_long-sleeve', 'shirt_t-shirt']
jacket_labels = ['jacket_empty', 'jacket_light', 'jacket_winter']
pants_labels = ['pants_pants', 'pants_shorts', 'pants_snow-pants']
shoes_labels = ['shoes_boots', 'shoes_rain-boots', 'shoes_sandals', 'shoes_sneakers']
umbrella_labels = ['umbrella_False', 'umbrella_True']


def getRecommended(params):
    # Load the saved model
    head_model = load_model('trained/head-m.h5')
    shirt_model = load_model('trained/shirt-m.h5')
    jacket_model = load_model('trained/jacket-m.h5')
    pants_model = load_model('trained/pants-m.h5')
    shoes_model = load_model('trained/shoes-m.h5')
    umbrella_model = load_model('trained/umbrella-m.h5')
    # Generate predictions

    raw_head = np.argmax(head_model.predict(params), axis=-1).tolist()
    raw_shirt = np.argmax(shirt_model.predict(params), axis=-1).tolist()
    raw_jacket = np.argmax(jacket_model.predict(params), axis=-1).tolist()
    raw_pants = np.argmax(pants_model.predict(params), axis=-1).tolist()
    raw_shoes = np.argmax(shoes_model.predict(params), axis=-1).tolist()
    raw_umbrella = np.argmax(umbrella_model.predict(params), axis=-1).tolist()

    head_predicted = [head_labels[i] for i in raw_head]
    shirt_predicted = [shirt_labels[i] for i in raw_shirt]
    jacket_predicted = [jacket_labels[i] for i in raw_jacket]
    pants_predicted = [pants_labels[i] for i in raw_pants]
    shoes_predicted = [shoes_labels[i] for i in raw_shoes]
    umbrella_predicted = [umbrella_labels[i] for i in raw_umbrella]

    predictions = head_predicted + shirt_predicted + jacket_predicted + pants_predicted + shoes_predicted + umbrella_predicted
    return predictions

