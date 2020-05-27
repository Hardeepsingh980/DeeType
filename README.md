## DeeType
# A python package to classify data types from a list.

This package can help you sort the different types of data in a list. 
For example :-
You make a list [1,"Hello",True,[0,8],{"name":"Hardeep"}]
You want to extract all the string, ints, bools, lists or dicts from it into different lists.

the code for that would be :- 

```
from DeeType import DeeType

deetype_obj = DeeType([1,"Hello",True,[0,8],{"name":"Hardeep"}])

# for strings
print(deetype_obj.findStr())
## Output :- ["Hello"]

# for integers
print(deetype_obj.findInt())
## Output :- [1]

# for list
print(deetype_obj.findList())
## Output :- [[0,8]]

# for dict
print(deetype_obj.findDict())
## Output :- [{"name":"Hardeep"}]

# for all datatypes
print(deetype_obj.showTypeDict())
## Output :- {
                'strings': ['Hello'],
                'integers': [1],
                'booleans': [True],
                'lists': [[0, 8]],
                'dicts': [{'name': 'Hardeep'}]
             }
```

Consider Giving a star on our github repo.

