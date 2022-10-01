import cv2
import matplotlib.pyplot as plt
import numpy as np


class image_mock:
    def __init__(self, name):
        self.data = cv2.imread(name)

    def show(self):
        aux = cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB)
        plt.imshow(aux)
        plt.plot()
        # cv.imshow("Mock img", self.data) # não funciona com jupyter

    def save(self, name):
        cv2.imwrite(name, self.data)


class enhance:

    def sharpen(data):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

        return cv2.filter2D(src=data, ddepth=-1, kernel=kernel)
