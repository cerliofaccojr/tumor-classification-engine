#!/usr/bin/env python
# coding=utf-8

"""AcquisitorAndCleaner engine action.

Use this module to add the project main code.
"""

from .._compatibility import six
from .._logging import get_logger
import pandas as pd

from marvin_python_toolbox.engine_base import EngineBaseDataHandler\

__all__ = ['AcquisitorAndCleaner']


logger = get_logger('acquisitor_and_cleaner')


class AcquisitorAndCleaner(EngineBaseDataHandler):

    def __init__(self, **kwargs):
        super(AcquisitorAndCleaner, self).__init__(**kwargs)

    def execute(self, params, **kwargs):
        featureNames = ['BI_RADS', 'age', 'shape', 'margin', 'density', 'severity']
        df = pd.read_csv("/Users/cerliojunior/Downloads/DataScience-Python3/mammographic_masses.data.txt", na_values=['?'],  names = featureNames)
        df.dropna(inplace=True)
        self.marvin_initial_dataset = df
