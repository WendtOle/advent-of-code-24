from load_data import load_data, satiesfies_rule, check_all_updates,get_incorrectly_ordered_updates, fix_update

def test_load_data():
    assert load_data("./dummy-input.txt") == {'rules': [[45, 43]], 'updates': [[43, 45]]}

def test_rule_checking():
    assert satiesfies_rule([34,45], [34,45]) == True
    assert satiesfies_rule([34,45], [45,34]) == False

def test_given_dummy_input():
    data = load_data("./given_dummy_input.txt")
    assert check_all_updates(data["updates"], data["rules"]) == 143

def test_get_incorrectly_ordered():
    data = load_data("./given_dummy_input.txt")
    assert get_incorrectly_ordered_updates(data["updates"], data["rules"]) == [[75,97,47,61,53],[61,13,29],[97,13,75,29,47]]

def test_fix_update_1():
    data = load_data("./given_dummy_input.txt")
    assert fix_update([75,97,47,61,53], data["rules"]) == [97,75,47,61,53]

def test_fix_update_2():
    data = load_data("./given_dummy_input.txt")
    assert fix_update([61,13,29], data["rules"]) == [61,29,13]

def test_fix_update_3():
    data = load_data("./given_dummy_input.txt")
    assert fix_update([97,13,75,29,47], data["rules"]) == [97,75,47,29,13]