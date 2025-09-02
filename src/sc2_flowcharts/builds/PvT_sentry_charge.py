from sc2_flowcharts.graph import BuildGraph

opening_steps = """
14 Pylon
16 Chrono probes + Gate
17 Gas w/ 17th probe
18 Probe rallied down
Send extra probe to gas
20 Nexus
S Scout for proxy
20 core
21 Gas
22 Lowground Pylon (same worker as gas)
Chrono stalker + WG
Lowground Battery
Chrono main Nexus
"""

proxy_response = """
A Subscribe to Patreon Tier 5
"""

opening_continued = """
Sentry
Twilight Council
S Pull 2 probes off gas
S Energy recharge sentry + Scout
S Scout ennemy nat then main
Stalker
Two Gateways (don't cut probes)
Charge
Third Pylon in base (trust)
Re-saturate main gas when nat saturated
Third Nexus (3:40-3:55)
"""

mine_response = """
Video Timestamp: 17:58 and 25:42
S Second hallucination as soon as you see the Starport produce
Go to 5-7 stalkers + 1 sentry
A Split army in main and natural
S Recharge + Third hallucination to track medivac
"""

cyclone_response = """
Video Timestamp: 14:32
Battery in main mineral line
Five stalkers then warp zealots
S Track medivac with hallucination
"""

reaper_hellion_response = """
Video Timestamp: 10:57
Full wall With Gateway
Delay nexus a bit
Keep 2 stalkers in main
Keep the sentry in nat for forcefields
"""

helion_drop_response = """
Video Timestamp: 21:00
Battery in main mineral line
Fourth stalker before pylon + charge
S Early second hallucination
S Track the hellions
Full wall with gateway
A Hold with 4 stalkers + sentry
A Focus medivac first
A Try to forcefield hellions
Warp more stalkers and move out once held
A Chase the starport
"""

three_one_zero_response = """
Video Timestamp: XX:XX
Regular expand timing
A Stay on 2 stalkers
Constant zealot warpins
4:05 Templar Archives ASAP
Gradually go to 5 gates when you have the money
S Scout for moveout with probe and hallucination
A Prioritise warp-ins
4:45 Chrono storm
Warp 3 templars - energy recharge
Forge with excess money - +1 defense
A Send 4-5 zealots around the map to counterattack
A Go out on the map and fish for big storms
"""

standard_followup = """
Robo
Third Gas
S Halluc scout to check Terran followup
A Continuous Zealot warp-ins until then
Templar Archives
"""

agro_followup = """
Video Timestamp: 28:46
Battery in main if you expect banshees or drops
Keep making zealots
Make immortals
Chrono your gates if needed
S Keep scouting until you see more rax
"""

macro_followup = """
Storm
Go to 8 Gateways
Warp prism
Forge
Warp 3-4 templars
Keep making zealots
Fourth base
S Get vision on the map
"""





def make_graph():
    dot = BuildGraph(comment='PvT Colossus Build Order')
    opening = dot.build_node(opening_steps, title="Opening")
    proxy = dot.build_node(proxy_response, title="Getting proxied")
    dot.edge(opening, proxy)

    opening_cont = dot.build_node(opening_continued, title="")
    dot.edge(opening, opening_cont)

    first_halluc = dot.reaction("First hallucination scout", parent=opening_cont)
    dot.edge(opening_cont, first_halluc)

    responses = [
        dot.build_node(mine_response, title="Mine Drop"),
        dot.build_node(cyclone_response, title="Cyclone Drop"),
        dot.build_node(reaper_hellion_response, title="3 Reapers 2 Hellions"),
        dot.build_node(helion_drop_response, title="Hellion Drop"),
    ]
    three_one_zero = dot.build_node(three_one_zero_response, title="3-1-0 push")
    dot.edge(first_halluc, three_one_zero)
    dot.dotedge(first_halluc, responses)

    standard = dot.build_node(standard_followup)
    dot.dotedge(responses, standard)
    
    followup_scout = dot.reaction("Followup scout")
    dot.edge(standard, followup_scout)
    agro_followup_node = dot.build_node(agro_followup, title="Signs of aggression")
    macro_followup_node = dot.build_node(macro_followup, title="Midgame setup")
    dot.dotedge(followup_scout, [agro_followup_node, macro_followup_node])
    dot.edge(three_one_zero, macro_followup_node)
    dot.edge(agro_followup_node, macro_followup_node)

    mid = dot.bold_node("Go into midgame")
    dot.edge(macro_followup_node, mid)

    # dot = dot.unflatten(stagger=2, fanout=True)
    
    return dot