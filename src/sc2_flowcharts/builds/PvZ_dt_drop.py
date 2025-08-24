from sc2_flowcharts.graph import BuildGraph
from sc2_flowcharts.builds.PvZ_cheese_counter import make_graph as cheese_graph
opening = """
14 Lowground Pylon
00:38 Chrono probes + Gate
S Send Gate probe to scout
Gas w/ 17th probe
19 Probe rallied down
"""

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
Pull 5 extra probes to attack hatchery (6 total)
Attack hatchery with probes + Zealot
If drone pull, wait for second zealot and engage
"""

proxy_hatch_steps = """
S Tell is no hatch but pool only halfway done
Pylon
Chrono Zealot
Cybercore Gate in wall
Pull 4 extra probes and go delay spines with zealot
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

fast_sg_steps = """
StarGate (As part of wall if needed)
WarpGate
Chrono Void Ray
Twilight
Robo
Charge
A Deny scout with VoidRay
Pull off gas (32 probes total)
+6 Gateways (8 total)
Pylons (~100 supply available)
Chrono Warp Prism
A Send prism across the map
Warp Zealots
Win
"""

standard_steps = """
20 Nexus
20 Cybercore
21 Gas
22 Pylon
Chrono adept
Twilight Council
Chrono stalker
Robo
S Scout main with adept - Main
Second Gate, finish wall
S Second scout with adept - Nat
S If no creep tumor, third unit
"""

low_drone_count = """
S 3:10 Less than 8 Drones
S No creep tumor in front of nat
Chrono second adept
Finish wall with gateway
Plug the wall with stalker
Make shield battery
Full wall with Gateway
"""

fast_lair_steps = """
Keep prism home
Warp dt/archons at home
Scout for nydus
"""

standard_cont = """
Dark shrine
Cut probes (38 for standard)
+2 Warpgates (4 total)
Chrono Warp Prism
Resume Probes
Gas 3 and 4
+2 Pylons
A Send prism across the map
A Probe and adept to the third
Hold position probe in front of adept
4:30 Warp 4 DTs
A Try to kill the third
Observer, rally to prism
Third base + pylon
Forge + pylon
A Bring prism back
Morph archons (staggered)
Battery at third
Chrono immortal
Warp 2 sentries
A Archons drop
Cut probes
+1 Atk and Charge
Chrono Second Immortal
+4 Gates, 8 total
Warp 4 sentries
Chrono +1 atk
Chrono 3rd Immortal
A Move out @3 immos
Warp zealots at the front
7:30 A Attack
"""

def make_graph(d: BuildGraph | None = None):
    d = d or BuildGraph()
    n1 = d.build_node(opening, reaction="Probe scout")

    # Getting cheesed
    cheese = d.bold_node("Getting Cheesed")
    d.edge(n1, cheese)
    _, start_nodes, end_nodes = cheese_graph(d)
    d.dotedge(cheese, start_nodes)
    # Got cheesed, collect quick win
    quick_sg = d.build_node(fast_sg_steps, title="Quick Win Stargate")
    d.dotedge(end_nodes, quick_sg)


    standard = d.build_node(standard_steps)

    adept_scout = d.reaction("Adept scout", parent=standard)
    low_drone = d.build_node(low_drone_count, title="Low Drone Count")
    dark_shrine = d.build_node(standard_cont, title="DT Drop into chargelots")
    d.edge(standard, adept_scout)
    d.edge(adept_scout, low_drone)
    d.edge(low_drone, dark_shrine)
    fast_lair = d.build_node(fast_lair_steps, title="Fast Lair")
    d.edge(adept_scout, fast_lair)
    d.edge(fast_lair, dark_shrine)

    d.edge(n1, standard, label="Standard")
    d.edge(adept_scout, dark_shrine, label="Standard")

    # Make graph more vertical, otherwise all nodes are squashed together
    d = d.unflatten(stagger=3, fanout=True)

    return d