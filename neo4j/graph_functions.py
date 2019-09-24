from py2neo import Graph
graph = Graph("bolt://localhost:7687", auth = ("neo4j", 
                                       "ILikeYuri"))
from PIL import Image

def ResetNeo():
    graph.run('''
      MATCH (n)
      OPTIONAL MATCH (n)-[r]-()
      WITH n,r LIMIT 50000
      DELETE n,r
      RETURN count(n) as deletedNodesCount
    ''')

#############
## Objects ##
#############
class ParamDict(dict):
    def __repr__(self):
        s = "{"
        for key in self:
            s += "{0}: '{1}', ".format(key, self[key])
        if len(s) > 1:
            s = s[0: -2]
        s += "}"
        return s


###############
## Functions ##
###############
def CreateNewNode(label: str, params: ParamDict):
    graph.run(f"CREATE (:{label} {params})")

def CreateNewRelation(rel_label: str, node_a: str, node_b: str):
    graph.run(f"MATCH (a:n {ParamDict(name=node_a)})")
    graph.run(f"MATCH (b:n {ParamDict(name=node_b)})")
    graph.run(f"RETURN CREATE (a)-[rel:{rel_label}]-(b)")