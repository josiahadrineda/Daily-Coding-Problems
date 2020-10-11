def order_courses_w_prereqs(courses):
    res = []
    is_cycle = 0
    visited = {}
    for course in courses:
        visited[course] = 0

    for course in courses:
        if is_cycle:
            return None
        elif not visited[course]:
            res, is_cycle = topological_sort(courses, course, res, is_cycle, visited)
    
    return res

def topological_sort(courses, course, res, is_cycle, visited):
    if visited[course] == 1:
        is_cycle = 1
    elif not visited[course]: # visited[course] could be 0 or 2, allow only 0s
        visited[course] = 1
        for neighbor in courses[course]:
            res, is_cycle = topological_sort(courses, neighbor, res, is_cycle, visited)

        visited[course] = 2
        res.append(course)

    return res, is_cycle

courses = {'CSC300':['CSC100','CSC200'],
           'CSC200':['CSC100'],
           'CSC100':[]}
assert order_courses_w_prereqs(courses) == ['CSC100','CSC200','CSC300']

courses = {'CSC300':['CSC100','CSC200'],
           'CSC200':['CSC100'],
           'CSC100':['CSC300']}
assert order_courses_w_prereqs(courses) == None