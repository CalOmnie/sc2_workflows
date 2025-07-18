import sys
from sc2_flowcharts.builds import PvT_twelvepool
import graphviz
from graphviz import Digraph



def main():
    """Console script for sc2_flowcharts."""
    print("Edit src/sc2_flowcharts/__main__.py to extend CLI.")
    return 0

if __name__ == "__main__":
    dot = Digraph(comment='PvZ 12 Pool Defense Build Order')
    print(dir(PvT_twelvepool))
    pool = PvT_twelvepool.TwelvePool()
    start_name = pool.update_graph(dot)
    print(start_name, dot)
    dot.render('PvT_12pool.gv', format='png')
    sys.exit(main)
