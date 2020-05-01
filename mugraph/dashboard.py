"""
Module for the Bokeh dashboard
"""
import networkx as nx

from bokeh.io import output_file, show
from bokeh.models import (
    BoxZoomTool,
    Circle,
    HoverTool,
    MultiLine,
    Plot,
    Range1d,
    ResetTool,
)
from bokeh.palettes import Spectral4
from bokeh.plotting import from_networkx

OUT_COLOR, IN_COLOR = "black", "red"


def prepare_graph(graph, root):
    """
    prepare graph will color the in and out edges differently
    """

    edge_colors = {}
    edge_types = {}

    for start_node, end_node, _ in graph.edges(data=True):
        edge_color = OUT_COLOR if start_node == root else IN_COLOR
        edge_colors[(start_node, end_node)] = edge_color

    nx.set_edge_attributes(graph, edge_colors, "edge_color")
    nx.set_edge_attributes(graph, edge_types, "edge_type")


def plot_graph(parsed_graph):
    G = parsed_graph.graph

    prepare_graph(G, parsed_graph.root_name)
    # Show with Bokeh
    plot = Plot(
        plot_width=800,
        plot_height=800,
        x_range=Range1d(-1.1, 1.1),
        y_range=Range1d(-1.1, 1.1),
    )
    plot.title.text = f"{parsed_graph.root_name} Relationships"

    node_hover_tool = HoverTool(tooltips=[("name", "@index")])
    plot.add_tools(node_hover_tool, BoxZoomTool(), ResetTool())

    graph_renderer = from_networkx(G, nx.spring_layout, scale=1, center=(0, 0))

    graph_renderer.node_renderer.glyph = Circle(size=30, fill_color=Spectral4[0])
    graph_renderer.edge_renderer.glyph = MultiLine(
        line_color="edge_color", line_alpha=0.8, line_width=8, line_dash="dashed"
    )
    plot.renderers.append(graph_renderer)

    output_file("interactive_graphs.html")
    show(plot)
