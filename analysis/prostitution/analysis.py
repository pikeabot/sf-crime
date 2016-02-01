import os, sys
from os import listdir
from os.path import isfile, join
import csv
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, BigInteger
from sqlalchemy import String, ForeignKey, Float, Table, Sequence
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.expression import extract
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
import numpy as np
from sklearn import neighbors, datasets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
sys.path.append('../..')
from models import *


CATEGORY='PROSTITUTION'

Base = declarative_base()
database_uri='postgresql://{0}:{1}@localhost/{2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
#connect to sqlalchemy engine
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session=Session()

def print_info():
    X = session.query(Train.x).filter(Train.category==CATEGORY).all()
    Y = session.query(Train.y).filter(Train.category==CATEGORY).all()
    print "Variance of longitude: {0}".format(np.var(X))
    print "Variance of latitude: {0}".format(np.var(Y))
    print "Mean of longitude: {0}".format(np.mean(X))
    print "Mean of latitude: {0}".format(np.mean(Y))
    print "Median of longitude: {0}".format(np.median(X))
    print "Median of latitude: {0}".format(np.median(Y))
    print "Standard deviation of longitude: {0}".format(np.std(X))
    print "Standard deviation of latitude: {0}".format(np.std(Y))

def plot_X_vs_t(category):

  Xc = session.query(Train.x).filter(Train.category==category).all()
  Tc = session.query(Train.datetime).filter(Train.category == category).all()
  tc=[time[0].hour for time in Tc]

  Xw = session.query(Train.x).filter(Train.category=='WEAPON LAWS').all()
  Tw = session.query(Train.datetime).filter(Train.category == 'WEAPON LAWS').all()
  tw=[time[0].hour for time in Tw]

  fig = plt.figure()
  #plt.xlim([-122.3,-122.6])
  #plt.ylim([37.83, 37.68])
  
  l = plt.plot(Xc, tc, 'ro', Xw, tw, 'g^')
  plt.ylabel('t')
  plt.xlabel('long')
  plt.title('Longitude of {0}'.format(category))

  plt.show()

def knn_X_vs_t():

    n_neighbors = 15

    Xp = session.query(Train.x, Train.datetime).filter(Train.category=='PROSTITUTION').all()
    X=[]
    y=[]
    for x in Xp:
        X=np.append(X, [x[0], int(x[1].hour)])
    for i in range(0, len(Xp)):
        y=np.append(y, 'PROSTITUTION')

    Xw = session.query(Train.x, Train.datetime).filter(Train.category=='WEAPON LAWS').all()
    for x in Xw:
        X=np.append(X, [x[0], int(x[1].hour)])
    for i in range(0, len(Xw)):
        y=np.append(y, 'WEAPON LAWS')
    y=y.reshape(1, -1)

    h = .02  # step size in the mesh
    '''
    # Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    for weights in ['uniform', 'distance']:
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        clf.fit(X, y)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, m_max]x[y_min, y_max].
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        plt.figure()
        plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

        # Plot also the training points
        plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
        plt.xlim(xx.min(), xx.max())
        plt.ylim(yy.min(), yy.max())
        plt.title("3-Class classification (k = %i, weights = '%s')"
                  % (n_neighbors, weights))

    plt.show()
    '''
if __name__ == '__main__':
  #print_info()
  #plot_X_vs_t('PROSTITUTION')
  knn_X_vs_t()