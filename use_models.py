from keras.models import load_model
from scipy import misc

model = load_model('model/mnist.h5')
img_rows, img_cols = 28, 28
image_file = "image.png"


def _save_image(data):
    with open(image_file, 'wb') as fh:
        fh.write(data)
        fh.close()


def _get_score():
    face = misc.imread(image_file, flatten=True, mode='L')
    face = misc.imresize(face, (img_rows, img_cols), mode='L')
    image = face.reshape(1, img_rows, img_cols, 1)
    image = image.astype('float32')
    return model.predict_classes(image)


def recognize_image(data):
    _save_image(data)
    return _get_score()

if __name__ == '__main__':
    print(_get_score())
