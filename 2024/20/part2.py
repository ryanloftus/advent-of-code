from heapq import *

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
CHEAT_MAX_DURATION = 20

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

    for cheat_start_i in range(len(track)):
        for cheat_start_j in range(len(track[cheat_start_i])):
            time_to_entry = dist_from_s[cheat_start_i][cheat_start_j]
            if time_to_entry is None or time_to_entry + 2 > target_time:
                continue

            for cheat_end_i in range(len(track)):
                for cheat_end_j in range(len(track[cheat_end_i])):
                    cheat_time = abs(cheat_start_i-cheat_end_i) + abs(cheat_start_j-cheat_end_j)
                    time_from_exit = dist_from_e[cheat_end_i][cheat_end_j]
                    if cheat_time > CHEAT_MAX_DURATION or time_from_exit is None:
                        continue

                    time = time_to_entry + cheat_time + time_from_exit
                    if time <= target_time:
                        effective_cheats.add((cheat_start_i, cheat_start_j, cheat_end_i, cheat_end_j))
    
    return len(effective_cheats)

def solution():
    track = parse_input()
    num_effective_cheats = count_effective_cheats(track, 100)
    print(num_effective_cheats)

if __name__ == "__main__":
    solution()
