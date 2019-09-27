from py2neo import Node, Relationship
import random

building_nodes = dict(
    t1 = Node("building", name = "T1", description = "dark blue", school = ""),
    t1ac = Node("building", name = "T1A Concourse", description = "dark blue"),
    t2 = Node("building", name = "T2", description = "dark blue", school = ""),
    w1 = Node("building", name = "W1", description = "dark blue"),
    w2 = Node("building", name = "W2", description = "dark blue"),
    w3 = Node("building", name = "W3", description = "dark blue"),
    isc = Node("building", name = "Integrated Simulation Centre", description = "dark blue"),
    t3 = Node("building", name = "T3", description = "bright yellow", school = ""),
    t3a = Node("building", name = "T3A", description = "bright yellow", school = ""),
    w4 = Node("building", name = "W4", description = "bright yellow"),
    w5 = Node("building", name = "W5", description = "bright yellow"),
    w5a = Node("building", name = "W5A", description = "bright yellow"),
    t4 = Node("building", name = "T4", description = "red", school = ""),
    t4a = Node("building", name = "T4A", description = "red", school = ""),
    t5 = Node("building", name = "T5", description = "red", school = ""),
    t6 = Node("building", name = "T6", description = "red", school = ""),
    t7 = Node("building", name = "T7", description = "red", school = ""),
    t8 = Node("building", name = "T8", description = "red", school = ""),
    t9 = Node("building", name = "T9", description = "red", school = ""),
    t10 = Node("building", name = "T10", description = "purple", school = ""),
    t11a = Node("building", name = "T11A", description = "brown", school = "CLS"),
    t11b = Node("building", name = "T11B", description = "brown", school = "CLS"),
    t11c = Node("building", name = "T11C", description = "brown", school = "CLS"),
    t12 = Node("building", name = "T12", description = "brown", school = "CLS"),
    t12a = Node("building", name = "T12A", description = "brown", school = "CLS"),
    t14 = Node("building", name = "T14", description = "brown", school = "CLS"),
    t15 = Node("building", name = "T15", description = "brown", school = "CLS"),
    t16 = Node("building", name = "T16", description = "brown", school = "CLS"),
    t17 = Node("building", name = "T17", description = "muted yellow", school = ""),
    t18 = Node("building", name = "T18", description = "muted yellow", school = ""),
    w12 = Node("building", name = "W12", description = "muted yellow"),
    w13 = Node("building", name = "W13", description = "muted yellow"),
    w14 = Node("building", name = "W14", description = "muted yellow"),
    t19 = Node("building", name = "T19", description = "This building is filled with classrooms.", school = "SoC"),
    t20 = Node("building", name = "T20", description = "More classrooms.", school = "SoC"),
    t21 = Node("building", name = "T21", description = "This building has a lot of tables for students to use when studying.", school = "SoC"),
    t22 = Node("building", name = "T22", description = "This building is separated from the rest, but still filled with classrooms.", school = "SoC"),
    sob = Node("building", name = "SoB", description = "blue"),
    parking = Node("building", name = "Parking lot", description = "test")
)

