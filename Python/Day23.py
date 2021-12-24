import time
from functools import lru_cache

room_spots = (2, 4, 6, 8)
hallway_spots = (0, 1, 3, 5, 7, 9, 10)
availible_destinations = {"A": 0, "B": 1, "C": 2, "D": 3}
energy = {"A": 1, "B": 10, "C": 100, "D": 1000}

@lru_cache(maxsize=None) # If two paths have the same energy_usage, they are the same path
def solve(hallway, rooms, room_size):
    least_energy = 99999999
    
    # if goal is reached
    if rooms == (("A",) * room_size, ("B",) * room_size, ("C",) * room_size, ("D",) * room_size): return 0

    # move from hallway into room
    for i, square in enumerate(hallway):
        if square is None: continue
        destination = availible_destinations[square]

        # check if there is already a amphipod not of the same type in the room
        can_move = True
        for amphipod in rooms[destination]:
            if amphipod is not None and amphipod != square:
                can_move = False
                break
        if not can_move: continue

        # check if the hallway squares on the path are blocked
        offset = 1 if room_spots[destination] > i else -1
        for j in range(i + offset, room_spots[destination] + offset, offset):
            if hallway[j] is not None:
                can_move = False
                break
        if not can_move: continue

        # move into room
        none_count = sum(elem is None for elem in rooms[destination])
        new_room = (None,) * (none_count - 1) + (square,) * (room_size - none_count + 1)
        steps = none_count + abs(i - room_spots[destination])
        energy_usage = steps * energy[square]
        result = solve(hallway[:i] + (None,) + hallway[i+1:], rooms[:destination] + (new_room,) + rooms[destination+1:], room_size)
        if energy_usage + result < least_energy: least_energy = energy_usage + result
        
    # move from room into hallway
    for i, room in enumerate(rooms):
        # check if there is already a amphipod not of the same type in the room
        can_move = False
        for amphipod in room:
            if amphipod is not None and availible_destinations[amphipod] != i:
                can_move = True
                break
        if not can_move: continue

        # check if the room squares on the path are blocked
        none_count = sum(elem is None for elem in room)
        steps = none_count + 1
        square = room[none_count]

        # check move into hallway
        for hallway_spot in hallway_spots:
            availible_destinations_steps = steps + abs(hallway_spot - room_spots[i])
            availible_destinations_energy_usage = availible_destinations_steps * energy[square]

            # check if the hallway squares on the path are blocked
            blocked = False
            for j in range(min(hallway_spot, room_spots[i]), max(hallway_spot, room_spots[i]) + 1):
                if hallway[j] is not None:
                    blocked = True
                    break
            if blocked: continue

            # move into hallway
            new_room = (None,) * (none_count + 1) + room[none_count+1:]
            result = solve(hallway[:hallway_spot] + (square,) + hallway[hallway_spot+1:], rooms[:i] + (new_room,) + rooms[i+1:], room_size)
            if availible_destinations_energy_usage + result < least_energy: least_energy = availible_destinations_energy_usage + result

    return least_energy

def part1(burrows, startings):
    return solve(burrows, startings, 2)

def part2(burrows, startings):
    return solve(burrows, startings, 4)

def main():
    burrows = tuple(None for _ in range(len(room_spots) + len(hallway_spots)))
    print(part1(burrows, (("D", "C"), ("B", "A"), ("A", "D"), ("C", "B"))))
    # print(part2(burrows, (("D", "D", "D", "C"), ("B", "C", "B", "A"), ("A", "B", "A", "D"), ("C", "A", "C", "B"))))
    print(part2(burrows, (("B", "D", "D", "D"), ("B", "C", "B", "A"), ("C", "B", "A", "A"), ("D", "A", "C", "C"))))

if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))