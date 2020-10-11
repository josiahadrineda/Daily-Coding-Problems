def find_path(dir):
    #Base case
    if "." not in dir:
        return 0
    
    #Convert str to list
    dir = dir.replace('\n', ' ')
    dir_list = list(dir.split(' '))

    #Find all files and their respective depths and indices
    file_list = []
    for dir in dir_list:
        if '.' in dir:
            cnt = dir.count('\t')
            ind = dir_list.index(dir)
            file_list.append((dir[(2*cnt) - cnt:], cnt, ind))
    
    #Generate paths for all files
    res = []
    for file, cnt, ind in file_list:
        res.append(generate_path(dir_list, file, cnt, ind))

    #Return max path
    sol = max(res)
    return "\nLongest Absolute Path: {}\nNumber of Characters: {}".format(sol, len(sol))

def generate_path(dir_list, file, cnt, ind):
    temp = []

    while ind >= 0:
        if dir_list[ind].count('\t') == cnt:
            temp.append(dir_list[ind][(2*cnt) - cnt:])
            cnt -= 1
        ind -= 1

    s = '/'.join(temp[::-1])
    return s

#Driver code
dir = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(dir)
print(find_path(dir))