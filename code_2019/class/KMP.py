def get_next(partern_str):
    next_list=[]
    next_list.append(-1)
    k=-1
    j = 0
    #import pdb;pdb.set_trace()
    while j < len(partern_str)-1:
        if k==-1 or partern_str[j]==partern_str[k]:
            j+=1
            k+=1
            if partern_str[j]!=partern_str[k]:
                next_list.append(k)
            else:
                next_list.append((next_list[k]))
        else:
            k = next_list[k]

    return next_list


def KMP(target,pattern):
    next_list = get_next(partern)
    print(next_list)
    i = 0
    j = 0
    while i<len(target) and j<len(pattern):
        if j==-1 or target[i] == pattern[j]:
            j+=1
            i+=1
        else:
            j = next_list[j]
    if j == len(pattern):
        return i-jvi
    else:
        return -1



print(get_next('abcde'))
