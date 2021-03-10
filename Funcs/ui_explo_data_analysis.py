
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
                            vars_poss_dens_cat
                            ):
    """
    Makes the UI of the Exploratory Data Analysis tab.
    :param fastest: 
    :param heaviest: 
    :param longest: 
    :param most_potent: 
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
            
            # Pies:
            dbc.Row(
                [
                    "pie 1 pie 2"
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
    
    return(tab)

