# -*- coding: utf-8 -*-
import pandas as pd 

path = ''
filename = 'clustering_dataset_01.xlsx'
xls = pd.ExcelFile(path + filename)
df = pd.read_excel(xls, 'clustering_dataset_01')

x1 = df[0]
x2 = df[1]
print(x1)
# Building block functions:
    
def dist(x1, x2):
    """ Return euclidean distance between x1 and x2 """
    # todo
    pass

def centroid(xList):
    """ Compute centroid of multi-dimensional x data in xList """
    # TODO
    pass

def assignmentDiffers(yCurrent, yPrev):
    """ Return True if yCurrent differs from yPrev """
    # TODO
    pass

# Let's use a class for our K-Means implementation
class KMeans:
    """ Perform k-means clustering """
    
    def __init__(self, k=5):
        self.k = k          # number of clusters
        self.means = None   # means of clusters
        
    def classify(self, x):
        """ Return the index of the cluster closest to the input """
        # TODO
        pass
    
    def train(self, data):
        """ Train model based on data """
        # TODO assign to self.means, one per cluster
        pass


def kmeans(x, k):
    # Use it like this?
    km = KMeans(k = 10)
    km.train(x)
    # can print out km.means to see the fit means
    # can call km.classify([1,2,3,4]) to get cluster index
    
    #The function should return a list the length of x that contains
    # the cluster number (1 - k) for the corresponding x point
    # TODO determine return value
