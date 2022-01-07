'''
A sequence of five words is called magical if the i^{th}ith word is a substring of the (i + 1)^{th}(i+1)th
word for every ii in the range 1 \leq i < 51≤i<5. Accept a sequence of five words as input, one word on each line. Print magical if the sequence is magical and non-magical otherwise.
Note that str_1 is a substring of str_2 if and only if str_1 is present as a sequence of consecutive characters in str_2.
'''

word1 = input()
word2 = input()
word3 = input()
word4 = input()
word5 = input()

flag = False
if word1 in word2:
    flag = True
    if word2 in word3:
        if word3 in word4:
            flag = True
            if word4 in word5:
                flag = True
            else:
                flag = False
        else:
            flag = False
    else:
        flag = False
else:
    flag = False
    
if flag == True:
    print("magical")
else:
    print("non-magical")
    