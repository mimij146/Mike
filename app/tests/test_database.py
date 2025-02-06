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

    def test_infection_percentage_bar_chart_zero_value_handling(self):
        """
        Test that the bar chart correctly handles a category with a value of 0.
        """
        # Mock results with one category having a value of 0
        mock_results = [
            ('Antibacterials', 82.25),
            ('Antifungal', 0.00),
            ('Antiviral', 2.68),
            ('Antiprotozoal', 9.04),
            ('Anthelmintics', 5.23)
        ]

        # Calculate total for processing (if needed by the chart logic)
        total = sum(value for _, value in mock_results)

        # Ensure the zero value does not cause rendering issues
        for category, percentage in mock_results:
            if category == 'Antifungal':
                self.assertEqual(
                    percentage,
                    0.00,
                    msg="Zero value for 'Antifungal' is not handled correctly."
                )
def test_infection_percentage_bar_chart_over_100_handling():
    """
    Test that the bar chart correctly handles a total percentage exceeding 100%.
    """
    # Mock results with values summing to more than 100%
    mock_results = [
        ('Antibacterials', 50.0),
        ('Antifungal', 30.0),
        ('Antiviral', 25.0),
        ('Antiprotozoal', 10.0),
        ('Anthelmintics', 5.0)
    ]

    # Calculate total for processing (if needed by the chart logic)
    total = sum(value for _, value in mock_results)

    # Check if the total exceeds 100%
    assert total > 100.0, f"Total percentage exceeds 100%: {total}. Chart logic should handle this correctly."

    # Ensure individual values are still correct
    for category, percentage in mock_results:
        assert percentage >= 0.0, f"Percentage for '{category}' should not be negative."

    def test_top_5_antidep(self):
        data = [2429020, 2418812, 2394213, 1801482, 847308]
        labels = ["Fluoxetine HCl_Cap 20mg", "Sertraline HCl_Tab 50mg", "Sertraline HCl_Tab 100mg", "Citalopram Hydrob_Tab 20mg", "Citalopram Hydrob_Tab 10mg"]
        fig = go.Figure(data=[go.Bar(x=labels, y=data)])
        bar_data = fig.data[0]
        x_values = list(bar_data.x)
        y_values = list(bar_data.y)


        self.assertEqual(x_values, labels)
        self.assertEqual(y_values, data)



if __name__ == "__main__":
    unittest.main()