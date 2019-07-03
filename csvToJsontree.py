#-*-coding:utf-8
import csv
from collections import defaultdict

def ctree():
    return defaultdict(ctree)

def build_leaf(name, leaf, key, depth):
    res = {key : name}
    depth += 1

    if len(leaf.keys()) > 0:
        if depth <2:
            first_res = [build_leaf(k, v, "city", depth) for k, v in leaf.items()]
            res["cities"] = first_res
        if depth >= 2:
            second_res = [build_leaf(k, v, "town", depth) for k, v in leaf.items()]
            res["towns"] = second_res
            

    return res


def main():
    tree = ctree()
    with open('data.csv', encoding="UTF8") as csvfile:
        reader = csv.reader(csvfile)
        for rid, row in enumerate(reader):

            if rid == 0:
                continue

            leaf = tree[row[0]]
            for cid in range(1, len(row)):
                leaf = leaf[row[cid]]

    res = []
    for name, leaf in tree.items():
        res.append(build_leaf(name, leaf, "province", depth=0))

    import json
    with open('location_data1.json','w',encoding="UTF8") as file:
        file.write(json.dumps(res, ensure_ascii = False))

main()
