import time
import fileinput

def get_graph(lines):
    graph = {}
    for line in lines:
        if line[0] in graph: graph[line[0]].append(line[1])
        else: graph[line[0]] = [line[1]]
        if line[1] in graph: graph[line[1]].append(line[0])
        else: graph[line[1]] = [line[0]]
    return graph

def dfs(node, graph, visited, twice):
    paths = []
    for child in graph[node]:
        if child == "end":
            paths.append(visited + [child])
        elif child.isupper() or (child.islower() and child not in visited):
            paths.extend(dfs(child, graph, visited + [child], twice))
        elif child.islower() and child in visited and not twice:
            paths.extend(dfs(child, graph, visited + [child], True))
    return paths

def part1(lines):
    print(len(dfs("start", get_graph(lines), ["start"], True)))

def part2(lines):
    graph = get_graph(lines)
    for node in graph:
        if "start" in graph[node]: graph[node].remove("start")
    graph.pop("end", None)
    print(len(dfs("start", graph, ["start"], False)))

def main():
    paths = [line.strip().split("-") for line in fileinput.input("./Input/Day12.txt")]
    part1(paths)
    part2(paths)

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))