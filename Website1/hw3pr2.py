# CS 5 Gold, hw3pr2
# Filename: hw3pr2.py
# Name: Shruthi Sukir (w/Michael Guzman)
# Problem Description: Sorting out Caesar!

#Function #1: Encipher(S,n)
def rot(c,n):
    """rotates c (a single character) by n spots in the alphabet
    """
    if 'a' <= c <= 'z':
        if ord(c) + n <= ord('z'):
            return chr(ord(c) + n)
        else:
            return chr (ord(c) + n - 26)
    elif 'A' <= c <= 'Z':
        if ord(c) + n <= ord ('Z'):
            return chr(ord(c) + n)
        else:
            return chr(ord(c) + n - 26)
    else:
        return(c)

def list_to_str( L ):
    """ L must be a list of characters; then, this returns a single string from them
    """
    if len(L) == 0: return ''
    return L[0] + list_to_str(L[1:])

def encipher(S,n):
    """takes in an input string S and a non-negative integer n (0-25). Encipher returns a new string in which the letters in S have been "rotated"/encoded n characters forward in the alphabet.
    """
    L = list(S)
    L = [rot(c,n) for c in L]
    return list_to_str(L)

#Function #2: Decipher(S)
#letterscore
def letterScore(let):
    """letterScore returns the scrabble score of the given letter (string)
    """
    if let in 'aeilnorstu':
        return 1
    elif let in 'dg':
        return 2
    elif let in 'bcmp':
        return 3
    elif let in 'fhvwy':
        return 4
    elif let in 'k':
        return 5
    elif let in 'jx':
        return 8
    elif let in 'qz':
        return 10
    else:
        return 0

#scrabbleScore
def scrabbleScore(S):
    """scrabbleScore inputs a string and outputs the scrabble score (int) of the string
    """
    if S != '':
        return letterScore(S[0]) + scrabbleScore(S[1:])
    else:
        return 0

#decipher
def decipher(S):
    """ takes in a string and outputs a "translation"/decodes the input into the most "English" string
    """
    L = [encipher(S,n) for n in range(26)]
    LoL = [[scrabbleScore(x), x] for x in L ]

    bestpair = min(LoL)
    return bestpair[1]

#decipher2 (just for fun)
def decipher2(S):
    """ takes in a string and outputs a "translation"/decodes the input into the most "English" string
    """
    L = [encipher(S,n) for n in range(26)]
    LoL = [[letProbSum(x), x] for x in L ]

    bestpair = max(LoL)
    return bestpair[1]

#Function #3: blsort(L)

#count
def count(e,L):
    """counts the number of times e appears in L
    """
    LC = [1 for x in L if e==x]
    return sum (LC)

#blsort
def blsort(L):
    """takes in a list L and outputs a list with the same elements at L but in ascending order
    """
    return [0]*count(0,L) + [1]*count(1,L)

#Function #4: gensort(L)
def remOne( e, L ):
    """ returns seq. L with one e rmoved
    """
    if  len(L) == 0:
        return L
        
    elif  L[0] != e:
        return  L[0:1] + remOne( e, L[1:] )

    else:
        return  L[1:]

def gensort(L):
    """takes in a list L and outputs a list with the same elements in ascending order
    """
    if len(L) == 0:
        return L
    else:
        return [min(L)] + gensort(remOne(min(L),L))
    
#Function 5: jscore(S,T)
def jscore(S,T):
    """inputs two strings, returns the number of letters the two strings have in common
    """
    if len(S) == 0:
        return 0
    elif S[0] in T:
        return jscore(S[1:], remOne(S[0],T)) + 1
    else:
        return jscore(S[1:],T)

#Function #6: exact_change(target_amount, L)
def exact_change(target_amount, L):
    """ inputs a single non-negative integer target_amount and a list of positive integer values L. exact_change returns True if it's possible to create target_amount by adding up some or all of the values in L
    """
        
    if target_amount < 0:
        return False
    elif target_amount == 0:
        return True
    elif len(L) == 0:
        return False

    loseit = exact_change (target_amount, L[1:])
    useit = exact_change(target_amount - L[0], L[1:])

    return useit or loseit

#Function #7: LCS(S,T)
def LCS (S,T):
    """inputs two strings S and T and outputs the longest common subsequence (LCS) that S and T share.
    """

    if len(S) == 0:
        return ''
    elif len(T) == 0:
        return ''
    elif S[0] == T[0]:
        return S[0] + LCS(S[1:],T[1:])
    else:
        result1 = LCS(S[1:],T)
        result2 = LCS(S,T[1:])

        if len(result1) > len(result2):
            return result1
        else:
            return result2