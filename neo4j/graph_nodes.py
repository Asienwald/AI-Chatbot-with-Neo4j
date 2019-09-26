from py2neo import Node, Relationship

building_nodes = dict(
    t19 = Node("Building", name = "T19", description = "enter descrip", school = "SoC"),
    t21 = Node("Building", name = "T21", description = "enter descrip 2", school = "SoC")
)

food_nodes = dict(
    fc6 = Node("Food", name = "Food Court 6", description = "Suck food"),
    macs = Node("Food", name = "McDonalds", description = "GGood food mmmm")
)

graph_nodes= [building_nodes, food_nodes]


## Relations start here
walk_relations = [
    Relationship(building_nodes['t19'], "WALK", building_nodes['t21']),
    Relationship(food_nodes['fc6'], "WALK", building_nodes['t21'])
]

relation_nodes = [walk_relations]