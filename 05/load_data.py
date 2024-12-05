def load_data(file_name):
    rules = []
    updates = []
    with open(file_name, 'r') as file:
        lines = file.readlines()
    for line in lines:
        if "|" in line:
            rules.append(list(map(lambda item: int(item), line.split("|"))))
        if "," in line:
            updates.append(list(map(lambda item: int(item), line.split(","))))
    return {"rules": rules, "updates": updates}

def check_all_updates(updates, rules): 
    sum = 0
    for update in updates:
        if satisfies_rules(update, rules):
            middle_index = int(len(update)/2)
            sum += update[middle_index]
    return sum

def get_sum_of_corrected(updates, rules):
    sum = 0
    for update in get_incorrectly_ordered_updates(updates, rules):
        middle_index = int(len(update)/2)
        fixed = fix_update(update, rules)
        sum += fixed[middle_index]
    return sum

def get_incorrectly_ordered_updates(updates,rules):
    list = []
    for update in updates:
        if not satisfies_rules(update, rules):
            list.append(update)  
    return list

from functools import cmp_to_key

def fix_update(update, rules): 
    def sort_by_rules(left, right):
        for rule in rules:
            if left in rule and right in rule:
                if left == rule[0]:
                    return -1
                else:
                    return 1
        return 0
    return sorted(update, key=cmp_to_key(sort_by_rules))

def satisfies_rules(update, rules):
    for rule in rules:
        [left, right] = rule
        if left in update and right in update:
            if not satiesfies_rule(update, rule):
                return False
    return True

def satiesfies_rule(update, rule):
    [left, right] = rule
    return update.index(left) < update.index(right)

if __name__ == "__main__":
    data = load_data("./puzzle-input.txt")
    print(check_all_updates(data["updates"], data["rules"]))
    print(get_sum_of_corrected(data["updates"], data["rules"]))