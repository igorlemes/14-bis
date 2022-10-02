# Class to read image from file or URL
import cv2
import numpy as np
import zipfile as zp

class Image:
    def __init__(self, filename):
        """ Constructor """
        self.filename = filename
        self.data = Data(filename)
        self.height, self.width, self.channels = self.data.shape

    def open_images(self, filename):
        """ Open 3 grey images and combine them in one colored image  """
        # regex of filename to find if it is a blue, green or red image
        image = cv2.imread(filename)
        return image

    def copy(self):
        """ Return a copy of image """
        return Image(self.filename)

    def get_histogram(self):
        """ Return histogram of image """
        hist = cv2.calcHist([self.image], [0], None, [256], [0, 256])
        return hist

    def get_blue(self):
        """ Returns blue channel of image """
        return self.image[:,:,0]
    
    def get_green(self):
        """ Returns green channel of image """
        return self.image[:,:,1]
    
    def get_red(self):
        """ Returns red channel of image """
        return self.image[:,:,2]
    
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
        aux = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        plt.imshow(self.filename, self.image)
        plt.plot()

class Data:
    def __init__(self, filename):
        """ Constructor """
        self.data = Unzip(filename).get_data()
        self.r = self.get_red() 
        self.g = self.get_green()
        self.b = self.get_blue()

    def get_blue(self):
        """ Returns blue channel of image """
        return self.data[:,:,0]
    
    def get_green(self):
        """ Returns green channel of image """
        return self.data[:,:,1]

    def get_red(self):
        """ Returns red channel of image """
        return self.data[:,:,2]

class Unzip:
    def __init__(self, filename):
        self.filename = filename

    def unzip_it(self):
        with zp.ZipFile(self.filename, mode="r") as archive:
         for file in archive.namelist():
             if file.endswith(".png"):
                archive.extract(file, "output_dir/")

    def get_data(self):
        zip = zp(self.filename)
        return {name: zip.read(name) for name in zip.namelist()}
