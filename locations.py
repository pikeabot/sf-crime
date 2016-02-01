import os, sys
from os import listdir
from os.path import isfile, join
import csv
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, BigInteger
from sqlalchemy import String, ForeignKey, Float, Table, Sequence
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, relationship
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.dialects import postgresql
from numpy import ndarray
import matplotlib.pyplot as plt
sys.path.append('..')
from models import *
from sklearn import tree

Base = declarative_base()
database_uri='postgresql://{0}:{1}@localhost/{2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
#connect to sqlalchemy engine
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session=Session()

def plot_locations(category):

  X = session.query(Train.x).filter(Train.category==category).all()
  Y = session.query(Train.y).filter(Train.category==category).all()
  
  fig = plt.figure()
  plt.xlim([-122.3,-122.6])
  plt.ylim([37.83, 37.68])
  
  l = plt.plot(X, Y, 'ro', linewidth=1)
  plt.xlabel('lat')
  plt.ylabel('long')
  plt.title('Location of {0}'.format(category))
  
  '''
  map = Basemap(projection='merc', lat_0 = 37.7, lon_0 = -122.4, \
    resolution = 'h', area_thresh = 0.1, \
    llcrnrlon=-121, llcrnrlat=35, \
    urcrnrlon=-124, urcrnrlat=39)
 
  map.drawcoastlines()
  map.drawcountries()
  map.fillcontinents(color = 'coral')
  map.drawmapboundary()
  '''
  plt.show()
  

if __name__ == '__main__':
  #plot_locations('LARCENY/THEFT')
  #plot_locations('PROSTITUTION')
  plot_locations('OTHER OFFENSES')
  plot_locations('DRUG/NARCOTIC')