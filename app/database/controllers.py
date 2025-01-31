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


    def get_top_pct(self):
        """ Get the PCT with the highest count of Gps"""
        result = db.session.query(
            PrescribingData.PCT,
            func.count(func.distinct(PrescribingData.practice)).label('num_practices')
        ).group_by(PrescribingData.PCT).order_by(
            func.count(func.distinct(PrescribingData.practice)).desc()
        ).first()

        # Get the PCT with the highest number of distinct practices and the count itself
        most_recurring_PCT = result[0] if result else None
        distinct_practice_count = result[1] if result else 0

        return most_recurring_PCT, distinct_practice_count

    def get_top_5_antidepressants(self):
        """Returns the top 5 prescribed antidepressant names along with their quantities."""
        subquery = db.session.query(
            PrescribingData.BNF_name,
            func.sum(PrescribingData.quantity).label('total_quantity')
        ).filter(
            PrescribingData.BNF_code.like('0403%'),
            ~PrescribingData.BNF_name.like('Amitrip%')
        ).group_by(PrescribingData.BNF_name).subquery()

        result = db.session.query(subquery.c.BNF_name, subquery.c.total_quantity) \
            .order_by(subquery.c.total_quantity.desc()) \
            .limit(5).all()

        # Debugging: Print the result
        print("Top 5 antidepressants:", result)

        # Extract names and quantities
        BNF_names = [row.BNF_name for row in result]
        quantities = [row.total_quantity for row in result]

        return BNF_names, quantities





db.session.execute