
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_ml_models():
    """
    Makes the UI of the ML Models tab.
    :return: 
    """

    tab = html.Div(
        [
            # Civil/Military Classification with Logit Reg:
            dbc.Row(
                [
                    "logit reg"
                ]
            ),

            # k-Means Clustering:
            dbc.Row(
                [
                    "k-means"
                ]
            )
        ]
    )

    return (tab)

