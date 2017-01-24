from keras.models import load_model
from scipy import misc

model = load_model('model/mnist.h5')
img_rows, img_cols = 28, 28


def recognize_image(data):
    image_file = "image.png"
    with open(image_file, 'w') as fh:
        fh.write(data)

    face = misc.imread(image_file, flatten=True, mode='L')
    for i in xrange(28):
        for j in xrange(28):
            face[i][j] = 255 - face[i][j]
    image = face.reshape(1, img_rows, img_cols, 1)
    image = image.astype('float32')
    return model.predict_classes(image)
