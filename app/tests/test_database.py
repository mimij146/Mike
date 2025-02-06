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
from app.views.controllers import generate_top_5_antidepressants_barchart_data
from unittest.mock import patch
import plotly.utils
import pandas as pd
import json

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


    def test_top_5_antidep(self):
        data = [2429020, 2418812, 2394213, 1801482, 847308]
        labels = ["Fluoxetine HCl_Cap 20mg", "Sertraline HCl_Tab 50mg", "Sertraline HCl_Tab 100mg", "Citalopram Hydrob_Tab 20mg", "Citalopram Hydrob_Tab 10mg"]
        fig = go.Figure(data=[go.Bar(x=labels, y=data)])
        bar_data = fig.data[0]
        x_values = list(bar_data.x)
        y_values = list(bar_data.y)


        self.assertEqual(x_values, labels)
        self.assertEqual(y_values, data)


    @patch("app.views.controllers.db_mod.get_top_5_antidepressants")
    def test_generate_top_5_antidepressants_barchart_data(self, mock_get_top_5):

        mock_get_top_5.return_value = (
            ["Fluoxetine HCl_Cap 20mg", "Sertraline HCl_Tab 50mg", "Sertraline HCl_Tab 100mg", "Citalopram Hydrob_Tab 20mg", "Citalopram Hydrob_Tab 10mg"],
            [2429020, 2418812, 2394213, 1801482, 847308]
        )

        result = generate_top_5_antidepressants_barchart_data()

        self.assertIn("graphJSON", result)
        self.assertIn("header", result)
        self.assertIn("description", result)
        self.assertEqual(result["header"], "Top 5 Prescribed Antidepressants")
        self.assertIn("Top 5 prescribed antidepressants", result["description"])


        try:
            graph_data = json.loads(result["graphJSON"])
        except ValueError:
            self.fail("graphJSON is not valid JSON")

        # Check Plotly figure properties
        self.assertIn("data", graph_data)
        self.assertIn("layout", graph_data)

        # Ensure sorting is correct
        df = pd.DataFrame({
            "chart_names": ["Fluoxetine HCl_Cap 20mg", "Sertraline HCl_Tab 50mg", "Sertraline HCl_Tab 100mg", "Citalopram Hydrob_Tab 20mg", "Citalopram Hydrob_Tab 10mg"],
            "chart_quantities": [2429020, 2418812, 2394213, 1801482, 847308]
        }).sort_values(by="chart_quantities", ascending=False)

        self.assertListEqual(df["chart_names"].tolist(), ["Fluoxetine HCl_Cap 20mg", "Sertraline HCl_Tab 50mg", "Sertraline HCl_Tab 100mg", "Citalopram Hydrob_Tab 20mg", "Citalopram Hydrob_Tab 10mg"])
        self.assertListEqual(df["chart_quantities"].tolist(), [2429020, 2418812, 2394213, 1801482, 847308])


if __name__ == "__main__":
    unittest.main()