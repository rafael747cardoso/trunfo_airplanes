
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_table():
    """
    Makes the UI of the Table tab.
    :return: 
    """

    tab = html.Div(
        [
            dbc.Row(
                [
                    "table"
                ]
            )
        ]
    )

    return (tab)

