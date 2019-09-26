from py2neo import Node, Relationship

building_nodes = dict(
    t1 = Node("Building", name = "T1", description = "dark blue", school = ""),
    t2 = Node("Building", name = "T2", description = "dark blue", school = ""),
    w1 = Node("Building", name = "W1", description = "dark blue"),
    w2 = Node("Building", name = "W2", description = "dark blue"),
    w3 = Node("Building", name = "W3", description = "dark blue"),
    t3 = Node("Building", name = "T3", description = "bright yellow", school = ""),
    t3a = Node("Building", name = "T3A", description = "bright yellow", school = ""),
    w4 = Node("Building", name = "W4", description = "bright yellow"),
    w5 = Node("Building", name = "W5", description = "bright yellow"),
    t4 = Node("Building", name = "T4", description = "red", school = ""),
    t4a = Node("Building", name = "T4A", description = "red", school = ""),
    t5 = Node("Building", name = "T5", description = "red", school = ""),
    t6 = Node("Building", name = "T6", description = "red", school = ""),
    t7 = Node("Building", name = "T7", description = "red", school = ""),
    t8 = Node("Building", name = "T8", description = "red", school = ""),
    t9 = Node("Building", name = "T9", description = "red", school = ""),
    t10 = Node("Building", name = "T10", description = "purple", school = ""),
    t11a = Node("Building", name = "T11A", description = "brown", school = "CLS"),
    t11b = Node("Building", name = "T11B", description = "brown", school = "CLS"),
    t11c = Node("Building", name = "T11C", description = "brown", school = "CLS"),
    t12 = Node("Building", name = "T12", description = "brown", school = "CLS"),
    t12a = Node("Building", name = "T12A", description = "brown", school = "CLS"),
    t14 = Node("Building", name = "T14", description = "brown", school = "CLS"),
    t15 = Node("Building", name = "T15", description = "brown", school = "CLS"),
    t16 = Node("Building", name = "T16", description = "brown", school = "CLS"),
    t17 = Node("Building", name = "T17", description = "muted yellow", school = ""),
    t18 = Node("Building", name = "T18", description = "muted yellow", school = ""),
    w12 = Node("Building", name = "W12", description = "muted yellow"),
    w13 = Node("Building", name = "W13", description = "muted yellow"),
    w14 = Node("Building", name = "W14", description = "muted yellow"),
    t19 = Node("Building", name = "T19", description = "blue", school = "SoC"),
    t20 = Node("Building", name = "T20", description = "blue", school = "SoC"),
    t21 = Node("Building", name = "T21", description = "blue", school = "SoC"),
    t22 = Node("Building", name = "T22", description = "blue", school = "SoC"),
    sob = Node("Building", name = "SoB", description = "blue")
)

facilities_nodes = dict(
    audi = Node("Facility", name = "Auditorium", type = "info", description = "muted yellow"),
    cc = Node("Facility", name = "Convention Centre", type = "info", description = "muted yellow"),
    aero = Node("Facility", name = "Aerohub", type = "info", description = "muted yellow"),
    maepw = Node("Facility", name = "MAE Project Workshop", type = "lab", description = "muted yellow"),
    ds = Node("Facility", name = "Dance Studio", type = "recreation", description = "muted yellow"),
    hilltop = Node("Facility", name = "Hilltop Library", type = "library", description = "blue"),
    mlt8 = Node("Facility", name = "Major Lecture Theatre 8", type = "info", description = "blue"),
    mlt9 = Node("Facility", name = "Major Lecture Theatre 9", type = "info", description = "blue"),
    mlt10 = Node("Facility", name = "Major Lecture Theatre 10", type = "info", description = "blue"),
    mlt11 = Node("Facility", name = "Major Lecture Theatre 11", type = "info", description = "blue"),
    mlt12 = Node("Facility", name = "Major Lecture Theatre 12", type = "info", description = "blue"),
    spec = Node("Facility", name = "Spectrum", type = "study", description = "brown"),
    eleven = Node("Facility", name = "eleven²", type = "study", description = "brown"),
    mpf = Node("Facility", name = "Multi Purpose Field", type = "sports", description = "purple"),
    gym = Node("Facility", name = "The Place", type = "sports", description = "purple"),
    sc = Node("Facility", name = "Swimming Complex", type = "sports", description = "purple"),
    sa = Node("Facility", name = "Sports Arena", type = "sports", description = "purple")
)

