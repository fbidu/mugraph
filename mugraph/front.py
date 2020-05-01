"""
Provides a simple Flask app that renders the graph
"""

from flask import Flask
from flask import render_template


class Dashboard:
    def __init__(self, graph):
        self.graph = graph
        self.app = Flask("dashboard")

    def render(self):
        return render_template("dashboard.html", graph=self.graph)

    def run(self):
        self.app.add_url_rule("/", view_func=self.render)
        self.app.run()
