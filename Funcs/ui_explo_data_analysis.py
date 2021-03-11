
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from Funcs.ui_card import card

def tab_explo_data_analysis(fastest,
                            heaviest,
                            longest,
                            most_potent,
                            vars_poss_num,
                            vars_poss_cat,
                            vars_poss_dens_cat,
                            funcs_pie_poss):
    """
    Makes the UI of the Exploratory Data Analysis tab.
    :param fastest: 
    :param heaviest: 
    :param longest: 
    :param most_potent: 
    :param vars_poss_num:
    :param vars_poss_cat:
    :param vars_poss_dens_cat:
    :param funcs_pie_poss:
    :return: 
    """
    
    tab = html.Div(
        [
            # Cards:
            html.Br(),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        card(category = "Fastest",
                             plane = fastest,
                             card_id = "fastest-card"),
                        width = 3,
                        className = "col-card"
                    ),
                    dbc.Col(
                        card(category = "Heaviest",
                             plane = heaviest,
                             card_id = "heaviest-card"),
                        width = 3,
                        className = "col-card"
                    ),
                    dbc.Col(
                        card(category = "Longest",
                             plane = longest,
                             card_id = "longest-card"),
                        width = 3,
                        className = "col-card"
                    ),
                    dbc.Col(
                        card(category = "Most Potent",
                             plane = most_potent,
                             card_id = "most_potent-card"),
                        width = 3,
                        className = "col-card"
                    )
                ]
            ),
            html.Br(),
            html.Br(),

            # Scatter plot:
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    # Selects:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H5("X axis",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "x_scatter_eda",
                                                        options = vars_poss_num,
                                                        value = vars_poss_num[0]["value"]
                                                    )
                                                ],
                                                width = 3
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5("Y axis",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "y_scatter_eda",
                                                        options = vars_poss_num,
                                                        value = vars_poss_num[1]["value"]
                                                    )
                                                ],
                                                width = 3
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5("Size",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "size_scatter_eda",
                                                        options = vars_poss_num,
                                                        value = vars_poss_num[2]["value"]
                                                    )
                                                ],
                                                width = 3
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5("Color",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "color_scatter_eda",
                                                        options = vars_poss_cat,
                                                        value = vars_poss_cat[0]["value"]
                                                    )
                                                ],
                                                width = 3
                                            )
                                        ]
                                    ),
    
                                    # Plot:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(id = "plot_scatter_eda",
                                                              figure = {"layout": {"height": 650}})
                                                ],
                                                width = 12
                                            )
                                        ]
                                    )
    
                                ],
                                className = "plot-card",
                                inverse = True
                            )
                        ],
                        width = 12
                    )
                ]
            ),
            html.Br(),
    
            # Density:
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    # Selects:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H5("X axis",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "x_density_eda",
                                                        options = vars_poss_num,
                                                        value = vars_poss_num[0]["value"]
                                                    )
                                                ],
                                                width = 6
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5("Color",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "color_density_eda",
                                                        options = vars_poss_dens_cat,
                                                        value = vars_poss_dens_cat[0]["value"]
                                                    )
                                                ],
                                                width = 6
                                            )
                                        ]
                                    ),
                                    
                                    # Plot:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(
                                                        id = "plot_density_eda",
                                                        figure = {"layout": {"height": 600}}
                                                    )
                                                ],
                                                width = 12
                                            )
                                        ]
                                    )
                                ],
                                className = "plot-card",
                                inverse = True
                            )
                        ],
                        width = 12
                    )
                ]
            ),
            html.Br(),
            
            # Pies:
            dbc.Row(
                [
                    # Pie Count:
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    # Selects:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H5("Category",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "cat_pie_count_eda",
                                                        options = vars_poss_cat[1:],
                                                        value = vars_poss_cat[1]["value"]
                                                    )
                                                ],
                                                width = 12
                                            )
                                        ]
                                    ),
                                    
                                    # Plot:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(id = "plot_pie_count_eda",
                                                              figure = {"layout": {"height": 600}})
                                                ],
                                                width = 12
                                            )
                                        ]
                                    )
                                ],
                                className = "plot-card",
                                inverse = True
                            )
                        ],
                        width = 6
                    ),
                    
                    # Pie Func:
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    # Selects:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H5("Value",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "x_pie_func_eda",
                                                        options = vars_poss_num,
                                                        value = vars_poss_num[0]["value"]
                                                    )
                                                ],
                                                width = 4
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5("Function",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "function_pie_func_eda",
                                                        options = funcs_pie_poss,
                                                        value = funcs_pie_poss[0]["value"]
                                                    )
                                                ],
                                                width = 4
                                            ),
                                            dbc.Col(
                                                [
                                                    html.H5("Category",
                                                            className = "selectinput-label"),
                                                    dbc.Select(
                                                        id = "cat_pie_func_eda",
                                                        options = vars_poss_cat[1:],
                                                        value = vars_poss_cat[1]["value"]
                                                    )
                                                ],
                                                width = 4
                                            )
                                        ]
                                    ),
                                    # Plot:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(id = "plot_pie_func_eda",
                                                              figure = {"layout": {"height": 600}})
                                                ],
                                                width = 12
                                            )
                                        ]
                                    )
                                ],
                                className = "plot-card",
                                inverse = True
                            )
                        ],
                        width = 6
                    )
                ]
            ),
            html.Br(),

            # Parallel sets:
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    # Selects:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.H5("Dimnesions",
                                                            className = "selectinput-label"),
                                                    dcc.Dropdown(
                                                        id = "dimensions_parallel_sets_eda",
                                                        options = vars_poss_cat[1:],
                                                        value = [vars_poss_cat[i]["value"] for i in range(2, 5)],
                                                        multi = True
                                                    )
                                                ],
                                                width = 12
                                            )
                                        ]
                                    ),
                                    # Plot:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dcc.Graph(
                                                        id = "plot_parallel_sets_eda",
                                                        figure = {"layout": {"height": 600}}
                                                    )
                                                ],
                                                width = 12
                                            )
                                        ]
                                    )
                                ],
                                className = "plot-card",
                                inverse = True
                            )
                        ],
                        width = 12
                    )
                ]
            ),
            html.Br()
    
        ]
    )
    
    return(tab)

