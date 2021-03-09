
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output


#-----------------------------------------------------------------------------------------------------------------------
#################################################### Data ##############################################################

# Read the data from the csv:
df_airplanes = pd.read_csv("Data/airplanes.csv",
                           sep = ";")

# Data to show on hovers:
custom_hovertemplate = ("<b>%{customdata[0]}</b><br><br>" +
                        "<b>Thrust (kN) = </b>%{customdata[1]}<br>" +
                        "<b>Max Takeoff Mass (kg) = </b>%{customdata[2]}<br>" +
                        "<b>Speed (km/h) = </b>%{customdata[3]}<br>" +
                        "<b>Range (km) = </b>%{customdata[4]}<br>" +
                        "<b>Max Altitude (m) = </b>%{customdata[5]}<br>" +
                        "<b>Length (m) = </b>%{customdata[6]:.2f}<br>" +
                        "<b>Height (m) = </b>%{customdata[7]:.2f}<br>" +
                        "<b>Wing Span (m) = </b>%{customdata[8]:.2f}<br>" +
                        "<b>Country = </b>%{customdata[9]}<br>" +
                        "<b>Engine Mount = </b>%{customdata[10]}<br>" +
                        "<b>Engine Type = </b>%{customdata[11]}<br>" +
                        "<b>Wing configuration = </b>%{customdata[12]}<br>" +
                        "<b>Main Operator = </b>%{customdata[13]}")


#-----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ###########################################################

app = dash.Dash(name = __name__,
                external_stylesheets = ["assets/bootstrap.css"])
server = app.server

#-----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ###########################################################

### Callbacks

# # Plot 1:
# @app.callback(
#     Output(component_id = "plot_1", component_property = "figure"),
#     [Input(component_id = "plot_1_scale", component_property = "value")]
# )
# def update_plot_1():
#     plot_1 = px.scatter(
#         data_frame = df_airplanes,
#         x = "thrust_kN",
#         y = "speed_kmh",
#         color = "engine_type",
#         size = "max_takeoff_mass_kg",
#         custom_data = list(df_airplanes.columns),
#         template = "plotly_dark",
#         labels = {"thrust_kN": "<b style = 'font-size: 14px;'>Thrust (kN)</b>",
#                   "speed_kmh": "<b style = 'font-size: 14px;'>Speed (km/h)</b>",
#                   "engine_type": "<b style = 'font-size: 14px;'>Engine Type:</b> <br>"}
#     )
#     plot_1.update_traces(
#         hovertemplate = custom_hovertemplate
#     )
#     plot_1.show()
#     
#     return (plot_1)



#-----------------------------------------------------------------------------------------------------------------------
################################################## Frontend ############################################################

# Exploratory Data Analysis:
tab_explo_data_analysis = html.Div(
    [
        # Cards:
        html.Br(),
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H3(className = "card-title",
                                        children = "Fastest"),
                                html.Br(),
                                html.H3(className = "card-subtitle",
                                        children = "F-15")
                            ]
                        ),
                        className = "card_top_airplane",
                        color = "primary",
                        inverse = False
                    ),
                    width = 3,
                    className = "col-card"
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H3(className = "card-title",
                                        children = "Heaviest"),
                                html.Br(),
                                html.H3(className = "card-subtitle",
                                        children = "An-225")
                            ]
                        ),
                        className = "card_top_airplane",
                        color = "primary",
                        inverse = False
                    ),
                    width = 3,
                    className = "col-card"
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H3(className = "card-title",
                                        children = "Longest"),
                                html.Br(),
                                html.H3(className = "card-subtitle",
                                        children = "An-225")
                            ]
                        ),
                        className = "card_top_airplane",
                        color = "primary",
                        inverse = False
                    ),
                    width = 3,
                    className = "col-card"
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(
                            [
                                html.H3(className = "card-title",
                                        children = "Farthest"),
                                html.Br(),
                                html.H3(className = "card-subtitle",
                                        children = "Global Express")
                            ]
                        ),
                        className = "card_top_airplane",
                        color = "primary",
                        inverse = False
                    ),
                    width = 3,
                    className = "col-card"
                )
            ]
        ),
        html.Br(),

        # Scatter plot:
        dbc.Row(
            [
                "scatter plot"
            ]
        ),
        
        # Density and Pie plots:
        dbc.Row(
            [
                "dens and pie"
            ]
        ),
        
        # Parallel sets:
        dbc.Row(
            [
                "parallel"
            ]
        )

    ]
)

# Table:
tab_table = html.Div(
    [
        dbc.Row(
            [
                "table"
            ]
        )
    ]
)

# ML Models:
tab_ml_models = html.Div(
    [
        # Civil/Military Classification with Logit Reg:
        dbc.Row(
            [
                "logit reg"
            ]
        ),
        
        # k-Means Clustering:
        dbc.Row(
            [
                "k-means"
            ]
        )
    ]
)

# Layout:
app.layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.H2("Trunfo Airplanes Dashboard",
                style = {"text-align": "center"}),
        html.Br(),
        html.Br(),
        dbc.Tabs(
            [
                dbc.Tab(
                    label = "Eploratory Analysis",
                    children = tab_explo_data_analysis
                ),
                dbc.Tab(
                    label = "Data",
                    children = tab_table
                ),
                dbc.Tab(
                    label = "Machine Learning Models",
                    children = tab_ml_models
                )
            ]
        )
    ],
    className = "main-div"
)


#-----------------------------------------------------------------------------------------------------------------------
############################################## Run the dashboard #######################################################

run_vers = "dev"
# run_vers = "production"

if run_vers == "dev":
    app.run_server(debug = True)
if run_vers == "production":
    if __name__ == "__main__":
        app.run_server(debug = True)

