
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import operator
import dash_table
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, roc_auc_score
from sklearn.model_selection import train_test_split


from Funcs.ui_explo_data_analysis import tab_explo_data_analysis
from Funcs.ui_table import tab_table
from Funcs.ui_ml_models import tab_ml_models

pd.set_option("display.width", 1200)
pd.set_option("display.max_columns", 20)


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

# Nice labels:
nice_names = [
    "Manufacturer Name",
    "Model Name",
    "Thrust (kN)",
    "Max Takeoff Mass (kg)",
    "Speed (km/h)",
    "Range (km)",
    "Max Altitude (m)",
    "Lenght (m)",
    "Height (m)",
    "Wingspan (m)",
    "Manufacturer Country",
    "Engine Mount",
    "Engine Type",
    "Wing Config",
    "Main Operator"
]
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
labels_cat = {
    "manufacturer_name": "Manufacturer Name",
    "manufacturer_country": "Manufacturer Country",
    "engine_mount": "Engine Mount",
    "engine_type": "Engine Type",
    "wing_config": "Wing Config",
    "main_operator": "Main Operator"
}

# Possible variables for the selects:
vars_poss_filter_num = [
    {"label": "Variable", "value": "Variable"},
    {"label": "Thrust", "value": "thrust_kN"},
    {"label": "Max Takeoff Mass", "value": "max_takeoff_mass_kg"},
    {"label": "Speed", "value": "speed_kmh"},
    {"label": "Range", "value": "range_km"},
    {"label": "Max Altitude", "value": "max_altitude_m"},
    {"label": "Length", "value": "length_m"},
    {"label": "Height", "value": "height_m"},
    {"label": "Wingspan", "value": "wing_span_m"}
]
vars_poss_num = vars_poss_filter_num[1:]
vars_poss_filter_cat = [
    {"label": "Variable", "value": "Variable"},
    {"label": "Manufacturer Name", "value": "manufacturer_name"},
    {"label": "Manufacturer Country", "value": "manufacturer_country"},
    {"label": "Engine Mount", "value": "engine_mount"},
    {"label": "Engine Type", "value": "engine_type"},
    {"label": "Wing Config", "value": "wing_config"},
    {"label": "Main Operator", "value": "main_operator"}
]
vars_poss_cat = vars_poss_filter_cat[1:]
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
filter_operations_poss = [
    {"label": "Operator", "value": "Operator"},
    {"label": ">=", "value": ">="},
    {"label": ">", "value": ">"},
    {"label": "==", "value": "=="},
    {"label": "<", "value": "<"},
    {"label": "<=", "value": "<="}
]
ops = {
    ">=": operator.ge,
    ">": operator.gt,
    "==": operator.eq,
    "<": operator.lt,
    "<=": operator.le
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
    df = df_airplanes.copy().groupby(cat_pie_count_eda)[cat_pie_count_eda].count()
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
        df = df_airplanes.copy().groupby(cat_pie_func_eda)[x_pie_func_eda].mean().astype(int)
    if function_pie_func_eda == "sum":
        df = df_airplanes.copy().groupby(cat_pie_func_eda)[x_pie_func_eda].sum().astype(int)
    if function_pie_func_eda == "min":
        df = df_airplanes.copy().groupby(cat_pie_func_eda)[x_pie_func_eda].min().astype(int)
    if function_pie_func_eda == "max":
        df = df_airplanes.copy().groupby(cat_pie_func_eda)[x_pie_func_eda].max().astype(int)
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
@app.callback(
    Output(component_id = "plot_parallel_sets_eda", component_property = "figure"),
    [Input(component_id = "dimensions_parallel_sets_eda", component_property = "value")]
)
def update_plot_parallel_sets_eda(dimensions_parallel_sets_eda):
    vars_cat = []
    for i in range(len(vars_poss_cat)):
        if vars_poss_cat[i]["value"] in dimensions_parallel_sets_eda:
            vars_cat += [vars_poss_cat[i]]
    dimensions_parcat = [go.parcats.Dimension(values = df_airplanes[vars_cat[i]["value"]], 
                                              label = vars_cat[i]["label"]) for i in range(len(vars_cat))]
    plot_parallel_sets_eda = go.Figure(
        data = go.Parcats(
            dimensions = dimensions_parcat,
            line = {"shape": "hspline"}
        )
    )
    plot_parallel_sets_eda.update_layout(
        template = "plotly_dark"
    )   
    return(plot_parallel_sets_eda)

#################### Table

# Update the options for the categorical filter select:
@app.callback(
    Output(component_id = "table_filter_cat_var_value", component_property = "options"),
    [Input(component_id = "table_filter_cat_var_name", component_property = "value")]
)
def update_select_filter_cat(table_filter_cat_var_name):
    opt0 = [{"label": "", "value": ""}]
    if table_filter_cat_var_name in df_airplanes.columns:
        opts = [{"label": l, "value": l} for l in df_airplanes[table_filter_cat_var_name].unique()]
    else:
        opts = [{"label": "", "value": ""}]
    return(opt0 + opts)

# Table with filters:
@app.callback(
    Output(component_id = "div_table", component_property = "children"),
    [Input(component_id = "table_filter_num_var_name", component_property = "value"),
     Input(component_id = "table_filter_num_operation", component_property = "value"),
     Input(component_id = "table_filter_num_var_value", component_property = "value"),
     Input(component_id = "table_filter_cat_var_name", component_property = "value"),
     Input(component_id = "table_filter_cat_var_value", component_property = "value")
     ]
)   
def update_table(table_filter_num_var_name,
                 table_filter_num_operation,
                 table_filter_num_var_value,
                 table_filter_cat_var_name,
                 table_filter_cat_var_value):
    # Filters:
    df = df_airplanes.copy()
    if table_filter_num_var_name != "Variable" and \
       table_filter_num_operation != "Operator":
        op_func = ops[table_filter_num_operation]
        df = df[op_func(df[table_filter_num_var_name], table_filter_num_var_value)]
    if table_filter_cat_var_name != "Variable" and \
       table_filter_cat_var_value != "Levels" and \
       table_filter_cat_var_value != "":
        df = df[df[table_filter_cat_var_name] == table_filter_cat_var_value]
    df.columns = nice_names
    
    # Table:
    table = dash_table.DataTable(
        id = "table_data",
        columns = [{"name": c, "id": c} for c in df.columns],
        data = df.to_dict("records"),
        page_size = 18,
        style_as_list_view = True,
        style_header = {
            "backgroundColor": "rgb(30, 30, 30)"
        },
        style_cell = {
            "backgroundColor": "rgb(50, 50, 50)",
            "color": "white",
            "textAlign": "center"
        },
        style_cell_conditional = [
            {"if": {"column_id": ["Manufacturer Name", 
                                  "Model Name"]},
             "textAlign": "left"}
        ],
        style_table = {
            "overflowX": "auto"
        }        
    )
    return(table)

#################### ML Models

###### Logistic Regression

# Feature selection:
df = df_airplanes.copy()[["main_operator",
                          "thrust_kN",
                          "max_takeoff_mass_kg",
                          "speed_kmh",
                          "range_km",
                          "max_altitude_m",
                          "length_m",
                          "height_m",
                          "wing_span_m",
                          "engine_mount",
                          "engine_type",
                          "wing_config"]]
df["is_military"] = np.where(df["main_operator"] == "Military", 1, 0)
df["engine_mount"].loc[np.where(df["engine_mount"] == "Wings and Tail")] = "WingsTail"
engine_mounts = pd.get_dummies(data = df["engine_mount"],
                               prefix = "engine_mount")
engine_types = pd.get_dummies(data = df["engine_type"],
                              prefix = "engine_type")
wing_configs = pd.get_dummies(data = df["wing_config"],
                              prefix = "wing_config")
df = df.join([engine_mounts, engine_types, wing_configs])
df.drop(["main_operator",
         "engine_mount",
         "engine_type",
         "wing_config"],
        axis = 1,
        inplace = True)
predictors = list(df.columns)

# Model:
x = df[predictors].values.reshape(-1, len(predictors))
y = df["is_military"].values
x_train, x_test, y_train, y_test = train_test_split(x, 
                                                    y, 
                                                    test_size = 0.35, 
                                                    random_state = 42)
model = LogisticRegression(
    penalty = "l2",
    tol = 1E-4,
    C = 1,
    fit_intercept = True,
    random_state = 0,
    solver = "liblinear"
).fit(x_train, y_train)

### Evaluation

# Plot the projection of the fitted curve over the predictors:
b0 = model.intercept_[0]
bs = [model.coef_[0][i] for i in range(len(predictors))]
df_fit = pd.DataFrame()
for i in range(len(predictors)):
    df_fit[predictors[i]] = np.linspace(min(x_test[:, i]), max(x_test[:, i]), x_test.shape[0])
df_fit["f"] = b0 + sum([bs[i]*df_fit[predictors[i]] for i in range(len(predictors))])
df_fit["p"] = 1/(1 + np.exp(-(df_fit["f"])))
p_i = 0
plot_logit_fit_proj = px.line(
    x = df_fit[predictors[p_i]],
    y = df_fit["p"],
    template = "plotly_dark"
).add_scatter(
    x = df[predictors[p_i]],
    y = df["is_military"],
    mode = "markers"
)

# Plot of probability distributions of the populations:
threshold = 0.5
prob_distr_TN = model.predict_proba(x_test)[:, 1][np.where(y_test == 0)]
prob_distr_TN = prob_distr_TN[prob_distr_TN < threshold]/sum(model.predict_proba(x_test)[:, 1])
prob_distr_TP = model.predict_proba(x_test)[:, 1][np.where(y_test == 1)]
prob_distr_TP = prob_distr_TP[prob_distr_TP >= threshold]/sum(model.predict_proba(x_test)[:, 1])
prob_distr_FN = model.predict_proba(x_test)[:, 1][np.where(y_test == 1)]
prob_distr_FN = prob_distr_FN[prob_distr_FN < threshold]/sum(model.predict_proba(x_test)[:, 1])
prob_distr_FP = model.predict_proba(x_test)[:, 1][np.where(y_test == 0)]
prob_distr_FP = prob_distr_FP[prob_distr_FP >= threshold]/sum(model.predict_proba(x_test)[:, 1])
hist_vars = [prob_distr_TN,
             prob_distr_TP,
             prob_distr_FN,
             prob_distr_FP]
hist_data = [i for i in hist_vars if len(i) > 0]
hist_labels = ["True Negatives", 
               "True Positives", 
               "False Negatives",
               "False Positives"]
group_labels = [hist_labels[i] for i in range(len(hist_labels)) if len(hist_vars[i]) > 0]
plot_logit_pdf_pop = ff.create_distplot(
    hist_data = hist_data, 
    group_labels = group_labels, 
    bin_size = 0.0005,
    curve_type = "normal",
    histnorm = "probability",
    colors = ["#c70039", "#2a7b9b", "#ff8d1a", "#57c785"]
).update_layout(
    template = "plotly_dark"
)

# Confusion matrix:
cm = pd.DataFrame(
    data = confusion_matrix(y_true = y_test,
                            y_pred = model.predict(x_test)),
    index = ["Civil", "Military"],
    columns = ["Civil", "Military"]                  
)
plot_logit_confusion = px.imshow(
    img = cm,
    labels = {
        "x": "Predicted",
        "y": "Actual",
        "color": "Frequency"
    },
    template = "plotly_dark"
)

# ROC curve:
y_prob = model.predict_proba(x_test)[:, 1]
fpr, tpr, thresholds = roc_curve(y_true = y_test, 
                                 y_score = y_prob)
auc = roc_auc_score(y_true = y_test,
                    y_score = y_prob)
df_roc = pd.DataFrame({"fpr": fpr.round(3),
                       "tpr": tpr.round(3),
                       "thresholds": thresholds.round(3)})
plot_logit_roc = px.area(
    data_frame = df_roc,
    x = "fpr", 
    y = "tpr",
    hover_data = ["thresholds"],
    title = f"ROC Curve (AUC={auc:.3f})",
    labels = {
        "fpr": "False Positive Rate",
        "tpr": "True Positive Rate",
        "thresholds": "Threshold"
    },
    template = "plotly_dark"
).add_shape(
    type = "line", 
    line = {"dash": "dash"},
    x0 = 0,
    x1 = 1,
    y0 = 0,
    y1 = 1
)

# Report:
print("Accuracy: " + str(model.score(x_test, y_test).round(2)))
print(classification_report(y_true = y_test,
                            y_pred = model.predict(x_test),
                            output_dict = False))












###### k-Means Clustering









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
                    label = "Exploratory Data Analysis",
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
                    children = tab_table(vars_poss_filter_num = vars_poss_filter_num,
                                         vars_poss_filter_cat = vars_poss_filter_cat,
                                         filter_operations_poss = filter_operations_poss)
                ),
                dbc.Tab(
                    label = "Machine Learning Models",
                    children = tab_ml_models(plot_logit_fit_proj = plot_logit_fit_proj,
                                             plot_logit_pdf_pop = plot_logit_pdf_pop,
                                             plot_logit_confusion = plot_logit_confusion,
                                             plot_logit_roc = plot_logit_roc)
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

