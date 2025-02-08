"""
NAME:          models.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          22/11/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Database ORM class
"""
from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, aliased, relationship
from collections import namedtuple



class PrescribingData(db.Model):
    """class for the prescription data table."""
    __tablename__ = 'practice_level_prescribing'
    id = db.Column(db.Integer, primary_key=True)
    SHA = db.Column(db.String(3))
    PCT = db.Column(db.String(3))
    practice = db.Column(db.String(6))
    BNF_code = db.Column("BNFCODE", db.String(15))
    BNF_name = db.Column("BNFNAME", db.String(40))
    items = db.Column(db.Integer)
    NIC = db.Column(db.Float)
    ACT_cost = db.Column("ACTCOST", db.Float)
    quantity = db.Column(db.Integer)
    practices = db.relationship("PracticeData", back_populates = "practice_level_prescribing")

class PracticeData(db.Model):
    """Class for the practice address data table."""
    __tablename__ = 'practices'
    code = db.Column("CODE", db.String(6), db.ForeignKey('practice_level_prescribing.practice'))
    practice_name = db.Column("PRACTICE", db.Text, primary_key=True)
    address_line_1 = db.Column("ADDRESS1",db.Text)
    address_line_2 = db.Column("ADDRESS2",db.Text)
    area = db.Column("AREA",db.Text)
    city = db.Column("CITY", db.Text)
    post_code = db.Column("POSTCODE", db.String(10))
    practice_level_prescribing = db.relationship("PrescribingData", back_populates = "practices")
   


            



