import cv2
import numpy as np


def get_img(path: str):
    img = cv2.imread(path, 0)
    img = np.flipud(img)
    return img, img.shape[0], img.shape[1]


def update(updated_path: str):
    return get_img(updated_path)
