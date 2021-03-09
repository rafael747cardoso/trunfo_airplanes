
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from Funcs.ui_explo_data_analysis import tab_explo_data_analysis
from Funcs.ui_table import tab_table
from Funcs.ui_ml_models import tab_ml_models


#-----------------------------------------------------------------------------------------------------------------------
#################################################### Data ##############################################################

# Read the data from the csv:
df_airplanes = pd.read_csv("Data/airplanes.csv",
                           sep = ",")

# Data to show on hovers:
customdata = list(df_airplanes.columns)
custom_hovertemplate = ("<b>%{customdata[0]} %{customdata[1]}</b><br><br>" +
                        "<b>Thrust (kN) = </b>%{customdata[2]}<br>" +
                        "<b>Max Takeoff Mass (kg) = </b>%{customdata[3]}<br>" +
                        "<b>Speed (km/h) = </b>%{customdata[4]}<br>" +
                        "<b>Range (km) = </b>%{customdata[5]}<br>" +
                        "<b>Max Altitude (m) = </b>%{customdata[6]}<br>" +
                        "<b>Length (m) = </b>%{customdata[7]:.2f}<br>" +
                        "<b>Height (m) = </b>%{customdata[8]:.2f}<br>" +
                        "<b>Wing Span (m) = </b>%{customdata[9]:.2f}<br>" +
                        "<b>Country = </b>%{customdata[10]}<br>" +
                        "<b>Engine Mount = </b>%{customdata[11]}<br>" +
                        "<b>Engine Type = </b>%{customdata[12]}<br>" +
                        "<b>Wing configuration = </b>%{customdata[13]}<br>" +
                        "<b>Main Operator = </b>%{customdata[14]}")

# Top airplanes for the cards
fastest = np.array(df_airplanes.loc[np.where(df_airplanes["speed_kmh"] == max(df_airplanes["speed_kmh"]))].iloc[0])[[0, 1]]
heaviest = np.array(df_airplanes.loc[np.where(df_airplanes["max_takeoff_mass_kg"] == max(df_airplanes["max_takeoff_mass_kg"]))].iloc[0])[[0, 1]]
longest = np.array(df_airplanes.loc[np.where(df_airplanes["length_m"] == max(df_airplanes["length_m"]))].iloc[0])[[0, 1]]
most_potent = np.array(df_airplanes.loc[np.where(df_airplanes["thrust_kN"] == max(df_airplanes["thrust_kN"]))].iloc[0])[[0, 1]]


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
                    children = tab_explo_data_analysis(fastest = fastest,
                                                       heaviest = heaviest,
                                                       longest = longest,
                                                       most_potent = most_potent)
                ),
                dbc.Tab(
                    label = "Table",
                    children = tab_table()
                ),
                dbc.Tab(
                    label = "Machine Learning Models",
                    children = tab_ml_models()
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

