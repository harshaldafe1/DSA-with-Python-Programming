"""
Dictionary in python (dict):

dictionary is collection of key value pair of encloses in {} brackets
keys are unique, values in dict can be access by their keys

Basic Syntax:
note:
dictionary container key value pair seperated by colon ':'
key are defined as string in python, but not in javascript 
in javacript dictionary are called as objects even objects has different properties in js



properties of dict:
dictionary has keys which act like index for perticular values, they are uniques 

an attempt to create pair with same key, result in update old key value

dictionary are no order 



Applications:
Caching: Quickly map memory locations to stored values

Database indexing: Efficiently index tuples for fast retrieval

Pattern matching algorithms: Example: Rabin-Karp

Counting and storing frequencies: Efficient data aggregatio

"""

person = {
    'name': 'harshal',
    'age': 22,
    'place': 'Achalpur',
    'profession': 'AI trainer'
}

# print(f'dict = {person}')

for i in person: # list of keys
    print(i)