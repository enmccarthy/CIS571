from __future__ import division
import numpy as np


class GaussianNB(object):
    def __init__(self, alpha=1.0):
        self.alpha = alpha

    def fit(self, X, y):
