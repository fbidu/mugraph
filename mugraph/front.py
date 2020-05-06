"""
Provides a simple Flask app that renders the graph
"""

from flask import Flask
from flask import render_template


class Dashboard:
    """
    The Dashboard receives a graph from the Parser and runs a web app with a
    visual representation of the microsservices and their connections.
    """

    def __init__(self, graph):
        self.graph = graph
        self.app = Flask("dashboard")
        self.app.config["EXPLAIN_TEMPLATE_LOADING"] = True
        self.app.config["DEBUG"] = True

    def render(self):
        """
        Returns the rendered Jinja2 template with the associated graph
        """
        return render_template("dashboard.html", graph=self.graph)

    def run(self):
        """
        Runs the flask app
        """
        self.app.add_url_rule("/", view_func=self.render)
        self.app.run(debug=True)
