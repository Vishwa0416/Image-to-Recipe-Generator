from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

model = InceptionV3(weights="imagenet")

def predict_ingredients(img, top_k=5):
    """
    Predict ingredients from an uploaded image.
    :param img: PIL Image
    :param top_k: number of top predictions
    :return: list of ingredient names
    """
    img = img.resize((299, 299))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    decoded = decode_predictions(preds, top=top_k)[0]
    return [d[1] for d in decoded]
