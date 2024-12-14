def get_total_calibration_result(file_name):
    lines = None
    with open(file_name, 'r') as file:
        lines = file.readlines()
    equations = []
    for line in lines:
        [result_string, items_string] = line.split(": ")
        items = list(map(lambda item: int(item), items_string.split(" ")))
        equations.append([int(result_string), items])
    sum = 0
    for [result, items] in equations:
        if is_equation_solvable(result, items):
            sum += result
    return sum 

def test_get_total_calibration_result():
    assert get_total_calibration_result("./example.txt") == 3749

def is_equation_solvable(result, items):
    return result in get_results(items)

def get_results(items):
    results = set()
    results.add(items[0])
    for item in items[1:]:
        new_result_set = set()
        for result in results:
            new_result_set.add(result + item)
            new_result_set.add(result * item)
        results = new_result_set
    return results

def test_is_equation_solvable():
    assert is_equation_solvable(190, [10,19]) == True
    assert is_equation_solvable(161011, [16,10,13]) == False
    assert is_equation_solvable(3267, [81,40,27]) == True

if __name__ == "__main__":
    print(get_total_calibration_result("./given.txt"))   