food_nodes = dict(
    fc1 = Node("Food", name = "Food Court 1", description = "dark blue"),
    fc2 = Node("Food", name = "Food Court 2", description = "dark blue"),
    fc3 = Node("Food", name = "Food Court 3", description = "purple"),
    fc4 = Node("Food", name = "Koufu", description = "muted yellow"),
    fc5 = Node("Food", name = "Food court 5", description = "purple"),
    fc6 = Node("Food", name = "Food Court 6", description = "blue"),
    macs = Node("Food", name = "McDonalds", description = "brown")
)

graph_nodes= [building_nodes, facilities_nodes, food_nodes]


## Relations start here
walk_relations = [
    Relationship(building_nodes["t19"], "WALK", building_nodes["sob"]),
    Relationship(building_nodes["sob"], "WALK", facilities_nodes["aero"]),
    Relationship(facilities_nodes["aero"], "WALK", facilities_nodes["cc"]),
    Relationship(facilities_nodes["cc"], "WALK", building_nodes["t18"]),
    Relationship(building_nodes["t18"], "WALK", facilities_nodes["audi"]),
    Relationship(facilities_nodes["audi"], "WALK", building_nodes["t17"]),
    Relationship(building_nodes["t17"], "WALK", building_nodes["w14"]),
    Relationship(building_nodes["w14"], "WALK", building_nodes["w13"]),
    Relationship(building_nodes["w13"], "WALK", building_nodes["w12"]),
    Relationship(building_nodes["t17"], "WALK", building_nodes["t16"]),
    Relationship(building_nodes["t16"], "WALK", building_nodes["t15"]),
    Relationship(building_nodes["t15"], "WALK", building_nodes["t14"]),
    Relationship(facilities_nodes["maepw"], "WALK", building_nodes["w12"]),
    Relationship(facilities_nodes["ds"], "WALK", building_nodes["w14"]),
    Relationship(building_nodes["t14"], "WALK", building_nodes["t11a"]),
    Relationship(building_nodes["t12a"], "WALK", building_nodes["t15"]),
    Relationship(building_nodes["t11b"], "WALK", building_nodes["t11a"]),
    Relationship(food_nodes["fc5"], "WALK", building_nodes["t16"])
]

connected_to_relations = [
    Relationship(building_nodes["t19"], "CONNECTED_TO", building_nodes["t20"]),
    Relationship(building_nodes["t20"], "CONNECTED_TO", building_nodes["t21"]),
    Relationship(building_nodes["t19"], "CONNECTED_TO", building_nodes["t21"]),
    Relationship(building_nodes["t22"], "CONNECTED_TO", building_nodes["t21"]),
    Relationship(facilities_nodes["hilltop"], "CONNECTED_TO", building_nodes["t22"]),
    Relationship(food_nodes["macs"], "CONNECTED_TO", facilities_nodes["spec"]),
    Relationship(building_nodes["t12"], "CONNECTED_TO", building_nodes["t12a"]),
    Relationship(facilities_nodes["eleven"], "CONNECTED_TO", building_nodes["t11a"]),
    Relationship(building_nodes["t11c"], "CONNECTED_TO", building_nodes["t11b"]),
    Relationship(facilities_nodes["sc"], "CONNECTED_TO", food_nodes["fc5"]),
    Relationship(facilities_nodes["gym"], "CONNECTED_TO", facilities_nodes["sc"]),
    Relationship(facilities_nodes[""])
]

in_same_building_relations = [
    Relationship(food_nodes["fc6"], "IN_SAME_BUILDING", building_nodes["t19"]),
    Relationship(food_nodes["fc4"], "IN_SAME_BUILDING", facilities_nodes["aero"]),
    Relationship(facilities_nodes["mlt8"], "IN_SAME_BUILDING", building_nodes["t19"]),
    Relationship(facilities_nodes["mlt9"], "IN_SAME_BUILDING", building_nodes["t19"]),
    Relationship(facilities_nodes["mlt10"], "IN_SAME_BUILDING", building_nodes["t19"]),
    Relationship(facilities_nodes["mlt11"], "IN_SAME_BUILDING", building_nodes["t19"]),
    Relationship(facilities_nodes["mlt12"], "IN_SAME_BUILDING", building_nodes["t21"]),
    Relationship(facilities_nodes["spec"], "IN_SAME_BUILDING", building_nodes["t15"])
]

relation_nodes = [walk_relations, connected_to_relations, in_same_building_relations]