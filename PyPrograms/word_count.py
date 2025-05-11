
from index import strindex,sp_ind

#name = "I am the storm that is approaching, the darkness that encroaches the very essence of humanity"

name = input("Enter the sentence: ")

strindex(name)

if len(sp_ind) == 1:
    print('There is only one continuous string with no delimiters')
    exit
else:
    pass

word_list = []

j = 0
for num in sp_ind:
    val = num
    word = name[j:val]
    if word in word_list:
        pass
    else:
        print(word, 'occurs: ',name.count(word),'times')

    word_list.append(word)
    j = val+1


