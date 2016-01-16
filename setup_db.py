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
    desc = Column(String(200))
    day = Column(String(20))
    pd_district = Column(String(20))
    resolution = Column(String(50))
    address = Column (String(50))
    x = Column(Float)
    y = Column(Float)
    def __repr__(self):
        return "<Train(date='%s', category='%s', desc='%s', day='%s', pd_district='%s', \
                    resolution='%s', address='%s', x='%d', y='%d')>" % \
                    (self.date, self.category, self.desc, self.day, self.pd_district, self.resolution, \
                    self.address, self.x, self.y)


class Test(Base):
    __tablename__ = 'test_data'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    date = Column(Date)
    day = Column(String(20))
    pd_district = Column(String(20))
    address = Column (String(50))
    x = Column(Float)
    y = Column(Float)
    def __repr__(self):
        return "<Train(date='%s', day='%s', pd_district='%s', address='%s', x='%d', y='%d')>" % \
                    (self.date, self.day, self.pd_district, self.address, self.x, self.y)

#create tables Node and node_to_node
Base.metadata.create_all(engine, checkfirst=True)




engine = create_engine('postgresql://train:kaggle@localhost/{0}'.format(sys.argv[3]))
Session = sessionmaker(bind=engine)
session=Session()


f=open('data/train.csv', 'rb')
reader = csv.reader(f)
i=0
for r in reader:
  if r[0]!='Dates':
    date=datetime.strptime(r[0], '%Y-%m-%d %H:%M:%S')
    session.add(Train(date=date, \
              category=r[1], \
              desc=r[2], \
              day=r[3], pd_district=r[4], resolution=r[5], address=r[6], \
              x=r[7], y=r[8]))

    session.commit()

f.close()

'''
f=open('test.json', 'rb')
test_lines=''.join(f.readlines())
jtlines = json.loads(test_lines)

for jt in jtlines:
  #add recipe
  new_test_recipe = Test(recipe_id=jt['id'], ingredients=[]) 
  for i in jt['ingredients']:
    new_test_ingredient = Test_Ingredients(ingredient=i)
    new_test_recipe.ingredients.append(new_test_ingredient)
    session.add(new_test_ingredient)
  session.add(new_test_recipe)

  session.commit()

f.close()
'''