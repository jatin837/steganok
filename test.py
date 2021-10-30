import cv2
import numpy as np
import matplotlib.pyplot as plt

class Message():
    def __init__(self, content):
        self.content = content

    def to_bin(self):
        if type(self.content) == str:
            return ''.join(
            [format(ord(i), "08b") for i in self.content])

        elif type(self.content) == bytes or type(self.content) == np.ndarray:
            return [format(i, "08b") for i in self.content ]
        elif type(self.content) == int or type(self.content) == np.uint8:
            return format(self.content, "08b")
        else:
            raise TypeError("Input type not supported")

class Image():
    def __init__(self, path):
        self.path = path
        self.image = cv2.cvtColor(
                cv2.imread(self.path), 
                cv2.COLOR_BGR2RGB)

    def get_pxl_vals(self):
        return np.float32(self.image.reshape((-1, 3)))

    def __repr__(self):
        return f"image at {self.path}"

    def cluster(self, k):
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

        _, self.labels, (self.centers) = cv2.kmeans(
                self.get_pxl_vals(), 
                k, 
                None, 
                criteria, 
                10, 
                cv2.KMEANS_RANDOM_CENTERS)

        self.centers = np.uint32(self.centers)
        self.labels = self.labels.reshape(1, -1)


    def get_indx_for_cluster(self, k):
        return np.where(self.labels == k)

if __name__ == "__main__":
    image = Image("test.png")
    pixel_values = image.get_pxl_vals()

    k = 7
    image.cluster(k)
    image.labels
    image.centers
    print("DONE")
