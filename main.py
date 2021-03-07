
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pymysql



#-----------------------------------------------------------------------------------------------------------------------
#################################################### Data ##############################################################

# Pull the tablea from the database in MySQL:
db_conn = pymysql.connect(
    host = "localhost",
    user = "root", 
    password = "",
    database = "super_trunfo"
)
cursor = db_conn.cursor()
cursor.execute("SELECT * FROM airplanes;")
airplanes_rows = cursor.fetchall()
num_fields = len(cursor.description)
airplanes_header = [i[0] for i in cursor.description]
db_conn.close()
df_airplanes = pd.DataFrame(list(airplanes_rows))
df_airplanes = df_airplanes.rename(columns = dict([(i, airplanes_header[i]) for i in range(num_fields)]))


#-----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ###########################################################

app = dash.Dash(name = __name__,
                external_stylesheets = ["assets/bootstrap.css"])
server = app.server

#-----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ###########################################################

### Elements that wont need user inputs

# Plot 1:
def update_plot_1():
    plot_1 = px.scatter(
        data_frame = df_airplanes,
        x = "thrust_kN",
        y = "speed_kmh",
        color = "engine_mount",
        template = "plotly_dark",
        labels = {"thrust_kN": "Thrust (kN)",
                  "speed_kmh": "Speed (km/h)"}
    )
    return(plot_1)

### Callbacks

# Plot 2:
@app.callback(
    Output(component_id = "plot_2", component_property = "figure"),
    [Input(component_id = "plot_2_scale", component_property = "value")]
)
def update_plot_2(plot_2_scale):
    plot_2 = px.scatter(
        data_frame = df_airplanes,
        x = "max_takeoff_mass_kg",
        y = "length_m",
        color = "wing_config",
        template = "plotly_dark",
        log_y = plot_2_scale,
        labels = {"max_takeoff_mass_kg": "Maximum Takeoff Mass (kg)",
                  "length_m": "Length (m)"}
    )
    return(plot_2)

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
    dcc.Graph(id = "plot_2",
              figure = {}),
    html.Br()
])


# Layout:
app.layout = html.Div(
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

