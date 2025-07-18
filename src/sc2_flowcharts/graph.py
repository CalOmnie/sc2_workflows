import graphviz
from sc2_flowcharts.formatting import parse_step, TABLE_FSTRING

class BuildGraph(graphviz.Digraph):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.last = None
        self.num_nodes = 0

    def node(self, name, *args, **kwargs):
        super().node(name, *args, **kwargs)
        self.num_nodes += 1
        self.last = name

    def nid(self):
        """Unique incrementing ID"""
        return f"{self.num_nodes + 1}"
    
    def build_node(self, build: list[str], reaction: str=""):
        if isinstance(build, str):
            build = build.strip().split("\n")
        steps = map(parse_step, build)
        full_table = TABLE_FSTRING.format("".join(steps))
        id1 = self.nid()
        self.node(id1, label=full_table, shape="box")
        if reaction:
            self.reaction(reaction)
        return self.last
    
    def reaction(self, reaction: str, parent: str=""):
        """Add a reaction node to the graph."""
        parent = parent or self.last
        self.node(self.nid(), label=reaction, shape="ellipse", fillcolor="aquamarine", style="filled")
        self.edge(parent, self.last)
        # raise ValueError(f"Reaction node '{self.last}' added to parent '{parent}'")
        return self.last