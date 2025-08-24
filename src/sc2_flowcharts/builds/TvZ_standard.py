from sc2_flowcharts.graph import BuildGraph
from sc2_flowcharts.formatting import RED, GREEN

# Base 3CC Build Steps
three_cc_opening_1 = """
14 Depot
16 Rax
16 Gas (fill gas once finished)
20 Orbital + Reaper
20 Nat CC
Marine after reaper
Factory @ next 100 gas
"""

three_cc_opening_2 = """
Reactor on Rax after Marine completes
Third CC @400 minerals
Orbital after Nat CC finishes
Swap Reactor between Factory + Rax
Starport + 2nd gas after Factory finishes
Hellions 2x (6 total, can do 8)
Rax Techlab @ next 25 gas
Orbital on 3rd CC when completed
Move out with Hellions @ 4 complete
S Scouting done via Reaper, Hellions, Viking, Libs or Banshees
S Do not scan
S Do not sack Reaper or Hellion unless there's a clear opening 
"""

one_base_baneling = """
Reinforce wall with buildings
Build marines and hellions asap
"""

one_base_3_rav = """
Bunker in wall (move rax)
Cyclone asap
Go into any variation starting from when your factory finishes
Always get natural and 3rd CC. No exceptions. 
"""

lib_variation = """
@100% Starport - Viking
A Go kill overlords with vikings
@Next 100 gas after Viking - Stim
@Next 125 gas - Liberator
@Liberator complete - Reactor on Starport
A Go siege main or nat with liberator
"""

banshee_variation = """
@100% Starport - Swap Rax with Starport
Banshee THEN Cloak with next available gas
Rax sits empty until gas is available for Techlab
Second Banshee THEN Stim
"""

reaction_ling_flood = """
A Micro with 4 Hellions
A Get 8 Hellions if more lings come
S If Viking+Libs: counter-damage unless Hellions die
S If Banshees: defend until 2 banshees + cloack
"""

reaction_8_roach = """
Bunker at Nat and top of ramp
Start Marine production one at a time
S Pray you get starport unit out before losing all SCVs
"""

reaction_ravling = """
Bunker at Nat and top of ramp
Start Marine production one at a time
Widow Mines/Hellions and Liberators/banshee one at a time if needed
S If vikings and libs: Stay home
S If banshees: keep them alive
"""

universal_followup = """
Lift factory, add reactor
Reactor on Startport FIXME
Two rax; one on reactor, one to swap with factory
Two ebays + 3rd gas. 4th shortly after
Fourth and 5th rax
Start 1-1
Swap factory and empty rax, start tech lab
Start tank production
Start Medivacs production
Third CC orbital, land as early as you can
Only do it if you feel safe enough
Reactors on rax 4 and 5
6:35 A Have around 100 supply when two medivacs pop
Second factory
Armoury @ 50% 1-1
7:45 A ~145 supply, 1-1, 4 medivacs, marine ball, 2 tanks
8:40 Fourth base
"""

basic_tvz_production = """
One BASE: 1-1-1
Two BASES: 3-1-1 (OR 5-1-1 if allin)
Three BASES: 5-1-1 (OR 8-1-1 if allin)(OR 5-2-1 standard ramp up)
Four BASES: 8-2-1
Five+ BASES: 8+-2+-1+ (WHATEVER IS NEEDED)
"""

def make_graph(d: BuildGraph | None = None):
    d = d or BuildGraph()
    open1 = d.build_node(three_cc_opening_1, title="Standard 3CC Opener", reaction="Reaper scout")


    # One base variation
    one_base = d.bold_node("One base")
    d.edge(open1, one_base)
    rav = d.build_node(one_base_3_rav, title="3 Ravagers")
    banelings = d.build_node(one_base_baneling, title="baneling bust")
    d.dotedge(one_base, [rav, banelings])

    # Standard
    standard = d.bold_node("Standard")
    d.edge(open1, standard)

    # Continue game plan
    open2 = d.build_node(three_cc_opening_2, title="Open continuation")
    d.dotedge([standard, rav, banelings], open2)



    # Liberator Variation
    lib = d.build_node(lib_variation, title="Liberator Variation")
    # Banshee Variation
    banshee = d.build_node(banshee_variation, title="Banshee Variation")
    d.dotedge(open2, [lib, banshee])

    scout = d.reaction("Scout reactions")
    d.dotedge([lib, banshee], scout)
    agro = d.bold_node("Enemy Aggression Detected",)
    std = d.bold_node("Standard Zerg BS")
    d.dotedge(scout, [agro, std])

    # Enemy Reactions
    ling_flood = d.build_node(reaction_ling_flood, title="Vs Ling Flood")
    roach = d.build_node(reaction_8_roach, title="Vs 8 Roach")
    ravling = d.build_node(reaction_ravling, title="Vs Ravager-Ling All-In")
    d.edge(agro, ling_flood)
    d.edge(agro, roach)
    d.edge(agro, ravling)

    # Follow-up for all variations
    follow = d.build_node(universal_followup, title="All Variants Follow-up")
    d.dotedge([std, ling_flood, roach, ravling], follow)

    # end = d.build_node(basic_tvz_production, title="Production benchmarks")
    # d.edge(follow, end)
    
    # comps = d.bold_node("Army compositions")
    # d.edge(end, comps)

    # ennemy_comp1 = d.bold_node("ling, bane, ultra, viper, infestor", RED)
    # ennemy_comp2 = d.bold_node("Brood, corruptor, infestor, viper, ground support", RED)
    # ennemy_comp3 = d.bold_node("Lurker, viper, hydra, infestor, ling, bane", RED)
    # d.dotedge(comps, [ennemy_comp1, ennemy_comp2, ennemy_comp3])

    # easy_comp1 = d.bold_node("Turtle: tanks, libs, marines, marauders, thors, 2-4 vikings", GREEN)
    # d.edge(ennemy_comp1, easy_comp1, label="easy")
    # easy_comp2 = d.bold_node("Turtle: Thors, libs, marines, marauders, thors, 2-4 vikings", GREEN)
    # d.edge(ennemy_comp2, easy_comp2, label="easy")
    # easy_comp3 = d.bold_node("Marine, Marauder, Tanks, Libs, 2-3 thors + 2-4 vikings", GREEN)
    # d.edge(ennemy_comp3, easy_comp3, label="easy")

    # hard_comp1 = d.bold_node("Ghosts, Thors, Libs, Tanks, Marines", GREEN)
    # d.edge(ennemy_comp2, hard_comp1, label="hard")
    # d.edge(ennemy_comp3, hard_comp1, label="hard")
    # hard_comp2 = d.bold_node("Ghosts, tanks, libs, thors", GREEN)
    # d.edge(ennemy_comp1, hard_comp2, label="hard")

    return d.unflatten(stagger=2, fanout=True)