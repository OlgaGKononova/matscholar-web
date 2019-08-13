import os
import json
from os import environ

# dash
import dash
import dash_auth
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from flask import send_from_directory
from matscholar.rest import Rester
from matscholar.rest import MatScholarRestError

# apps
from matscholar_web.view import search_view, analysis_view

# callbacks
from matscholar_web.callbacks import search_view_callbacks

"""
APP CONFIG
"""

app = dash.Dash()
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
app.config.suppress_callback_exceptions = True
app.title = "matscholar - rediscover materials"

# Authentication
VALID_USERNAME_PASSWORD_PAIRS = [
    [environ['MATERIALS_SCHOLAR_WEB_USER'], environ['MATERIALS_SCHOLAR_WEB_PASS']]]
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

# loading css files
css_files = ["skeleton.min.css", "matscholar_web.css", ]
stylesheets_links = [
    html.Link(rel='stylesheet', href='/static/css/' + css) for css in css_files]


"""
VIEW
"""
# try:
#     abstract_count = Rester().get_abstract_count()
# except MatScholarRestError:
#     abstract_count = 0


header = html.Div([
    dcc.Location(id="url", refresh=False),
    html.Img(
        src="https://s3.amazonaws.com/matscholar/matscholar_logo.png",
        style={
            'width': '250px',
            "display": "block",
            'max-width': "100%",
            "margin": "5px auto",
        }),
    # html.Label(str(abstract_count)+" Abstracts Analyzed!",style={"textAlign": "center"})
], className="row")

# nav = html.Nav(
#     style={
#         "margin": "3px 1px",
#         "padding": "3px 1px",
#         "textAlign": "center"},
#     children=[
#         dcc.Link("search", href="/search"),
#         html.Span(" | ", style={"color": "whitesmoke"}),
#         #dcc.Link("explore embeddings", href="/explore"),
#         #html.Span(" | ", style={"color": "whitesmoke"}),
#         dcc.Link("materials map", href="/materials_map"),
#         # html.Span(" | ", style={"color": "whitesmoke"}),
#         # dcc.Link("journal suggestion", href="/journal_suggestion"),
#         html.Span(" | ", style={"color": "whitesmoke"}),
#         dcc.Link("summary", href="/summary"),
#         html.Span(" | ", style={"color": "whitesmoke"}),
#         dcc.Link("extract", href="/extract"),
#         html.Span(" | ", style={"color": "whitesmoke"}),
#         dcc.Link("material search", href="/material_search"),
#     ],
#     id="nav_bar")

footer = html.Div(
    [
        html.Span(
            "Copyright © 2018 - "),
        html.A(
            "Materials Scholar Development Team",
            href="https://github.com/materialsintelligence",
            target="_blank")
    ],
    className="row",
    style={
        "color": "grey",
        "textAlign": "center"
    }
)

app.layout = html.Div([
    html.Div(stylesheets_links, style={"display": "none"}),
    header,
    html.Div("", id="app_container"),
    footer],
    className='container',
    style={
        "maxWidth": "1600px",
        "height": "100%",
        "width": "100%",
        "padding": "0px 20px"})

"""
CALLBACKS
"""


# callbacks for loading different apps
@app.callback(
    Output('app_container', 'children'),
    [Input('url', 'pathname')])
def display_page(path):
    path = str(path)
    if path.startswith("/analysis"):
        return analysis_view.serve_layout()
    else:
        return search_view.serve_layout()

# setting the static path for loading css files


@app.server.route('/static/css/<path:path>')
def get_stylesheet(path):
    static_folder = os.path.join(os.getcwd(), 'matscholar_web/static/css')
    return send_from_directory(static_folder, path)


search_view_callbacks.bind(app)
