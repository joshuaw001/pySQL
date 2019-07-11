import random
global _keys = range(10000,99999,1)
def encode(_dbf,code,key):
    if key in _keys:
def letter_to_number(letters):   
    letters = letters.lower()
    dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    strlen = len(letters)
    if strlen == 1:
        number = dictionary[letters]
    elif strlen == 2:
        first_letter = letters[0]
        first_number = dictionary[first_letter]
        second_letter = letters[1]
        second_number = dictionary[second_letter]
        number = (first_number * 26) + second_number
    elif strlen == 3:
        first_letter = letters[0]
        first_number = dictionary[first_letter]
        second_letter = letters[1]
        second_number = dictionary[second_letter]
        third_letter = letters[2]
        third_number = dictionary[third_letter]
        number = (first_number * 26 * 26) + (second_number * 26) + third_number
    return number
