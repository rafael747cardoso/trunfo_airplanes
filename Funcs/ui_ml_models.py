
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_ml_models(plot_logit_fit_proj,
                  plot_logit_pdf_pop,
                  plot_logit_confusion,
                  plot_logit_roc
                  ):
    """
    Makes the UI of the ML Models tab.
    :param plot_logit_fit_proj:
    :param plot_logit_pdf_pop:
    :param plot_logit_confusion:
    :param plot_logit_roc:
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
                                                                                figure = plot_logit_fit_proj
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
                                                                                figure = plot_logit_pdf_pop
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
                                            dbc.Row(
                                                [
                                                    dbc.Col(
                                                        [
                                                            dbc.Card(
                                                                [
                                                                    dbc.Col(
                                                                        [
                                                                            dcc.Graph(
                                                                                figure = plot_logit_confusion
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
                                                                                figure = plot_logit_roc
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

