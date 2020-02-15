'''Implement a function to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not
become smaller than the original string, your method should return the original string. You
can assume the string has only uppercase and lowercase letters (a - z).'''

from collections import Counter

def compress(string):
    words = Counter(string).keys()
    count = Counter(string).values()

    combine = zip(words,count)
    compressed = [w + str(c) for w,c in combine]
    #compressed = "".join(compressed)

    if len(compressed) > len(string):
        print("this string cannot be compressed")
        return string
    
    return compressed


def long_compress(string):
    pair = {}
    word = []
    c = 0

    indiv = [char for char in string]

    '''for char in indiv:
        if char not in word:
            c = 0
            word.append(char)'''
        
    """for count,char in enumerate(indiv):
        c += 1
        if count <= len(indiv):
            if indiv[] == indiv[count+1]:
                print(char)"""

    for i in range(0,len(indiv)):
        if indiv[i] == indiv[i-1]:
            print(indiv[i])

    
    
long_compress("aaabbccccaaad")