facilities_nodes = dict(
    audi = Node("facility", name = "Auditorium", type = "info", description = "muted yellow"),
    cc = Node("facility", name = "Convention Centre", type = "info", description = "muted yellow"),
    aero = Node("facility", name = "Aerohub", type = "info", description = "muted yellow"),
    maepw = Node("facility", name = "MAE Project Workshop", type = "lab", description = "muted yellow"),
    ds = Node("facility", name = "Dance Studio", type = "recreation", description = "muted yellow"),
    hilltop = Node("facility", name = "Hilltop Library", type = "library", description = "blue"),
    mlt8 = Node("facility", name = "Major Lecture Theatre 8", type = "info", description = "blue"),
    mlt9 = Node("facility", name = "Major Lecture Theatre 9", type = "info", description = "blue"),
    mlt10 = Node("facility", name = "Major Lecture Theatre 10", type = "info", description = "blue"),
    mlt11 = Node("facility", name = "Major Lecture Theatre 11", type = "info", description = "blue"),
    mlt12 = Node("facility", name = "Major Lecture Theatre 12", type = "info", description = "blue"),
    spec = Node("facility", name = "Spectrum", type = "study", description = "brown"),
    eleven = Node("facility", name = "eleven²", type = "study", description = "brown"),
    mpf = Node("facility", name = "Multi Purpose Field", type = "sports", description = "purple"),
    mpc = Node("facility", name = "Multi Purpose Court", type = "sports", description = "purple"),
    bcourt = Node("facility", name = "Basketball Courts", type = "sports", description = "The basketball courts are often filled with people."),
    tcourt = Node("facility", name = "Tennis Courts", type = "sports", description = "This is where students can play tennis."),
    gym = Node("facility", name = "The Place", type = "sports", description = "This is a gym, although the name may not indicate so."),
    sc = Node("facility", name = "Swimming Complex", type = "sports", description = "The pools are used for swimming SFL in the evenings."),
    sa = Node("facility", name = "Sports Arena", type = "sports", description = "The sports arena is used for badminton SFL and as practice courts for sports clubs."),
    sac = Node("facility", name = "Student & Alumni Centre", type = "info", description = "purple"),
    polyc = Node("facility", name = "Poly Centre", type = "info", description = "purple"),
    moberly = Node("facility", name = "Moberly", type = "study", description = "Contains club rooms for recreational/arts CCA."),
    mainlib = Node("facility", name = "Main Library", type = "library", description = "This is a big library."),
    mainlibex = Node("facility", name = "Main Library Extension", type = "library", description = "The extension has many useful facilities."),
    admin = Node("facility", name = "Admin Building", type = "info", description = "Students can come to submit important documents like forms for EAE."), 
    sanc = Node("facility", name = "The Sanctuary", type = "study", description = "orange"),
    colours = Node("facility", name = "Colours", type = "study", description = "orange"),
    spav = Node("facility", name = "SPavillion", type = "study", description = "orange")
)

food_nodes = dict(
    fc1 = Node("food", name = "Food Court 1", description = "dark blue"),
    fc2 = Node("food", name = "Food Court 2", description = "dark blue"),
    fc3 = Node("food", name = "Food Court 3", description = "purple"),
    fc4 = Node("food", name = "Koufu", description = "muted yellow"),
    fc5 = Node("food", name = "Food court 5", description = "purple"),
    fc6 = Node("food", name = "Food Court 6", description = "blue"),
    macs = Node("food", name = "McDonalds", description = "brown"), 
    libcafe = Node("food", name = "Library Cafe", description = "orange")
)

lot_nodes = dict(
    a1 = Node("lots", name = "A-1"),
    a2 = Node("lots", name = "A-2"),
    a3 = Node("lots", name = "A-3"),
    a4 = Node("lots", name = "A-4"),
    a5 = Node("lots", name = "A-5"),
    a6 = Node("lots", name = "A-6"),
    a7 = Node("lots", name = "A-7"),
    a8 = Node("lots", name = "A-8"),
    a9 = Node("lots", name = "A-9"),
    a10 = Node("lots", name = "A-10"),
    a11 = Node("lots", name = "A-11"),
    a12 = Node("lots", name = "A-12"),
    a13 = Node("lots", name = "A-13"),
    a14 = Node("lots", name = "A-14"),
    a15 = Node("lots", name = "A-15"),
    a16 = Node("lots", name = "A-16"),
    a17 = Node("lots", name = "A-17"),
    a18 = Node("lots", name = "A-18"),
    a19 = Node("lots", name = "A-19"),
    a20 = Node("lots", name = "A-20")
)

event_nodes = dict(
    smartpoly = Node("event", name = "SmartPoly", description = "This is the smartpoly hackathon 2019.")
)

