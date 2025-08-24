from sc2_flowcharts.graph import BuildGraph
twelvepool = """
1:10 S Check gas and larva with probe
1:20 Pylon
1:26 Chrono Zealot, full wall with gate + cyber
Second zealot
22 Cut probes (26 total)
2:10 Pylon
Build 2 adepts
2:34 Nexus
S Scout with the 2 adepts
Second Gas
"""

hatch_in_wall_steps = """
Pylon
Chrono Zealot
Cybercore in wall, no second gate
A Pull 5 extra probes to attack hatchery (6 total)
Attack hatchery with probes + Zealot
If drone pull, wait for second zealot and engage
"""

proxy_hatch_steps = """
S Tell is no hatch but pool only halfway done
Pylon
Chrono Zealot
Cybercore Gate in wall
A Pull 4 extra probes and go delay spines with zealot
A Kill the drones
Shield Battery ASAP
Stalkers after 2 zealots
Keep making shield batteries until safe
"""

sixteenpool = """
S Hide probe
1:25 Cybercore
1:33 Nexus
20 Pylon Wall
Resume probes
Gas
Chrono adept
2:10 S Send probe back in
Full wall with pylon until adept
Chrono Second adept
Shield battery
If allin: Stalker
Full wall behind stalker
"""

def make_graph(d: BuildGraph | None = None) -> tuple[BuildGraph, list, list]:
    d = d or BuildGraph()

    # Getting cheesed
    twelve = d.build_node(twelvepool, title="12 Pool")
    proxy_hatch = d.build_node(proxy_hatch_steps, title="Proxy Hatchery")
    hatch_in_wall = d.build_node(hatch_in_wall_steps, title="Hatchery in Wall")
    early_pool = d.build_node(sixteenpool, title="16 Pool")
    
    start_nodes = end_nodes = [twelve, proxy_hatch, hatch_in_wall, early_pool]

    return d, start_nodes, end_nodes