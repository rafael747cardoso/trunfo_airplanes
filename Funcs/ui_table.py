
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_table(df_table):
    """
    Makes the UI of the Table tab.
    :return: 
    """

    tab = html.Div(
        [
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.Table.from_dataframe(
                                        df = df_table,
                                        striped = True, 
                                        bordered = True,
                                        hover = True
                                    )
                                ],
                                className = "table-card",
                                inverse = True
                            )
                        ],
                        width = 12
                    )
                ]
            )
        ]
    )

    return (tab)

