string=input("enter the line:")  #taking input o a paragraph 
def word_count(str):       #defining a function that counts number of word
    dict={}           #creating a empty dictionary in which we store the number of occurerence of a particular word
    words=str.split()   #spliting the words from string
    for word in words:

        if word in dict:
            dict[word] +=1  #condition applied if a word is already present then change the value from +1
        else:
            dict[word]=1    #else the occurence of word i 1
    return dict

print(word_count(string))   #print



