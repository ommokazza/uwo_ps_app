"""This generate label file from screenshot image by using learned model.
"""
import os

from PIL import Image
import tensorflow as tf
from tensorflow.saved_model import tag_constants

from uwo_ps_utils import common
from uwo_ps_utils import market_rates_cropper as mrc

class TensorFlowEstimator():
    def __init__(self, models, labels):
        """
        Arguments:
            models : The model directory list. [goods, towns, rates, arrows]
            labels : The label file list. [goods, towns, rates, arrows]
        """
        self.model_goods = models[0]
        self.model_towns = models[1]
        self.model_rates = models[2]
        self.model_arrows = models[3]

        self.goods_labels = open(labels[0]).read().splitlines()
        self.towns_labels = open(labels[1]).read().splitlines()
        self.rates_labels = open(labels[2]).read().splitlines()
        self.arrows_labels = open(labels[3]).read().splitlines()
        pass

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
        images = mrc.get_images_from_screenshot(path)
        if len(images) < 3:
            return []

        goods = self.__estimate_goods(images[0])
        rates = self.__estimate_rates(images[1])
        arrows = self.__estimate_arrows(images[2])
        result = [(goods, rates, arrows)]
        for i in range(3, len(images), 3):  
            towns = self.__estimate_towns(images[i])
            rates = self.__estimate_rates(images[i+1])
            arrows = self.__estimate_arrows(images[i+2])      
            result += [(towns, rates, arrows)]

        return result

    def __estimate_goods(self, im):
        resize_ratio = 6
        im = im.resize((int(im.width / resize_ratio),
                            int(im.height / resize_ratio)))
        index = common.estimate(self.model_goods, im.tobytes())
        return self.goods_labels[index]
    
    def __estimate_rates(self, im):
        index = common.estimate(self.model_rates, im.tobytes())
        return self.rates_labels[index]

    def __estimate_arrows(self, im):
        index = common.estimate(self.model_arrows, im.tobytes())
        return self.arrows_labels[index]

    def __estimate_towns(self, im):
        index = common.estimate(self.model_towns, im.tobytes())
        return self.towns_labels[index]