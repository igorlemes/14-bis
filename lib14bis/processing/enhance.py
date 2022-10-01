import cv2
import matplotlib.pyplot as plt


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

    pass
