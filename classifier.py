import os
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
from models import *
from nltk import *

Base = declarative_base()

database_uri='postgresql://{0}:{1}@localhost/{2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

Session = sessionmaker(bind=engine)

session=Session()

def classifier():
  sum=0.0
  num=0.0
  #for i in range(0, 191349):
  #for i in range(90000, 100000):  7.276
  #for i in range(40000, 50000): 6.19
  #for i in range(130000, 140000): 6.747
  #for i in range(1, 10001): #6.382
  for i in range(170000, 180000): #6.723
    print i
  #for i in range(1, 10):
    c=session.query(Test).filter(Test.visitnumber==i).count()
    if c > 0:
      sum=sum+c
      num+=1
  print sum/num


if __name__ == '__main__':
  classifier()