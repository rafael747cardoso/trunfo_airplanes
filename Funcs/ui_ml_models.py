
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_ml_models(plot_logit_1,
                  plot_logit_2
                  ):
    """
    Makes the UI of the ML Models tab.
    :param plot_logit_1:
    :return: 
    """

    tab = html.Div(
        [
            html.Br(),
            html.Br(),
            
            # Civil/Military Classification with Logit Reg:
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dbc.Card(
                                [
                                    dbc.Col(
                                        [
                                            html.Br(),
                                            dbc.Row(
                                                dbc.Col(
                                                    [
                                                        html.H3("Civil/Military Classification with Logistic Regression",
                                                                className = "title-model")
                                                    ],
                                                    width = 12
                                                )
                                            ),
                                            html.Br(),
                                            html.Br(),

                                            # Plots:
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        [
                                                            dbc.Card(
                                                                [
                                                                    dbc.Col(
                                                                        [
                                                                            dcc.Graph(
                                                                                figure = plot_logit_1
                                                                            )
                                                                        ],
                                                                        width = 12
                                                                    )
                                                                ],
                                                                className = "plot-card",
                                                                inverse = True
                                                            )
                                                        ],
                                                        width = 6
                                                    ),
                                                    dbc.Col(
                                                        [
                                                            dbc.Card(
                                                                [
                                                                    dbc.Col(
                                                                        [
                                                                            dcc.Graph(
                                                                                figure = plot_logit_2
                                                                            )
                                                                        ],
                                                                        width = 12
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

                                            # Model Summary:
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        [
                                                            dbc.Card(
                                                                [
                                                                    dbc.Col(
                                                                        [
                                                                            "Model summary"
                                                                        ],
                                                                        width = 12
                                                                    )
                                                                ],
                                                                className = "plot-card",
                                                                inverse = True
                                                            )
                                                        ],
                                                        width = 12
                                                    )
                                                ]
                                            )
                                        ],
                                        width = 12
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
            html.Br(),

            # k-Means Clustering:
            dbc.Row(
                [
                    "k-means"
                ]
            )
        ]
    )

    return (tab)

