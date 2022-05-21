"""

THIS SCRIPT IS NO LONGER VALID! GRAPH NAVIGATION NOW USES THE DESCRIPTOR FILE DIRECTLY,
AND THE FORMAT OF THE DESCRIPTOR FILE HAS CHANGED. SEE THE README FOR UPDATED INSTRUCTIONS.

This script creates a .navigation.json file for a map given a racing line description.
The description of the racing line is a text file where each line is a point on the racing
line and contains information about max speed on the upcoming segment. 

The following example racing line means from (1, 2) to (4, 5) the speed limit is 3, from
(4, 5) to (7, 8) the speed limit is 1, and from (7, 8) to (1, 2) the speed limit is 2.

Example:
1 2 3
4 5 1
7 8 2

To use this script run `python create_racing_line <racing_line_file> > <.navigation.json_file>`
"""
import json
import sys

if len(sys.argv) != 2:
    sys.stderr.write("Provide the filename of the racing line descriptor")

with open(sys.argv[1]) as f:
    lines = [line.split() for line in f.readlines()]
    points = [(float(x), float(y)) for x, y, _ in lines]
    speeds = [float(s) for _, _, s in lines]

graph = {"edges": [], "nodes": []}

for p in points:
    graph["nodes"].append({"id": len(graph["nodes"]), "loc": {"x": p[0], "y": p[1]}})

for i in range(len(graph["nodes"]) - 1):
    graph["edges"].append({
        "has_automated_door": False,
        "has_door": False,
        "has_elevator": False,
        "has_stairs": False,
        "max_clearance": 10.0,
        "max_speed": speeds[i],
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
        "max_speed": speeds[len(graph["nodes"])-1],
        "s0_id": graph["nodes"][len(graph["nodes"])-1]["id"],
        "s1_id": graph["nodes"][0]["id"],
    })

print(json.dumps(graph, indent=4))
