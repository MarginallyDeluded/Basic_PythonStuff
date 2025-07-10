
sp_ind = list()

def strindex(string):
    i = 0
    count = 0
    for i,char in enumerate(string):
        if char == ' ':
            sp_ind.append(i)
        i = i+1



