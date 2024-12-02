from load_reports import load_reports

def is_valid_step_width(last, next): 
    actual = abs(last - next) 
    return actual <= 3 and actual >= 1

def get_direction(left, right):
    if left - right < 0:
        return "INC"
    return "DEC"
    

def is_valid_direction(second_last, last, next):
    if last == next:
        return False
    previous_direction = get_direction(second_last, last)
    current_direction = get_direction(last, next)
    return previous_direction == current_direction
    

def is_valid_step(second_last, last, next): 
    if second_last == None and last == None:
        return True
    if second_last == None and last != None:
        return is_valid_step_width(last, next)
    return is_valid_direction(second_last, last, next) and is_valid_step_width(last, next)
    
    

def is_safe(report):
    for i, level in enumerate(report):
        second_last = None if i - 2 < 0 else report[i - 2]
        last = None if i - 1 < 0 else report[i - 1]
        if not is_valid_step(second_last, last, level):
            return False
    return True

def is_save_with_single_removed_level(report):
    if is_safe(report):
        return True
    for i,x in enumerate(report):
        if i + 1 > len(report):
            return False
        new_report = report[:i] + report[i + 1:]
        if (is_safe(new_report)):
            return True
    return False
            
def evaluate_reports(reports):
    safe_counter = 0
    for report in reports:
        if is_safe(report):
            safe_counter += 1
    return safe_counter

def evaluate_reports_with_single_removed_level(reports):
    safe_counter = 0
    for report in reports:
        if is_save_with_single_removed_level(report):
            safe_counter += 1
    return safe_counter

if __name__ == "__main__":
    reports = load_reports("./puzzle-input.txt")
    print(evaluate_reports(reports))
    print(evaluate_reports_with_single_removed_level(reports))