# Class to read image from file or URL
import cv2
import numpy as np
import zipfile as zp
import matplotlib.pyplot as plt


class Image:
    def __init__(self, filename):
        """ Constructor """
        self.filename = filename
        self.data = Data(filename)
        self.height, self.width, self.channels = self.data.shape

    def copy(self):
        """ Return a copy of image """
        return Image(self.filename)

    def get_histogram(self):
        """ Return histogram of image """
        hist = cv2.calcHist([self.image], [0], None, [256], [0, 256])
        return hist

    def get_height(self):
        """ Returns height of image """
        return self.height

    def get_width(self):
        """ Returns width of image """
        return self.width

    def get_channels(self):
        """ Returns number of channels of image """
        return self.channels

    def save(self, filename):
        """ Save image to file """
        cv2.imwrite(filename, self.image)

    def show(self):
        """ Show image """
        # print(self.data)
        aux = cv2.cvtColor(self.data.image, cv2.COLOR_BGR2RGB)
        plt.imshow(aux)
        plt.plot()


class Data:
    def __init__(self, filename):
        """ Constructor """
        self.image = self.load_images(filename)
        self.shape = self.image.shape
        self.r = self.get_red()
        self.g = self.get_green()
        self.b = self.get_blue()

    def load_images(self, filename):
        data = Unzip(filename).get_data()
        for name in data:
            if "blue" in name:
                blue = data[name]
                blue = cv2.cvtColor(blue, cv2.COLOR_BGR2GRAY)
            elif "green" in name:
                green = data[name]
                green = cv2.cvtColor(green, cv2.COLOR_BGR2GRAY)
            elif "red" in name:
                red = data[name]
                red = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
        return np.dstack((blue, green, red))

    def get_blue(self):
        """ Returns blue channel of image """
        return self.image[:, :, 0]

    def get_green(self):
        """ Returns green channel of image """
        return self.image[:, :, 1]

    def get_red(self):
        """ Returns red channel of image """
        return self.image[:, :, 2]


class Unzip:
    def __init__(self, filename):
        """ Constructor """
        self.filename = filename

    def unzip_it(self):
        """ Unzip file """
        with zp.ZipFile(self.filename, mode="r") as archive:
            for file in archive.namelist():
                if file.endswith(".png"):
                    archive.extract(file, "output_dir/")

    def get_data(self):
        """ Return data of image """
        zip = zp.ZipFile(self.filename)
        data = {}
        for name in zip.namelist():
            data[name] = cv2.imdecode(
                np.frombuffer(zip.read(name), np.uint8), 1)
        return data
