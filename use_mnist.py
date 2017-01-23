from keras.models import load_model
from keras.datasets import mnist

model = load_model('model/mnist.h5')

img_rows, img_cols = 28, 28

(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train[10].reshape(1, img_rows, img_cols, 1)
X_train = X_train.astype('float32')

score = model.predict_classes(X_train)

print(score[0])