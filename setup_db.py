import os, sys, logging
import sqlalchemy
import csv
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Table, Date
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy_utils import database_exists, create_database
from models import Train, Test

LEVELS = { 'debug':logging.DEBUG,
            'info':logging.INFO,
            'warning':logging.WARNING,
            'error':logging.ERROR,
            'critical':logging.CRITICAL,
            }

if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)

database_uri='postgresql://{0}:{1}@localhost/{2}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

#check if database exists and if not create database convo
if not database_exists(database_uri):
    print 'Database {0} does not exist'.format(sys.argv[3])
    print 'Creating database {0}'.format(sys.argv[3])
    create_database(database_uri)
    print 'Database {0} created'.format(sys.argv[3])

#connect to sqlalchemy engine
engine = create_engine(database_uri)
Session = sessionmaker(bind=engine)
session=Session()

Base = declarative_base()

class Train(Base):
    __tablename__ = 'training_data'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(Date)
    category = Column(String(50))
    cat_num = Column(Integer)
    desc = Column(String(200))
    day = Column(String(20))
    day_num = Column(Integer)
    pd_district = Column(String(20))
    pd_district_num = Column(Integer)
    resolution = Column(String(50))
    address = Column (String(50))
    x = Column(Float)
    y = Column(Float)
    def __repr__(self):
        return "<Train(date='%s', category='%s', cat_num=%d, desc='%s', day='%s', day_num=%d, pd_district='%s', \
                    'pd_district_num=%d', resolution='%s', address='%s', x='%d', y='%d')>" % \
                    (self.date, self.category, self.cat_num, self.desc, self.day, self.day_num, self.pd_district, \
                        self.pd_district_num, self.resolution, self.address, self.x, self.y)


class Test(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(Date)
    day = Column(String(20))
    day_num = Column(Integer)
    pd_district = Column(String(20))
    pd_district_num = Column(Integer)
    address = Column (String(50))
    x = Column(Float)
    y = Column(Float)
    def __repr__(self):
        return "<Train(date='%s', day='%s', day_num=%d, pd_district='%s', 'pd_district_num=%d', \
                    address='%s', x='%d', y='%d')>" % \
                    (self.date, self.day, self.day_num, self.pd_district, self.pd_district_num, \
                    self.address, self.x, self.y)

#create tables Node and node_to_node
Base.metadata.create_all(engine, checkfirst=True)




engine = create_engine('postgresql://train:kaggle@localhost/{0}'.format(sys.argv[3]))
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

f=open('data/train.csv', 'rb')
reader = csv.reader(f)
i=0
for r in reader:
  if r[0]!='Dates':
    date=datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S')
    session.add(Train(date=date, \
              category=r[1], cat_num=categories.index(r[1]), desc=r[2], \
              day=r[3], day_num=days.index(r[3]), pd_district=r[4], \
              pd_district_num=pd_districts.index(r[4]), resolution=r[5], address=r[6], \
              x=r[7], y=r[8]))

    session.commit()

f.close()

'''
f=open('data/test.csv', 'rb')
reader = csv.reader(f)
i=0
for r in reader:
  if r[0]!='Dates':
    date=datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S')
    session.add(Test(date=date, \
              day=r[2], day_num=days.index(r[2]), pd_district=r[3], \
              pd_district_num=pd_districts.index(r[3]), address=r[4], \
              x=r[5], y=r[6]))

    session.commit()

f.close()
'''