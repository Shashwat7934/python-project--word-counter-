string=input("enter the line:")
def word_count(str):
    dict={}
    words=str.split()
    for word in words:

        if word in dict:
            dict[word] +=1
        else:
            dict[word]=1
    return dict

print(word_count(string))



