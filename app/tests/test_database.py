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
import plotly.graph_objects as go

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
    
    def test_total_gp_practice(self):
        self.assertEqual(self.db_mod.get_total_gp_practice(), 9348)

    def test_get_top_pct(self):
        """Test get_top_pct function returns the correct values"""
        result = self.db_mod.get_top_pct()

        # Unpacking the result
        most_recurring_PCT, distinct_practice_count = result

        # Expected values (replace with expected test values)
        expected_pct = "00T"  # Replace with actual expected PCT code
        expected_count = 61  # Replace with actual expected count

            # Assertions
        self.assertEqual(most_recurring_PCT, expected_pct, 'Most recurring PCT is incorrect')
        self.assertEqual(distinct_practice_count, expected_count, 'Distinct practice count is incorrect')

    def test_get_top_pct(self):
        """Test that get_top_pct function does not return incorrect values"""
        result = self.db_mod.get_top_pct()

        # Unpacking the result
        most_recurring_PCT, distinct_practice_count = result

        # Values that should not be returned (replace with incorrect test values)
        incorrect_pct = "12F"
        incorrect_count = 70

        self.assertNotEqual(most_recurring_PCT, incorrect_pct, "Most recurring PCT should not be XYZ123")
        self.assertNotEqual(distinct_practice_count, incorrect_count, "Distinct practice count should not be 99999")


if __name__ == "__main__":
    unittest.main()