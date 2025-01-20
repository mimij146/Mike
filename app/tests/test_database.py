"""
NAME:          test_database.py
AUTHOR:        Alan Davies (Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          24/12/2019
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Suite of tests for testing the dashboards database
               functionality.
"""

import unittest
from app import app
from app.database.controllers import Database

class DatabaseTests(unittest.TestCase):
    """Class for testing database functionality and connection."""
    def setUp(self):
        """Run prior to each test."""
        self.app = app
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db_mod = Database()
        


    def tearDown(self):
        """Run post each test."""
        self.app_context.pop()

    def test_get_total_number_items(self):
        """Test that the total number of items returns the correct value."""
        
        self.assertEqual(self.db_mod.get_total_number_items(), 8218165, 'Test total items returns correct value')
    
    def test_avg_act(self):
        """Test that the average ACT function returns the correct value"""
        self.assertEqual(self.db_mod.get_avg_act(),76.22, 'Test total items returns incorrect value')
    
     
    def test_avg_act(self):
        """Test that the average ACT function returns the correct value"""
        self.assertNotEqual(self.db_mod.get_avg_act(),99910)

    
    def test_unique_areas(self):
        """Test that the unique areas function returns the correct value"""
        self.assertEqual(self.db_mod.get_distinct_areas(),2399, 'Test total items returns incorrect value')
    
    def test_unique_areas(self):
        """Test that the unique areas function returns the correct value"""
        self.assertNotEqual(self.db_mod.get_distinct_areas(),2319998)
    
    def non_existing_db_function(self):
        """Te"""
        self.assertRaises(self.db_mod.not_existing(),NameError)
    
    def test_unique_items(self):
        self.assertEqual(self.db_mod.get_unique_items(), 13935)


    def test_total_spend(self):
        """"Test total spend function returns the correct value"""
        result = self.db_mod.get_total_spend_drugs()
        if isinstance(result, str):
            result = int(result.replace(",", ""))
        self.assertEqual(result, 2596402159)


if __name__ == "__main__":
    unittest.main()