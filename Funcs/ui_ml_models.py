
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_ml_models(logit_predictors_poss):
    """
    Makes the UI of the ML Models tab.
    :param logit_predictors_poss:
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
                                                                className = "title-model"),
                                                        html.Br(),
                                                        html.Br(),
                                                        html.H4("Proportional size of the test dataset:",
                                                                className = "title-slider"),
                                                        html.Br(),
                                                        dcc.Slider(
                                                            id = "test_prop_logit",
                                                            min = 0.1,
                                                            max = 0.9,
                                                            step = 0.01,
                                                            value = 0.3,
                                                            marks = dict([(i, str(int(i*100))) for i in np.arange(0.1, 1, 0.1)])
                                                        ),
                                                        html.Br(),
                                                        html.Div(id = "test_prop_logit_chosen")
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
                                                                            html.H4("Logit Function Projections",
                                                                                    className = "table-card"),
                                                                            dbc.Col(
                                                                                [
                                                                                    dbc.Select(
                                                                                        id = "predictor_proj_logit",
                                                                                        options = logit_predictors_poss,
                                                                                        value = logit_predictors_poss[0]["value"]
                                                                                    )
                                                                                ],
                                                                                width = 6
                                                                            ),
                                                                            dcc.Graph(id = "plot_logit_fit_proj")
                                                                        ],
                                                                        width = 12
                                                                    )
                                                                ],
                                                                className = "plot-model-card",
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
                                                                            html.H4("Probability Distributions of the Populations",
                                                                                    className = "table-card"),
                                                                            dcc.Graph(id = "plot_logit_pdf_pop")
                                                                        ],
                                                                        width = 12
                                                                    )
                                                                ],
                                                                className = "plot-model-card",
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
                                                                            html.H4("Confusion Matrix",
                                                                                    className = "table-card"),
                                                                            dcc.Graph(id = "plot_logit_confusion")
                                                                        ],
                                                                        width = 12
                                                                    )
                                                                ],
                                                                className = "plot-model-card",
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
                                                                            html.H4("ROC Curve",
                                                                                    className = "table-card"),
                                                                            dcc.Graph(id = "plot_logit_roc")
                                                                        ],
                                                                        width = 12
                                                                    )
                                                                ],
                                                                className = "plot-model-card",
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
                                                                            html.H4("Report",
                                                                                    className = "table-card"),
                                                                            dcc.Graph(id = "plot_logit_report")
                                                                        ],
                                                                        width = 12
                                                                    )
                                                                ],
                                                                className = "plot-model-card",
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
            html.Br()
        ]
    )

    return (tab)

