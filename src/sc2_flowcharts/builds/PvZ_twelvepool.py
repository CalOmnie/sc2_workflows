__all__ = ['TwelvePool']
class TwelvePool:
    """12 pool reaction, this is assuming we have scouted the 12 pool."""
    def update_graph(self, graph):
        # Nodes
        graph.node('12pP1', 'Pylon + Scout')
        graph.node('12pC', 'Check Natural → No Hatch?')
        graph.node('12pM', 'Send Probe to Main')
        graph.node('12pS', 'See Pool + Lings?')
        graph.node('12pW', 'Build Gateway + Cybercore + 2nd Gateway')
        graph.node('12pPY2', 'Build 2nd Pylon')
        graph.node('12pZ1', 'Start Zealot (no Chrono)')
        graph.node('12pCR', 'Chrono Zealot @70%')
        graph.node('12pZ2', 'Build 2nd Zealot')
        graph.node('12pAD', 'Start 2x Adepts')
        graph.node('12pP3', 'Build 3rd Pylon')
        graph.node('12pN', 'Start Nexus')
        graph.node('12pSG', 'Start Stargate + 2nd Gas')
        graph.node('12pSC', 'Scout w/ Adepts')
        graph.node('12pADJ', 'Adjust vs Banelings/Roaches')
        graph.node('12pMG', 'Transition to Midgame (Oracle, 3rd Base, etc.)')

        # Edges
        graph.edges([('12pP1', '12pC'), ('12pC', '12pM'), ('12pM', '12pS')])
        graph.edge('12pS', '12pW', label='If Yes')
        graph.edge('12pW', '12pPY2')
        graph.edge('12pPY2', '12pZ1')
        graph.edge('12pZ1', '12pCR')
        graph.edge('12pCR', '12pZ2')
        graph.edge('12pZ2', '12pAD')
        graph.edge('12pAD', '12pP3')
        graph.edge('12pP3', '12pN')
        graph.edge('12pN', '12pSG')
        graph.edge('12pSG', '12pSC')
        graph.edge('12pSC', '12pADJ')
        graph.edge('12pADJ', '12pMG')

        return "12pP1"