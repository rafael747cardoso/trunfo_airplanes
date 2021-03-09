
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from Funcs.ui_card import card

def tab_explo_data_analysis(fastest,
                            heaviest,
                            longest,
                            most_potent                            
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
    
    return(tab)

