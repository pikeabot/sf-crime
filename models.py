import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float, Table, Date
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker, relationship

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
