#Problem_2
def factorial(num):
    factorial=1
    while num>0:
        factorial=factorial*num
        num=num-1
    return factorial

#Problem_3
def prime(num):
    factors=0
    divisor=1
    while divisor<int(num**0.5):
        if num%divisor==0:
            return False
        divisor+=1
    return True

#Problem_5
def isPalindrome(phrase):
    length=1+len(phrase)
    rev_phrase=""
    for c in range(1,length,1):
        rev_phrase+=phrase[-c]
    if phrase==rev_phrase:
        return True
    else: return False

#Problem_6
def isSubstring(phrase_1,phrase_2):
     length_1=len(phrase_1)
     length_2=len(phrase_2)
     for c in range(length_1,1):
         for n in range(length_2,1):
             if c==n:
                 return True
             else: return False   
