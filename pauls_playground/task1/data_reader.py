import pandas as pd
import numpy as np


class DataReader:
    """
    DataReader is cunstructed to read a file
    :param path:read a file
    """

    def __init__(self):
        self.data_read = None
        self.read_one = None

    def load_data(self, path):
        """
        The Methode is there to load a file and read it
        :param path: read a file
        """
        self.data_read = pd.read_csv(filepath_or_buffer=path)
        #print(self.data_read.head())
        print(self.data_read.loc[0])
        #Titel werden ausgegeben
        #print(self.data_read.keys())
        #self.read_one = self.data_read.loc[1, "longitude"]




# class DataCompare:
#     """
#
#     :param path:
#     """
#
#     def __init__(self):
#         self.data_read = None
#         self.data_read_one = None
#         wert = None
#
#     def load_one_data(self, path):
#         """
#
#         :param path:
#         """
#         self.data_read_one = self.data_read.iat[0, 0]
