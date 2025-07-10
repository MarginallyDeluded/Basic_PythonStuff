
string = input('Enter any string of words to count all the vowels in it: ')

def count_vow(string):
    count = 0;

    for alpha in string:
        if alpha == 'a' or alpha=='e' or alpha=='i' or alpha=='o' or alpha=='u':
            if alpha.upper()==alpha:
                count +=1
            else:
                count = count+1
    return count

vowels = f'There are {count_vow(string)} vowels in {string}'
print(vowels)

#print(help(str))
