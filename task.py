
def combiner(a):
    nums = []
    strings = []
    for i in a:
        if isinstance(i, str):
            strings.append(i)
        elif isinstance(i, (int, float)):
            nums.append(i)
    
    str_comb = "".join(strings)
    num_comb = sum(nums)
    
    all_comb = str_comb + str(num_comb)
    print(all_comb)

#combiner(["Jonas", 6.7, "Petras", 10])



def combiner(a):
    x = ""
    y = 0
    for i in a:
        if isinstance(i,str):
            x += i
        elif isinstance(i, (int, float)):
            y += i
    x += str(y)
    return x

combiner(["Jonas", 6.7, "Petras", 10])'''
