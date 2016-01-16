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
from models import *
from nltk import *
import matplotlib.pyplot as plt

Base = declarative_base()

database_uri='postgresql://{0}:{1}@localhost/{2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

#connect to sqlalchemy engine
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session=Session()

'''
Finds the frequency of crimes per day for all years from 2003-2015
Friday is a very popular day to commit a crime
'''
def crimes_per_day_all():

  crime_count=[]
  crime_count.append(session.query(Train).filter(Train.day=='Sunday').count())
  crime_count.append(session.query(Train).filter(Train.day=='Monday').count())
  crime_count.append(session.query(Train).filter(Train.day=='Tuesday').count())
  crime_count.append(session.query(Train).filter(Train.day=='Wednesday').count())
  crime_count.append(session.query(Train).filter(Train.day=='Thursday').count())
  crime_count.append(session.query(Train).filter(Train.day=='Friday').count())
  crime_count.append(session.query(Train).filter(Train.day=='Saturday').count())

  fig = plt.figure()
  ax = fig.add_subplot(111)
  #Sunday = 1, .... Saturday = 7
  x=range(1,8)
  l = plt.plot(x, crime_count, 'r--', linewidth=1)
  plt.xlabel('Day')
  plt.ylabel('Count')
  plt.title(r'Number of Crimes per day')

  # Tweak spacing to prevent clipping of ylabel
  plt.subplots_adjust(left=0.15)
  for i,j in zip(x,crime_count):
    ax.annotate(str(j),xy=(i,j))

  plt.show()

'''
Finds the frequency of crimes per day per year and plots them all to see if Friday is still 
a good day to commit a crime. (It is)
'''
def crimes_per_day_per_year():

  crime_count_year=[]
  for year in range(2003, 2016):
    crime_count=[]
    crime_count.append(session.query(Train).filter(Train.day=='Sunday', extract('year', Train.date) == year).count())
    crime_count.append(session.query(Train).filter(Train.day=='Monday', extract('year', Train.date) == year).count())
    crime_count.append(session.query(Train).filter(Train.day=='Tuesday', extract('year', Train.date) == year).count())
    crime_count.append(session.query(Train).filter(Train.day=='Wednesday', extract('year', Train.date) == year).count())
    crime_count.append(session.query(Train).filter(Train.day=='Thursday', extract('year', Train.date) == year).count())
    crime_count.append(session.query(Train).filter(Train.day=='Friday', extract('year', Train.date) == year).count())
    crime_count.append(session.query(Train).filter(Train.day=='Saturday', extract('year', Train.date) == year).count())
    crime_count_year.append(crime_count)

  fig = plt.figure()
  #Sunday = 1, .... Saturday = 7
  x=range(1,8)
  # These are the colors that will be used in the plot
  color_sequence = ['#1f77b4', '#aec7e8', '#ff7f0e', '#ffbb78', '#2ca02c', \
                    '#98df8a', '#d62728', '#ff9896', '#9467bd', '#c5b0d5', \
                    '#8c564b', '#c49c94', '#e377c2', '#f7b6d2', '#7f7f7f', \
                    '#c7c7c7', '#bcbd22', '#dbdb8d', '#17becf', '#9edae5']

  i=0
  for cc in crime_count_year:
    plt.plot(x, cc, 'r--', linewidth=1, color=color_sequence[i])
    i+=1
  plt.xlabel('Day')
  plt.ylabel('Count')
  plt.title(r'Number of Crimes per day')
  # Tweak spacing to prevent clipping of ylabel
  plt.subplots_adjust(left=0.15)
  plt.show()

if __name__ == '__main__':
  crimes_per_day_per_year()