import cv2
import matplotlib.pyplot as plt
import numpy as np


class ImageMock:
    def __init__(self, name):
        self.data = cv2.imread(name)

    def show(self):
        aux = cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB)
        plt.imshow(aux)
        plt.plot()
        # cv.imshow("Mock img", self.data) # não funciona com jupyter

    @property
    def r(self):
        return self.data[:, :, 0]

    def save(self, name):
        cv2.imwrite(name, self.data)


class Enhance:

    def sharpen(img):
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

        return cv2.filter2D(src=img.data, ddepth=-1, kernel=kernel)

    def emboss(img):
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])

        return cv2.filter2D(src=img.data, ddepth=-1, kernel=kernel)

    def multiply(img, facs):

        new_img = img.copy()

        # red
        img.data.r *= facs[0]
        # green
        img.data.g *= facs[1]
        # blue
        img.data.b *= facs[2]

        return new_img
