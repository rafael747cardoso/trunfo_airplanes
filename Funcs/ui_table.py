
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8],
                   "cat": ['falcon', 'dog', 'spider', 'fish']})

def tab_table(vars_poss_num
              ):
    """
    Makes the UI of the Table tab.
    :param vars_poss_num:
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
                                    
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    dbc.Select(
                                                        id = "table_filter_var_name",
                                                        options = vars_poss_num,
                                                        value = vars_poss_num[0]["value"]
                                                    )
                                                ],
                                                width = 4
                                            )
                                        ]
                                    ),
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        id = "div_table",
                                                        children = ""
                                                    )
                                                ],
                                                width = 12
                                            )
                                        ]
                                    )
                                    # dbc.Table.from_dataframe(
                                    #     df = df_table,
                                    #     striped = True, 
                                    #     bordered = True,
                                    #     hover = True
                                    # )
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

