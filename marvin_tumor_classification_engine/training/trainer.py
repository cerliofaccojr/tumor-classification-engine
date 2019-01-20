#!/usr/bin/env python
# coding=utf-8

"""Trainer engine action.

Use this module to add the project main code.
"""

from .._logging import get_logger

from marvin_python_toolbox.engine_base import EngineBaseTraining

__all__ = ['Trainer']


logger = get_logger('trainer')

from sklearn import svm


class Trainer(EngineBaseTraining):

    def __init__(self, **kwargs):
        super(Trainer, self).__init__(**kwargs)

    def execute(self, params, **kwargs):
        clf = svm.SVC(kernel='rbf', C=1)
        clf = clf.fit(self.marvin_dataset["X_train"], self.marvin_dataset["y_train"])
        self.marvin_model = clf