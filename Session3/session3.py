def minusduplicate(input_lis):
    outlist = []
    [outlist.append(x) for x in input_lis if x not in outlist]
    return outlist
    

def minusdup(inputlist):
    return list(set(inputlist))