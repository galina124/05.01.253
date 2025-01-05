def calculate_structure_sum(arg):
    sum = 0
    if isinstance(arg, int ):
        sum += arg
    elif isinstance(arg, str):
        sum += len(arg)
    elif isinstance(arg, (list, tuple, set)):
        for el in arg:
            sum += calculate_structure_sum(el)
    elif isinstance(arg, dict):
        for key, value in arg.items():
            sum = sum + calculate_structure_sum(value) + calculate_structure_sum(key)
    return sum

data_structure = [[1,2,3],{'a':4,'b':5},(6,{'cube':7,'drum':8}),'Hello',((),[{(2,'Urban',('Urban2',35))}])]

result = calculate_structure_sum(data_structure)
print(result)