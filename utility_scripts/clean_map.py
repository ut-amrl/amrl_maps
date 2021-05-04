#!/usr/bin/python
import sys
import math

kEpsilon = 0.000001

def Cross(a1, a2, b1, b2):
    return a1 * b2 - a2 * b1

def Dot(a1, a2, b1, b2):
    return a1 * b1 + a2 * b2

def TriangleArea(s1, s2, s3, s4, vx, vy):
    return Cross(vx - s1, vy - s2, s1 - s2, s3 - s4)

def PointColinear(s1, s2, s3, s4, vx, vy):
    area = TriangleArea(s1, s2, s3, s4, vx, vy)
    return math.fabs(area) <= kEpsilon

def CheckColinear(a1, a2, a3, a4, b1, b2, b3, b4):
    first = PointColinear(a1, a2, a3, a4, b1, b2)
    second = PointColinear(a1, a2, a3, a4, b3, b4)
    return first and second

def Within(s1, s2, s3, s4, vx, vy):
    d1 = s3 - s1
    d2 = s4 - s2
    return (Dot(vx - s1, vy - s2, d1, d2) > 0.0 and
            Dot(vx - s3, vy - s4, d1, d2) < 0.0)

def CheckOverlap(a1, a2, a3, a4, b1, b2, b3, b4):
    colinear = CheckColinear(a1, a2, a3, a4, b1, b2, b3, b4)
    return (colinear and
        (Within(a1, a2, a3, a4, b1, b2) or
         Within(a1, a2, a3, a4, b3, b4) or
         Within(b1, b2, b3, b4, a1, a2) or
         Within(b1, b2, b3, b4, a3, a4)))

def Length(l):
   return math.sqrt(pow(l[2] - l[0],2) + pow(l[3] - l[2], 2))

def MergeLines(a1, a2, a3, a4, b1, b2, b3, b4):
    lines = []
    lines.append([a1, a2, a3, a4])
    lines.append([b1, b2, b3, b4])
    lines.append([a1, a2, b1, b2])
    lines.append([a1, a2, b3, b4])
    lines.append([a3, a4, b1, b2])
    lines.append([a3, a4, b3, b4])
    best_length = 0
    best_line = []
    for line in lines:
        current_length = Length(line)
        if current_length > best_length:
            best_line = line
            best_length = current_length
    return best_line

if (len(sys.argv) != 2):
  print(len(sys.argv))
  print("Expects 1 argument: paths to input vector map file")
  raise SystemExit

lines = []
with open(sys.argv[1], 'r') as map:
    for line in map:
        lines.append([float(x) for x in line.split(",")])

new_lines = []
merged = []
# Iterate over the list backwards
for i in range (0, len(lines)):
    c = lines[i]
    if (c in merged):
        continue
    for j in range (i + 1, len(lines)):
        l = lines[j]
        if not l in merged and CheckOverlap(c[0], c[1], c[2], c[3], l[0], l[1], l[2], l[3]):
            print("Merging")
            print(c)
            print(l)
            print("\n")
            c = MergeLines(c[0], c[1], c[2], c[3], l[0], l[1], l[2], l[3])
            merged.append(l)
    new_lines.append(c)

with open("cleaned.txt", 'w') as output:
    for line in new_lines:
        line_str = ','.join([str(x) for x in line])
        output.write(line_str + "\n")

print("Starting Lines: ", len(lines))
print("Final Lines: ", len(new_lines))

