
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def card(category,
         plane,
         card_id):    
    """
    Makes the Top Airplanes cards.
    :param plane: 
    :param category: 
    :param card_id: 
    :return: 
    """
    
    card = dbc.Card(
        dbc.CardBody(
            [
                html.H3(category,
                        className = "topairplane-card-title"),
                html.H3(plane[0],
                        className = "topairplane-card-subtitle"),
                html.H3(plane[1],
                        className = "topairplane-card-subtitle")
            ]
        ),
        className = "topairplane-card",
        id = card_id,
        inverse = True
    )
    
    return(card)


