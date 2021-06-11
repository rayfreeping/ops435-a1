#! /usr/bin/env python3
'''docstring for this module
   functions for lab4c
   '''

def create_dictionary(keys, values):
    '''this function return a dictionay data object using
       two lists with equal number of items.
       the items in the first list will be used as the keys,
       and the items in the second list will be used as the values
       for the dictionay data object and return to the caller.
    '''
    count = 0
    dictionary = {}
    while count < len(keys):
        dictionary[keys[count]] = values[count]
        count += 1
    return dictionary

if __name__ == '__main__':
    keys_data = ['a','b']
    values_data = [1,2]
    d = create_dictionary(keys_data,values_data)
    print('new dict:',d)
