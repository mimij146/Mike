"""
NAME:          views\controllers.py
AUTHOR:        Alan Davies (Senior Lecturer Health Data Science)
EMAIL:         alan.davies-2@manchester.ac.uk
DATE:          18/12/2019
UPDATED:       07/06/2024
INSTITUTION:   University of Manchester (FBMH)
DESCRIPTION:   Views module. Renders HTML pages and passes in associated data to render on the
               dashboard.
"""
import json
import plotly
import plotly.express as px
import pandas as pd
from flask import Blueprint, render_template, request, jsonify
from app.database.controllers import Database

views = Blueprint('dashboard', __name__, url_prefix='/dashboard')

# get the database class
db_mod = Database()

# Set the route and accepted methods
@views.route('/home/', methods=['GET', 'POST'])
def home():
    """Render the home page of the dashboard passing in data to populate dashboard."""
    pcts = db_mod.get_distinct_pcts()
    if request.method == 'POST':
        # if selecting PCT for table, update based on user choice
        form = request.form
        selected_pct_data = db_mod.get_n_data_for_PCT(str(form['pct-option']), 5)
    else:
        # pick a default PCT to show
        selected_pct_data = db_mod.get_n_data_for_PCT(str(pcts[0]), 5)

    # prepare data structure to send to front end to update display
    dashboard_data = {    
        "tile_data_items": generate_data_for_tiles(),  
        "top_items_plot_data": generate_top_px_items_barchart_data(),
        "pct_list": pcts,
        "pct_data": selected_pct_data,
        "total_quantity": db_mod.get_max_qantity_name_percent()[1],
        "top_drug_amount": db_mod.get_max_qantity_name_percent()[2],
        "top_over_total_percent": round((db_mod.get_max_qantity_name_percent()[2])/ (db_mod.get_max_qantity_name_percent()[1])  * 100,2),     
        "top_5_antidepressant_data": generate_top_5_antidepressants_barchart_data()
    }
      


    # render the HTML page passing in relevant data
    return render_template('dashboard/index.html',dashboard_data=dashboard_data)
    

def generate_data_for_tiles():
    """Generate the data for the four home page tiles."""
    tile_data = {
        "total_items": db_mod.get_total_number_items(),
        "avg_act_cost": db_mod.get_avg_act(),
        "top_px_item": None,
        "num_unique_items": None,
        "distinct_areas": db_mod.get_distinct_areas(),
        "top_pct": db_mod.get_top_pct(),
        "total_spend_drugs": db_mod.get_total_spend_drugs(),
        "unique_items": db_mod.get_unique_items(),
        "total_gp_practice": db_mod.get_total_gp_practice(),
        "top_quant_drug_name":db_mod.get_max_qantity_name_percent()[0],
        "total_quantity": db_mod.get_max_qantity_name_percent()[1],
        "top_drug_amount": db_mod.get_max_qantity_name_percent()[2],
       
    
    }
    return tile_data



def generate_top_px_items_barchart_data():
    """Generate the data needed to populate the number of most prescrbed items per PCT barchart."""
    
    # Create a dataframe to store the database query results
    df = pd.DataFrame({
        "data_values": db_mod.get_prescribed_items_per_pct(),
        "pct_codes": db_mod.get_distinct_pcts()
    })
    # Generate the plot
    fig = px.bar(df, x="pct_codes", y="data_values", 
                 labels={"pct_codes": "PCT code", 
                         "data_values": "Prescribed items (number)"}).update_xaxes(categoryorder="sum descending")

    # Convert the plot for rendering and add any metadata (description/header)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    header="Prescribed items per Primary Care Trust (PCT)"
    description = "Total number (sum) of prescribed items per PCT (Primary Care Trust) by PCT code."
    plot_data = {
        'graphJSON': graphJSON,
        'header': header,
        'description': description
    }
    return plot_data

def generate_top_5_antidepressants_barchart_data():
    """Generate the data needed to populate the top 5 prescribed antidepressants across all PCTs."""

    # Fetch data
    top_names, top_quantities = db_mod.get_top_5_antidepressants()

    # Debugging: Print the data to check for errors
    print("Names:", top_names)
    print("Quantities:", top_quantities)

    # Create DataFrame
    df = pd.DataFrame({
        "chart_names": top_names,
        "chart_quantities": top_quantities
    })

    # Sort data manually in descending order
    df = df.sort_values(by="chart_quantities", ascending=False)

    # Generate the plot
    fig = px.bar(df, x="chart_names", y="chart_quantities",
                 labels={"chart_names": "Medication", "chart_quantities": "Quantity"})

    fig.update_xaxes(categoryorder="total descending")  # Ensure correct ordering

    # Convert the plot to JSON
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return {
        'graphJSON': graphJSON,
        'header': "Top 5 Prescribed Antidepressants",
        'description': "Top 5 prescribed antidepressants across all PCTs with their quantities."
    }


