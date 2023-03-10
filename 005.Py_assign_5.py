# 1. What does an empty dictionary's code look like?

Empty dictionary code will look like '{}'


# 2. What is the value of a dictionary value with the key 'foo' and the value 42?

It's value will be {'foo' : 42}


# 3. What is the most significant distinction between a dictionary and a list?

The items stored in a dict are unordered while the items stored in the list are ordered.


# 4. What happens if you try to access spam['foo'] if spam is {'bar':100}?

spam = {'bar':100}
We will get a 'Key-error' as key 'foo' is not defined in spam


# 5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

spam = {"cat":10}
There is no difference. The 'in' operator checks whether a value exists as a key in the dictionary.


# 6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?

'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.


# 7. What is a shortcut for the following code?
    if 'color' not in spam:
        spam['color'] = 'black'

 spam.setdefault('color', 'black')


# 8. How do you &quot;pretty print&quot; dictionary values using which module and function?

pprint.pprint()
