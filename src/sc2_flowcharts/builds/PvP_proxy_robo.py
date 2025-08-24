from sc2_flowcharts.graph import BuildGraph

proxy_robo_steps = """
13 Pylon
15 Chrono probes + Gate
17 Gas
18 Gas
19 Gateway + chrono probes
S Send probe to build proxy
20 Cybercore + pull to gas (15 on mineral)
21 Proxy pylon
Go to one base saturation
Robo
Warpgate
Two Stalker
S Send robo probe to scout main
Pylon
Two more stalkers
Chrono Immortal
Pylon
Sentry
S Shield Battery in main if suspect SG
Chrono warp prism
Keep making immortals and Stalkers
"""

def make_graph():
    dot = BuildGraph(comment='PvP Proxy robo build order')
    opening = dot.bold_node("Start")
    proxy = dot.build_node(proxy_robo_steps, title="Proxy Robo")
    win = dot.bold_node("Win")
    dot.edge(opening, proxy)
    dot.edge(proxy, win)
    
    return dot