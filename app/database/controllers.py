"""
NAME:          database\controllers.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          17/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Contains the Database class that contains all the methods used for accessing the database
"""

from sqlalchemy.sql import func
from flask import Blueprint

from app import db
from app.database.models import PrescribingData, PracticeData

database = Blueprint('dbutils', __name__, url_prefix='/dbutils')

class Database:
    """Class for managing database queries."""
    
    def convert_tuple_list_to_raw(self, tuple_list):
        """Helper function to convert results from tuple list to plain list."""
        order_row = [tuple(row) for row in tuple_list]
        return  [item for i in order_row for item in i]
    
    def get_total_number_items(self):
        """Return the total number of prescribed items."""
        return int(db.session.execute(db.select(func.sum(PrescribingData.items))).first()[0])
            
    def get_prescribed_items_per_pct(self):
        """Return the total items per PCT."""
        result = db.session.execute(db.select(func.sum(PrescribingData.items).label('item_sum')).group_by(PrescribingData.PCT)).all()
        return self.convert_tuple_list_to_raw(result)

    def get_distinct_pcts(self):
        """Return the distinct PCT codes."""
        result = db.session.execute(db.select(PrescribingData.PCT).distinct()).all()
        return self.convert_tuple_list_to_raw(result)

    def get_n_data_for_PCT(self, pct, n):
        """Return all the data for a given PCT."""
        return db.session.query(PrescribingData).filter(PrescribingData.PCT == pct).limit(n).all()
    

    def get_avg_act(self):
        """Returns the average ACT cost"""      
        return round(db.session.execute(db.select(func.avg(PrescribingData.ACT_cost))).first()[0],2)
    
    def get_distinct_areas(self):
        """Returns the total number of areas."""
        result = db.session.execute(db.select(PracticeData.area).distinct()).all()
        return len(tuple(self.convert_tuple_list_to_raw(result)))

    def get_total_spend_drugs(self):
        """"Returns total spend on drugs for all practices"""
        total_spend = int(db.session.execute(db.select(func.sum(PrescribingData.items * PrescribingData.ACT_cost))).first()[0])
        return f"{total_spend: ,}"
    def get_unique_items(self):
        """Returns the number of unique items prescribed"""
        return len(db.session.execute(db.select(PrescribingData.BNF_code).distinct()).all())

    def get_total_gp_practice(self):
        """Returns the total number of GP practices."""
        result = db.session.execute(db.select(func.count(PracticeData.code))).scalar()
        return result
        
        
        

db.session.execute