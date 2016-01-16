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