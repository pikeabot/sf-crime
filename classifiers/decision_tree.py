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
sys.path.append('..')
from models import *
from sklearn import tree

Base = declarative_base()
database_uri='postgresql://{0}:{1}@localhost/{2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
#connect to sqlalchemy engine
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session=Session()

categories = ['PROSTITUTION', \
                'VANDALISM', \
                'SUSPICIOUS OCC', \
                'BURGLARY', \
                'LARCENY/THEFT', \
                'OTHER OFFENSES', \
                'STOLEN PROPERTY', \
                'TRESPASS', \
                'WARRANTS', \
                'FORGERY/COUNTERFEITING', \
                'KIDNAPPING', \
                'WEAPON LAWS', \
                'SEX OFFENSES FORCIBLE', \
                'DISORDERLY CONDUCT', \
                'BRIBERY', \
                'DRUNKENNESS', \
                'SECONDARY CODES', \
                'MISSING PERSON', \
                'EXTORTION', \
                'NON-CRIMINAL', \
                'EMBEZZLEMENT', \
                'TREA', \
                'RECOVERED VEHICLE', \
                'ARSON', \
                'PORNOGRAPHY/OBSCENE MAT', \
                'GAMBLING', \
                'VEHICLE THEFT', \
                'LOITERING', \
                'ASSAULT', \
                'BAD CHECKS', \
                'FRAUD', \
                'ROBBERY', \
                'DRUG/NARCOTIC', \
                'RUNAWAY', \
                'SEX OFFENSES NON FORCIBLE', \
                'DRIVING UNDER THE INFLUENCE', \
                'FAMILY OFFENSES', \
                'LIQUOR LAWS', \
                'SUICIDE']

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
pd_districts = ['BAYVIEW', 'INGLESIDE', 'NORTHERN', 'CENTRAL', 'MISSION', 'SOUTHERN', \
                    'TENDERLOIN', 'PARK', 'RICHMOND', 'TARAVAL']

def decision_tree():
  Y = session.query(Train.cat_num).filter(Train.id<1000).all()
  X = session.query(Train.x, Train.y).filter(Train.id<1000).all()

  clf=tree.DecisionTreeClassifier()
  clf = clf.fit (X, Y)
  #missing person
  c = clf.predict([-122.4334218863, 37.7303897123])
  print categories[c]

if __name__ == '__main__':
  decision_tree()