from evaluate_report import is_safe, evaluate_reports, is_save_with_single_removed_level, evaluate_reports_with_single_removed_level

def test_is_safe_with_report_01():
    assert(is_safe([7,6,4,2,1])) == True

def test_is_safe_with_report_02():
    assert(is_safe([1,2,7,8,9])) == False

def test_is_safe_with_report_03():
    assert(is_safe([9,7,6,2,1])) == False

def test_is_safe_with_report_04():
    assert(is_safe([1,3,2,4,5])) == False

def test_is_safe_with_report_05():
    assert(is_safe([8,6,4,4,1])) == False

def test_is_safe_with_report_06():
    assert(is_safe([1,3,6,7,9])) == True

def test_is_safe02_with_report_01():
    assert(is_save_with_single_removed_level([7,6,4,2,1])) == True

def test_is_safe02_with_report_02():
    assert(is_save_with_single_removed_level([1,2,7,8,9])) == False

def test_is_safe02_with_report_03():
    assert(is_save_with_single_removed_level([9,7,6,2,1])) == False

def test_is_safe02_with_report_04():
    assert(is_save_with_single_removed_level([1,3,2,4,5])) == True # this one is not obvious

def test_is_safe02_with_report_05():
    assert(is_save_with_single_removed_level([8,6,4,4,1])) == True

def test_is_safe02_with_report_06():
    assert(is_save_with_single_removed_level([1,3,6,7,9])) == True

def test_is_safe_with_report_evaluate_reports():
    assert(evaluate_reports([[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]])) == 2

def test_is_safe02_with_report_evaluate_reports():
    assert(evaluate_reports_with_single_removed_level([[7,6,4,2,1],[1,2,7,8,9],[9,7,6,2,1],[1,3,2,4,5],[8,6,4,4,1],[1,3,6,7,9]])) == 4
