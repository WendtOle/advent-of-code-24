from itertools import combinations

def main():
    with open("./puzzle.txt", "r") as file:
        lines = file.readlines()
    lines = list(map(lambda line: line.strip(), lines))

    unique_connections = set()
    for network in lines:
        [left, right] = sorted(network.split("-"))
        unique_connections.add(f"{left}-{right}")

    lookup = {}
    for network in unique_connections:
        entries = network.split("-")
        for entry in entries:
            if not entry in lookup:
                lookup[entry] = []
            other_entry = entries[0] if entries[0] != entry else entries[1]
            lookup[entry].append(other_entry)
    #print(lookup)

    networks = unique_connections
    new_networks = None
    while new_networks is None or len(new_networks) > 0 :
        if not (new_networks is None):
            networks = new_networks
        new_networks = set()
        for network in networks:
            parts = network.split("-")
            potential_new_partners = set(lookup[parts[0]])
            for other_entry in parts[1:]:
                potential_new_partners.remove(other_entry)
                potential_new_partners = potential_new_partners.intersection(lookup[other_entry])
            for new_partner in potential_new_partners:
                sorted_partners = sorted([*parts, new_partner])
                new_networks.add("-".join(sorted_partners))
    print(networks, len(networks))



if __name__ == "__main__":
    main()