from itertools import combinations

def main():
    with open("./puzzle.txt", "r") as file:
        lines = file.readlines()
    lines = list(map(lambda line: line.strip(), lines))
    lookup = {}
    with_target = set()
    for connection in lines:
        entries = connection.split("-")
        entries.sort()
        [left, right] = entries
        for entry in entries:
            if not entry in lookup:
                lookup[entry] = []
            lookup[entry].append({left, right})
        if left.startswith("t") or right.startswith("t"):
            with_target.add(f"{left}-{right}")
    print(with_target, len(with_target))

    tuples_of_three_with_target = set()

    for tuple in with_target:
        [left, right] = tuple.split("-")
        potential_partners = []
        for entry_tuple in lookup[left]:
            [first, second] = entry_tuple
            potential_partners.append(first if first != left else second)
        for entry_tuple in lookup[right]:
            [first, second] = entry_tuple
            to_compare = first if first != right else second
            if to_compare in potential_partners:
                array = [left, right, to_compare]
                array.sort()
                [start, middle, end] = array
                tuples_of_three_with_target.add(f"{start}-{middle}-{end}")
    print(tuples_of_three_with_target, len(tuples_of_three_with_target))

if __name__ == "__main__":
    main()