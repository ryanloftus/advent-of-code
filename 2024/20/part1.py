from heapq import *

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def parse_input():
    with open("input.txt") as f:
        return [[c for c in line] for line in f.read().splitlines()]

def find_node(track, target):
    for i in range(len(track)):
        for j in range(len(track[i])):
            if track[i][j] == target:
                return (i, j)
            
def djikstra(track, si, sj):
    dist = [[None] * len(row) for row in track]
    pq = [(0, si, sj)]
    while pq:
        d, i, j = heappop(pq)
        if i < 0 or i >= len(track) or j < 0 or j >= len(track[i]) or track[i][j] == "#":
            continue
        if dist[i][j] is None:
            dist[i][j] = d
            heappush(pq, (d+1, i-1, j))
            heappush(pq, (d+1, i+1, j))
            heappush(pq, (d+1, i, j-1))
            heappush(pq, (d+1, i, j+1))
    return dist

def count_effective_cheats(track, min_saved_time):
    effective_cheats = set()

    si, sj = find_node(track, "S")
    dist_from_s = djikstra(track, si, sj)

    ei, ej = find_node(track, "E")
    dist_from_e = djikstra(track, ei, ej)

    target_time = dist_from_s[ei][ej] - min_saved_time

    for i in range(len(track)):
        for j in range(len(track[i])):
            for entry_dir in DIRS:
                cheat_start_i = i + entry_dir[0]
                cheat_start_j = j + entry_dir[1]

                if cheat_start_i < 0 or cheat_start_i >= len(track) or cheat_start_j < 0 or cheat_start_j >= len(track[i]):
                    continue

                time_to_entry = dist_from_s[cheat_start_i][cheat_start_j]
                if time_to_entry is None:
                    continue
                for exit_dir in DIRS:
                    if entry_dir == exit_dir:
                        continue
                    
                    cheat_end_i = i + exit_dir[0]
                    cheat_end_j = j + exit_dir[1]

                    if cheat_end_i < 0 or cheat_end_i >= len(track) or cheat_end_j < 0 or cheat_end_j >= len(track[i]):
                        continue

                    time_from_exit = dist_from_e[cheat_end_i][cheat_end_j]
                    if time_from_exit is None:
                        continue
                    if time_to_entry + 2 + time_from_exit <= target_time:
                        effective_cheats.add((cheat_start_i, cheat_start_j, cheat_end_i, cheat_end_j))
    
    return len(effective_cheats)

def solution():
    track = parse_input()
    num_effective_cheats = count_effective_cheats(track, 100)
    print(num_effective_cheats)

if __name__ == "__main__":
    solution()
