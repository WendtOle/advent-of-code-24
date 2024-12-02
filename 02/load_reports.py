def load_reports(file_name): 
    with open(file_name, 'r') as file:
        lines = file.readlines()

    reports = []
    for line in lines:
        splitted = line.strip().split()
        reports.append([ int(x) for x in splitted])
    
    return reports