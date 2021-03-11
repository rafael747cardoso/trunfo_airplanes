
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

# Top airplanes for the cards
fastest = np.array(df_airplanes.loc[np.where(df_airplanes["speed_kmh"] == max(df_airplanes["speed_kmh"]))].iloc[0])[[0, 1]]
heaviest = np.array(df_airplanes.loc[np.where(df_airplanes["max_takeoff_mass_kg"] == max(df_airplanes["max_takeoff_mass_kg"]))].iloc[0])[[0, 1]]
longest = np.array(df_airplanes.loc[np.where(df_airplanes["length_m"] == max(df_airplanes["length_m"]))].iloc[0])[[0, 1]]
most_potent = np.array(df_airplanes.loc[np.where(df_airplanes["thrust_kN"] == max(df_airplanes["thrust_kN"]))].iloc[0])[[0, 1]]

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
                        "<b>Manufacturer Country = </b>%{customdata[10]}<br>" +
                        "<b>Engine Mount = </b>%{customdata[11]}<br>" +
                        "<b>Engine Type = </b>%{customdata[12]}<br>" +
                        "<b>Wing configuration = </b>%{customdata[13]}<br>" +
                        "<b>Main Operator = </b>%{customdata[14]}")

# Possible variables for the selects:
vars_poss_num = [
    {"label": "Thrust", "value": "thrust_kN"},
    {"label": "Max Takeoff Mass", "value": "max_takeoff_mass_kg"},
    {"label": "Speed", "value": "speed_kmh"},
    {"label": "Range", "value": "range_km"},
    {"label": "Max Altitude", "value": "max_altitude_m"},
    {"label": "Length", "value": "length_m"},
    {"label": "Height", "value": "height_m"},
    {"label": "Wingspan", "value": "wing_span_m"}
]
vars_poss_cat = [
    {"label": "Manufacturer Name", "value": "manufacturer_name"},
    {"label": "Manufacturer Country", "value": "manufacturer_country"},
    {"label": "Engine Mount", "value": "engine_mount"},
    {"label": "Engine Type", "value": "engine_type"},
    {"label": "Wing Config", "value": "wing_config"},
    {"label": "Main Operator", "value": "main_operator"}
]
vars_poss_dens_cat = [
    {"label": "All categories", "value": "all_categories"},
    {"label": "Main Operator", "value": "main_operator"},
    {"label": "Engine Mount", "value": "engine_mount"},
    {"label": "Engine Type", "value": "engine_type"},
    {"label": "Wing Config", "value": "wing_config"}
]
funcs_pie_poss = [
    {"label": "Mean", "value": "mean"},
    {"label": "Sum", "value": "sum"},
    {"label": "Minimum", "value": "min"},
    {"label": "Maximum", "value": "max"},
]

# Labels for the plots axis:
axis_plots = {
    "thrust_kN": "<b style = 'font-size: 14px;'> Thrust (kN)</b>",
    "max_takeoff_mass_kg": "<b style = 'font-size: 14px;'> Max Takeoff Mass (kg)</b>",
    "speed_kmh": "<b style = 'font-size: 14px;'> Speed (km/h)</b>",
    "range_km": "<b style = 'font-size: 14px;'> Range (km)</b>",
    "max_altitude_m": "<b style = 'font-size: 14px;'> Max Altitude (m)</b>",
    "length_m": "<b style = 'font-size: 14px;'> Length (m)</b>",
    "height_m": "<b style = 'font-size: 14px;'> Height (m)</b>",
    "wing_span_m": "<b style = 'font-size: 14px;'> Wingspan (m)</b>",
    "manufacturer_name": "<b style = 'font-size: 14px;'> Manufacturer Name</b>",
    "manufacturer_country": "<b style = 'font-size: 14px;'> Manufacturer Country</b>",
    "engine_mount": "<b style = 'font-size: 14px;'> Engine Mount</b>",
    "engine_type": "<b style = 'font-size: 14px;'> Engine Type</b>",
    "wing_config": "<b style = 'font-size: 14px;'> Wing Config</b>",
    "main_operator": "<b style = 'font-size: 14px;'> Main Operator</b>"
}




#-----------------------------------------------------------------------------------------------------------------------
################################################# Initialize ###########################################################

app = dash.Dash(name = __name__,
                external_stylesheets = ["assets/bootstrap.css"])
server = app.server

#-----------------------------------------------------------------------------------------------------------------------
#################################################### Backend ###########################################################

#################### Exploratory Data Analysis