graph_nodes= [building_nodes, facilities_nodes, food_nodes, lot_nodes, event_nodes]

descrips = [
    "Turn left. Walk right, walk until you see it",
    "Walk to the next nearest turn and turn a left then a right then keep walking straight",
    "Climb up to level 2 and access the building through the bridge",
    "Walk along the classrooms and turn right before turning a left",
    "Walk to the intersection of the bridge and walk straight then turn right to the lifts",
    "Turn right from the intersection of the bridge and walk to the end of the corridor",
    "Go to the third floor and go across the bridge"
]


## Relations start here
walk_relations = [
    Relationship(building_nodes["t19"], "WALK", building_nodes["sob"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["sob"], "WALK", facilities_nodes["aero"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["aero"], "WALK", facilities_nodes["cc"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["cc"], "WALK", building_nodes["t18"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t18"], "WALK", facilities_nodes["audi"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["audi"], "WALK", building_nodes["t17"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t17"], "WALK", building_nodes["w14"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["w14"], "WALK", building_nodes["w13"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["w13"], "WALK", building_nodes["w12"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t17"], "WALK", building_nodes["t16"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t16"], "WALK", building_nodes["t15"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t15"], "WALK", building_nodes["t14"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["maepw"], "WALK", building_nodes["w12"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["ds"], "WALK", building_nodes["w14"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t14"], "WALK", building_nodes["t11a"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t12a"], "WALK", building_nodes["t15"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t11b"], "WALK", building_nodes["t11a"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(food_nodes["fc5"], "WALK", building_nodes["t16"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["sa"], "WALK", food_nodes["fc5"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["sac"], "WALK", facilities_nodes["sa"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["sac"], "WALK", facilities_nodes["polyc"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t10"], "WALK", facilities_nodes["polyc"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["sanc"], "WALK", building_nodes["t10"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["moberly"], "WALK", building_nodes["t10"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t7"], "WALK", facilities_nodes["sanc"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t9"], "WALK", facilities_nodes["sanc"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t8"], "WALK", building_nodes["t9"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t6"], "WALK", building_nodes["t9"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["mainlib"], "WALK", building_nodes["t6"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["colours"], "WALK", facilities_nodes["sanc"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["admin"], "WALK", facilities_nodes["colours"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["spav"], "WALK", facilities_nodes["colours"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t4"], "WALK", facilities_nodes["spav"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t4a"], "WALK", building_nodes["t4"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t3"], "WALK", building_nodes["t5"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t3a"], "WALK", building_nodes["t3"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["w4"], "WALK", building_nodes["t3a"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["w5a"], "WALK", building_nodes["w5"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["mpf"], "WALK", facilities_nodes["sa"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t2"], "WALK", building_nodes["t3"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(food_nodes["fc1"], "WALK", building_nodes["t3a"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t2"], "WALK", building_nodes["t1"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["w3"], "WALK", building_nodes["t1"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["w2"], "WALK", building_nodes["w3"], description = descrips[3], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["w1"], "WALK", building_nodes["w2"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["t1ac"], "WALK", building_nodes["t1"], description = descrips[1], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["isc"], "WALK", building_nodes["t1ac"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(facilities_nodes["moberly"], "WALK", facilities_nodes["tcourt"], description = descrips[0], distance = round(random.uniform(1.2, 25.6), 2)),
    Relationship(building_nodes["parking"], "WALK", building_nodes["t19"], description = descrips[2], distance = round(random.uniform(1.2, 25.6), 2))
]

connected_to_relations = [
    Relationship(building_nodes["t19"], "CONNECTED_TO", building_nodes["t20"], description = descrips[4], distance = 0),
    Relationship(building_nodes["t20"], "CONNECTED_TO", building_nodes["t21"], description = descrips[5], distance = 0),
    Relationship(building_nodes["t19"], "CONNECTED_TO", building_nodes["t21"], description = descrips[5], distance = 0),
    Relationship(building_nodes["t22"], "CONNECTED_TO", building_nodes["t21"], description = descrips[4], distance = 0),
    Relationship(facilities_nodes["hilltop"], "CONNECTED_TO", building_nodes["t22"], description = descrips[6], distance = 0),
    Relationship(food_nodes["macs"], "CONNECTED_TO", facilities_nodes["spec"], description = descrips[6], distance = 0),
    Relationship(building_nodes["t12"], "CONNECTED_TO", building_nodes["t12a"], description = descrips[4], distance = 0),
    Relationship(facilities_nodes["eleven"], "CONNECTED_TO", building_nodes["t11a"], description = descrips[6], distance = 0),
    Relationship(building_nodes["t11c"], "CONNECTED_TO", building_nodes["t11b"], description = descrips[5], distance = 0),
    Relationship(facilities_nodes["sc"], "CONNECTED_TO", food_nodes["fc5"], description = descrips[4], distance = 0),
    Relationship(facilities_nodes["gym"], "CONNECTED_TO", facilities_nodes["sc"], description = descrips[4], distance = 0),
    Relationship(facilities_nodes["mpc"], "CONNECTED_TO", facilities_nodes["mpf"], description = descrips[6], distance = 0),
    Relationship(facilities_nodes["bcourt"], "CONNECTED_TO", facilities_nodes["mpc"], description = descrips[6], distance = 0),
    Relationship(building_nodes["t5"], "CONNECTED_TO", facilities_nodes["spav"], description = descrips[5], distance = 0),
    Relationship(building_nodes["w5"], "CONNECTED_TO", building_nodes["w4"], description = descrips[4], distance = 0)
]

in_same_building_relations = [
    Relationship(food_nodes["fc6"], "IN_SAME_BUILDING", building_nodes["t19"], distance = 0),
    Relationship(food_nodes["fc4"], "IN_SAME_BUILDING", facilities_nodes["aero"], distance = 0),
    Relationship(food_nodes["fc3"], "IN_SAME_BUILDING", facilities_nodes["polyc"], distance = 0),
    Relationship(food_nodes["fc2"], "IN_SAME_BUILDING", building_nodes["t1ac"], distance = 0),
    Relationship(food_nodes["libcafe"], "IN_SAME_BUILDING", facilities_nodes["colours"], distance = 0),
    Relationship(facilities_nodes["mlt8"], "IN_SAME_BUILDING", building_nodes["t19"], distance = 0),
    Relationship(facilities_nodes["mlt9"], "IN_SAME_BUILDING", building_nodes["t19"], distance = 0),
    Relationship(facilities_nodes["mlt10"], "IN_SAME_BUILDING", building_nodes["t19"], distance = 0),
    Relationship(facilities_nodes["mlt11"], "IN_SAME_BUILDING", building_nodes["t19"], distance = 0),
    Relationship(facilities_nodes["mlt12"], "IN_SAME_BUILDING", building_nodes["t21"], distance = 0),
    Relationship(facilities_nodes["spec"], "IN_SAME_BUILDING", building_nodes["t15"], distance = 0), 
    Relationship(facilities_nodes["mainlibex"], "IN_SAME_BUILDING", facilities_nodes["mainlib"], distance = 0)
]

has_parking_lot_relations = [
    Relationship(lot_nodes["a1"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a2"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a3"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a4"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a5"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a6"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a7"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a8"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a9"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a10"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a11"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a12"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a13"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a14"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a15"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a16"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a17"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a18"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a19"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0),
    Relationship(lot_nodes["a20"], "HAS_PARKING_LOT", building_nodes["parking"], distance = 0)
]

held_in_relations = [
    Relationship(event_nodes["smartpoly"], "HELD_IN", building_nodes["t14"])
]

relation_nodes = [walk_relations, connected_to_relations, in_same_building_relations, has_parking_lot_relations, held_in_relations]