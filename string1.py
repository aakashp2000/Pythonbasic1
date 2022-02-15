#Append new string in the middle of a given string
def append_middle(s1,s2):
    print("Original Strings are",s1,s2)
    mi=int(len(s1)/2)
    x=s1[:mi:]
    #concatenate s2 to it
    x=x+s2
    #append remaining character from s1
    x=x+s1[mi:]
    print("After appending new string in middle:",x)
append_middle("Ault","Kelly")
