
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_table(vars_poss_num,
              filter_operations_poss
              ):
    """
    Makes the UI of the Table tab.
    :param vars_poss_num:
    :param filter_operations_poss:
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
                                    # Filters:
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
                                            ),
                                            dbc.Col(
                                                [
                                                    dbc.Select(
                                                        id = "table_filter_operation",
                                                        options = filter_operations_poss,
                                                        value = filter_operations_poss[0]["value"]
                                                    )
                                                ],
                                                width = 2
                                            ),
                                            dbc.Col(
                                                [
                                                    dbc.Input(
                                                        id = "table_filter_var_value",
                                                        type = "number",
                                                        value = 0
                                                    )
                                                ],
                                                width = 3
                                            ),
                                            dbc.Col(
                                                [
                                                    # dbc.Button(
                                                    #     id = "button_filters",
                                                    #     children = "No Filters",
                                                    #     className = "mr-1",
                                                    #     color = "info",
                                                    #     block = True
                                                    # )
                                                ],
                                                width = {"size": 2, "offset": 1}
                                            )
                                        ]
                                    ),
                                    
                                    # Table:
                                    dbc.Row(
                                        [
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        id = "div_table",
                                                        children = "",
                                                        className = "table-data"
                                                    )
                                                ],
                                                width = 12
                                            )
                                        ]
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

