import graphviz
from sc2_flowcharts.formatting import parse_step, TABLE_FSTRING, format_title, GRAPH_ATTR, NODE_ATTR, EDGE_ATTR, REACTION_COLOR, SCOUT_COLOR

class BuildGraph(graphviz.Digraph):

    def __init__(self, *args, graph_attr: dict=None, node_attr: dict=None, edge_attr: dict=None, **kwargs):
        graph_attr = graph_attr or {}
        graph_attr.update(GRAPH_ATTR)

        node_attr = node_attr or {}
        node_attr.update(NODE_ATTR)

        edge_attr = edge_attr or {}
        edge_attr.update(EDGE_ATTR)
        super().__init__(*args, graph_attr=graph_attr, node_attr=node_attr, edge_attr=edge_attr, **kwargs)
        self.last = None
        self.num_nodes = 0

    def node(self, name, *args, **kwargs):
        super().node(name, *args, **kwargs)
        self.num_nodes += 1
        self.last = name

    def nid(self):
        """Unique incrementing ID"""
        return f"{self.num_nodes + 1}"
    
    def build_node(self, build: list[str], title: str = "", reaction: str=""):
        if isinstance(build, str):
            build = build.strip().split("\n")
        if title:
            title = format_title(title)
        steps = [parse_step(step) for step in build]
        all_steps = [title] + steps if title else steps
        full_table = TABLE_FSTRING.format("".join(all_steps))
        id1 = self.nid()
        self.node(id1, label=full_table, shape="box")
        if reaction:
            self.reaction(reaction)
            self.edge(id1, self.last)
        return self.last
    
    def reaction(self, reaction: str, parent: str=""):
        """Add a reaction node to the graph."""
        parent = parent or self.last
        self.node(self.nid(), label=f"<<B>{reaction}</B>>", shape="ellipse", fontcolor=SCOUT_COLOR)
        # raise ValueError(f"Reaction node '{self.last}' added to parent '{parent}'")
        return self.last
    
    def bold_node(self, title: str, color: str = REACTION_COLOR):
        """Add a bold node to the graph."""
        id1 = self.nid()
        label = f"<<B>{title}</B>>"
        self.node(id1, label=label, shape="box", style="rounded,filled", fontcolor=color)
        return id1
    
    def dotedge(self, start_nodes: str|list[str], end_nodes: str|list[str]):
        """Aggregate nodes into a single node."""
        if isinstance(start_nodes, str):
            start_nodes = [start_nodes]
        if isinstance(end_nodes, str):
            end_nodes = [end_nodes]
        for start in start_nodes:
            for end in end_nodes:
                self.edge(start, end)