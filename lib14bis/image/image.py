# Class to read image from file or URL

import cv2
import numpy as np
import zipfile as zp

class Image:
    def __init__(self, filename):
        self.filename = filename
        self.image = cv2.imread(filename, cv2.IMREAD_COLOR)
        self.height, self.width, self.channels = self.image.shape

    # open greyscale blue image file on openCV
    

    def get_histogram(self):
        # get histogram of image
        hist = cv2.calcHist([self.image], [0], None, [256], [0, 256])
        return hist
    
    

    def get_image(self):
        return self.image

    def get_blue(self):
        return self.image[:,:,0]
    
    def get_green(self):
        return self.image[:,:,1]
    
    def get_red(self):
        return self.image[:,:,2]
    
    def get_height(self):
        return self.height
    
    def get_width(self):
        return self.width

    def get_channels(self):
        return self.channels
    
    def save(self, filename):
        cv2.imwrite(filename, self.image)
    
    def show(self):
        cv2.imshow(self.filename, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

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