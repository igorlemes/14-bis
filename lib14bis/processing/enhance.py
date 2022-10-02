import cv2
import matplotlib.pyplot as plt
import numpy as np
import copy


# class ImageMock:
#     def __init__(self, name):
#         self.data = cv2.imread(name)

#     def __repr__(self):
#         print(self.data)

#     def show(self):
#         aux = cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB)
#         plt.imshow(aux)
#         plt.plot()
#         # cv.imshow("Mock img", self.data) # não funciona com jupyter

#     def copy(self):
#         return copy.deepcopy(self)

#     @property
#     def b(self):
#         return self.data[:, :, 0]

#     @b.setter
#     def b(self, newValues):
#         self.data[:, :, 0] = newValues

#     @property
#     def g(self):
#         return self.data[:, :, 1]

#     @g.setter
#     def g(self, newValues):
#         self.data[:, :, 1] = newValues

#     @property
#     def r(self):
#         return self.data[:, :, 2]

#     @r.setter
#     def r(self, newValues):
#         self.data[:, :, 2] = newValues

#     def save(self, name):
#         cv2.imwrite(name, self.data)


class Enhance:

    def sharpen(img, times=1):
        newImg = img.copy()
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])
        for _ in range(times):
            newImg.data.image = cv2.filter2D(
                src=newImg.data.image, ddepth=-1, kernel=kernel)

        return newImg

    def emboss(img):
        newImg = img.copy()
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        newImg.data.image = cv2.filter2D(
            src=newImg.data.image, ddepth=-1, kernel=kernel)

        return newImg

    def multiply(img, facs):
        new_img = img.copy()
        # red
        new_img.data.r = np.floor(img.data.r * facs[0])
        # green
        new_img.data.g = np.floor(img.data.g * facs[1])
        # blue
        new_img.data.b = np.floor(img.data.b * facs[2])

        return new_img
