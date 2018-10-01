"""This generate label file from screenshot image by using learned model.
"""
import os

from PIL import Image
import tensorflow as tf
from tensorflow.saved_model import tag_constants

from uwo_ps_utils import common
from uwo_ps_utils import market_rates_cropper as mrc

class ImageCompareEstimator():
    ARROW_PIXEL_XY = (7, 7)
    ARROW_RGB = [(225, 129, 38), (160, 227, 37), (30, 227, 200)]

    def __init__(self, models, labels):
        """
        Arguments:
            models : The model directory list. [goods, towns, rates, arrows]
            labels : The label file list. [goods, towns, rates, arrows]
        """
        self.model_goods = models[0]
        self.model_towns = models[1]

        self.goods_labels = open(labels[0]).read().splitlines()
        self.towns_labels = open(labels[1]).read().splitlines()
        self.arrows_labels = open(labels[3]).read().splitlines()

    def estimate(self, path):
        """Estimation function.

        Arguments:
            path (str): Image file path to estimate

        Returns:
            Labels which are estimated
                [0] = (goods_label, rates, arrows)
                [1] = (nearby town1, rates, arrows)
                    ~
                [5] = (nearby town5, rates, arrows)
        """

        im = Image.open(path)
        try:
            goods_cell = mrc.get_selected_goods_cell_image(im)
            goods_imgs = mrc.get_images_from_goods_cell(goods_cell)
            goods = self.__estimate_goods(goods_imgs[0])
            rates = self.__estimate_rates(goods_imgs[3])
            arrows = self.__estimate_arrows(goods_imgs[2])
            result = [(goods, rates, arrows)]
        except:
            return []

        nearby_cells = mrc.get_nearby_towns_cell_images(im)
        for cell in nearby_cells:
            try:
                imgs = mrc.get_images_from_nearby_cell(cell)
                towns = self.__estimate_towns(imgs[0])
                rates = self.__estimate_rates(imgs[3])
                arrows = self.__estimate_arrows(imgs[2])
                result += [(towns, rates, arrows)]
            except:
                continue

        return result

    def __estimate_goods(self, im):
        resize_ratio = 6
        im = im.resize((int(im.width / resize_ratio),
                            int(im.height / resize_ratio)))
        index = common.estimate(self.model_goods, im.tobytes())
        return self.goods_labels[index]

    def __estimate_rates(self, im):
        count, _ = list(filter(self.__colored_pixel, im.getcolors()))[0]
        return str(int(count * 2.13))

    def __colored_pixel(self, pixels):
        _, rgb = pixels
        return not (rgb[0] < 75 and rgb[1] < 75 and rgb[2] < 75)

    def __estimate_arrows(self, im):
        pixel = im.getpixel(self.ARROW_PIXEL_XY)
        diffs = []
        for rgb in self.ARROW_RGB:
            diffs += [self.__get_rgb_diff(pixel, rgb)]

        return self.arrows_labels[diffs.index(min(diffs))]

    def __get_rgb_diff(self, px1, px2):
        diff = 0
        for i in range(3):
            diff += (px1[i] - px2[i]) ** 2
        return diff

    def __estimate_towns(self, im):
        index = common.estimate(self.model_towns, im.tobytes())
        return self.towns_labels[index]

