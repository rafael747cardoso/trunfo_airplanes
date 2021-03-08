
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

### Without inputs

### With inputs

# Plot 1:
@app.callback(
    Output(component_id = "plot_1", component_property = "figure"),
    [Input(component_id = "plot_1_scale", component_property = "value")]
)
def update_plot_1():
    plot_1 = px.scatter(
        data_frame = df_airplanes,
        x = "thrust_kN",
        y = "speed_kmh",
        color = "engine_type",
        size = "max_takeoff_mass_kg",
        custom_data = list(df_airplanes.columns),
        template = "plotly_dark",
        labels = {"thrust_kN": "<b style = 'font-size: 14px;'>Thrust (kN)</b>",
                  "speed_kmh": "<b style = 'font-size: 14px;'>Speed (km/h)</b>",
                  "engine_type": "<b style = 'font-size: 14px;'>Engine Type:</b> <br>"}
    )
    plot_1.update_traces(
        hovertemplate = custom_hovertemplate
    )
    plot_1.show()
    
    return (plot_1)



#-----------------------------------------------------------------------------------------------------------------------
################################################## Frontend ############################################################

tab_1 = html.Div([
    html.Br(),
    html.H3("Airplanes here",
            style = {"text-align": "center"}),
    html.Br(),
    dcc.Graph(id = "plot_1",
              figure = update_plot_1()),
    html.Br()
])

tab_2 = html.Div([
    html.Br(),
    html.H3("Airplanes here too",
            style = {"text-align": "center"}),
    html.Br(),
    dbc.RadioItems(
        id = "plot_2_scale",
        options =
        [
            {"label": "Linear", 
             "value": False},
            {"label": "Log", 
             "value": True}
        ],
        value = False,
        inline = True,
        style = {"text-align": "center"}
    ),
    html.Br()
])


# Layout:
app.layout = dbc.Container(
    [
        html.Div(
            [
                html.Br(),
                html.H2("Dashboard Airplanes"),
                html.Br(),
                
                dbc.Tabs(
                    [
                        dbc.Tab(children = tab_1,
                                label = "Tab 1"),
                        dbc.Tab(children = tab_2,
                                label = "Tab 2")
                    ]
                )
                
            ]
        )
    ]
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

