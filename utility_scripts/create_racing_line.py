import json

graph = {"edges": [], "nodes": []}
points = [(10.0, 0.5), (20.7, 0.8), (21.2, 1.7), (22, 3.7), (21.4, 6.8), (20.4, 7.5), (19.75, 7.1), (19.4, 6.3), (20, 4.6), (20.1, 3.5), (19.3, 2.7), (17.9, 2.0), (11.8, 1.5), (11, 1.9), (10.7, 2.3), (10.9, 2.8), (11.5, 3.2), (17.4, 3.9), (18.1, 4.9), (17.9, 5.6), (17.5, 5.9), (16.6, 5.8), (15, 5.3), (1.3, 6.5), (0.75, 6), (0.8, 5.2), (1.2, 3.3), (1.6, 2.6), (2.7, 2.3), (7.5, 2.1), (8.9, 0.8)]

id_ct = 0
for p in points:
    graph["nodes"].append({"id": id_ct, "loc": {"x": p[0], "y": p[1]}})
    id_ct += 1

for i in range(len(graph["nodes"]) - 1):
    graph["edges"].append({
        "has_automated_door": False,
        "has_door": False,
        "has_elevator": False,
        "has_stairs": False,
        "max_clearance": 10.0,
        "max_speed": 50.0,
        "s0_id": graph["nodes"][i]["id"],
        "s1_id": graph["nodes"][i+1]["id"],
    })

if len(graph["nodes"]) > 1:
    graph["edges"].append({
        "has_automated_door": False,
        "has_door": False,
        "has_elevator": False,
        "has_stairs": False,
        "max_clearance": 10.0,
        "max_speed": 50.0,
        "s0_id": graph["nodes"][len(graph["nodes"])-1]["id"],
        "s1_id": graph["nodes"][0]["id"],
    })

print(json.dumps(graph, indent=4))
