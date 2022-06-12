from matplotlib.pyplot import figure
import mpld3

from mpld3._server import serve

class InlineWrapper:
    def __init__(self):
        self.figs=[]
    def add_figure(self,fig):
        self.figs.append(fig)
    def serve(self):
        html=""
        for fig in self.figs:
            html+=mpld3.fig_to_html(fig)
        serve(html)
