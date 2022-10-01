import cv2 as cv


class image_mock:
    def __init__(self, name):
        self.data = cv.imread(cv.samples.findFile(name))

    def show(self):
        cv.imshow("Mock img", self.data)

    def save(self, name):
        cv.imwrite(name, self.data)


class enhance:

    pass
