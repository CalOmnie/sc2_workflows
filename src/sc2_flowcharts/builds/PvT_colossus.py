from sc2_flowcharts.graph import BuildGraph

opening_steps = """
14 Reaper Wall Pylon
00:38 Chrono probes + Gate
Gas w/ 17th probe
18 Probe rallied down
Send extra probe to gas
All Same probe:
19 Nexus
19 CyberCore
20 Gas
21 Lowground Pylon
Chrono stalker + WG
Lowground Battery
Sentry
Chrono Natural Nexus
S Energy recharge sentry + Scout
Gateway
Stalker
"""

standard_steps = """
Blink (Chrono)
Pylon
Third Gateway
3:50 Third base + pylon
Pylon (edge of main)
Third Gas
Robo
Warp 3 stalkers
Pylon (edge of third)
Keep Warping stalkers
A Split army between main and Nat
Observers (2)
Charge ASAP
Battery in every base
5:17 Forge (+1 atk)
Robo Bay
Fourth Gas
Five Gates (8 total)
Fourth Base
"""

one_base_steps = """
Charge (Chrono)
Pylon
Warp 2 more stalkers
Battery in main
S Check for tech lab starport
If Yes, 5 Gates + Robo, make obs
Go to 6 gates
Move out with 4 stalkers
More batteries
Wait for charge then engage
"""

three_rax_steps = """
Blink (Chrono)
Pylon
Robo + 2 Gas
Stalker warp-in
Pylon
Immortal ASAP
Warp in stalkers
4:40 Robo Bay
4:50 A Defend three rax
Observer x 2
Colossus
Third base
Forge
Charge
A Always chrono colossus
Second/Third colossus
Add 6 Gates (8 total)
Templar archives
Warp prism
A Move out at +1 atk/3 colossus
A Warp in Archons at the front
"""

def make_graph():
    dot = BuildGraph(comment='PvT Colossus Build Order')
    opening = dot.build_node(opening_steps, title="Opening", reaction="Scout with Hallucination")
    standard = dot.build_node(standard_steps, title="Standard")
    tree_rax = dot.build_node(three_rax_steps, title="Three Rax")
    one_base = dot.build_node(one_base_steps, title="One Base")
    dot.edge(opening, tree_rax)
    dot.edge(opening, standard)
    dot.edge(opening, one_base)
    
    return dot