# Scatter plot:
@app.callback(
    Output(component_id = "plot_scatter_eda", component_property = "figure"),
    [Input(component_id = "x_scatter_eda", component_property = "value"),
     Input(component_id = "y_scatter_eda", component_property = "value"),
     Input(component_id = "size_scatter_eda", component_property = "value"),
     Input(component_id = "color_scatter_eda", component_property = "value")]
)
def update_plot_scatter_eda(x_scatter_eda,
                            y_scatter_eda,
                            size_scatter_eda,
                            color_scatter_eda):
    plot_scatter_eda = px.scatter(
        data_frame = df_airplanes,
        x = x_scatter_eda,
        y = y_scatter_eda,
        size = size_scatter_eda,
        color = color_scatter_eda,
        custom_data = list(df_airplanes.columns),
        template = "plotly_dark",
        labels = axis_plots
    )
    plot_scatter_eda.update_traces(
        hovertemplate = custom_hovertemplate
    )
    return(plot_scatter_eda)

# Density plot:
@app.callback(
    Output(component_id = "plot_density_eda", component_property = "figure"),
    [Input(component_id = "x_density_eda", component_property = "value"),
     Input(component_id = "color_density_eda", component_property = "value")]
)
def update_plot_density_eda(x_density_eda,
                            color_density_eda):
    if color_density_eda == "all_categories":
        plot_density_eda = px.histogram(
            data_frame = df_airplanes,
            x = x_density_eda,
            marginal = "violin",
            nbins = 100,
            template = "plotly_dark",
            labels = axis_plots
        )
    else:        
        plot_density_eda = px.histogram(
            data_frame = df_airplanes,
            x = x_density_eda,
            color = color_density_eda,
            marginal = "violin",
            nbins = 100,
            template = "plotly_dark",
            labels = axis_plots
        )
    return(plot_density_eda)

# Pie Count:
@app.callback(
    Output(component_id = "plot_pie_count_eda", component_property = "figure"),
    [Input(component_id = "cat_pie_count_eda", component_property = "value")]
)
def update_plot_pie_count_eda(cat_pie_count_eda):
    df = df_airplanes.groupby(cat_pie_count_eda)[cat_pie_count_eda].count()
    levels_names = list(df.index)
    levels_counts = list(df)    
    plot_pie_count_eda = go.Figure(
        data = go.Pie(
            labels = levels_names,
            values = levels_counts
        )
    )
    plot_pie_count_eda.update_layout(
        autosize = True,
        template = "plotly_dark"
    )
    return(plot_pie_count_eda)

# Pie Func:
@app.callback(
    Output(component_id = "plot_pie_func_eda", component_property = "figure"),
    [Input(component_id = "x_pie_func_eda", component_property = "value"),
     Input(component_id = "function_pie_func_eda", component_property = "value"),
     Input(component_id = "cat_pie_func_eda", component_property = "value")]
)
def update_plot_pie_count_eda(x_pie_func_eda,
                              function_pie_func_eda,
                              cat_pie_func_eda):
    if function_pie_func_eda == "mean":
        df = df_airplanes.groupby(cat_pie_func_eda)[x_pie_func_eda].mean().astype(int)
    if function_pie_func_eda == "sum":
        df = df_airplanes.groupby(cat_pie_func_eda)[x_pie_func_eda].sum().astype(int)
    if function_pie_func_eda == "min":
        df = df_airplanes.groupby(cat_pie_func_eda)[x_pie_func_eda].min().astype(int)
    if function_pie_func_eda == "max":
        df = df_airplanes.groupby(cat_pie_func_eda)[x_pie_func_eda].max().astype(int)
    levels_names = list(df.index)
    levels_counts = list(df)    
    plot_pie_func_eda = go.Figure(
        data = go.Pie(
            labels = levels_names,
            values = levels_counts
        )
    )
    plot_pie_func_eda.update_layout(
        autosize = True,
        template = "plotly_dark"
    )   
    return(plot_pie_func_eda)

# Parallel Sets:









#################### Table


#################### ML Models





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
                    label = "Eploratory Data Analysis",
                    children = tab_explo_data_analysis(fastest = fastest,
                                                       heaviest = heaviest,
                                                       longest = longest,
                                                       most_potent = most_potent,
                                                       vars_poss_num = vars_poss_num,
                                                       vars_poss_cat = vars_poss_cat,
                                                       vars_poss_dens_cat = vars_poss_dens_cat,
                                                       funcs_pie_poss = funcs_pie_poss)
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

