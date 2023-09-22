# Exercises (Modify this file)

Answer and complete the following exercises.

## Python Standard Library

1. How you name functions and member functions matter. Take a look at the [dictionary](https://docs.python.org/3/library/stdtypes.html#typesmapping) 
and [list](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range) member functions in the SL. 
Do the names of the member functions correlate to what they do? That is, are they good 'verbs' where the name of the function describes the action the code is doing? A good example would be a function called 'pop' which only removes one element. A bad example would be a function called 'pop' where one element is removed **and** that value is returned. A better name would be 'popAndGet' or 'popAndReturn', which captures the two events happening.

*In my opinion, names of functions in SL does not fully describes the functionalities of the function. For example, list.pop(index) removes the item at the given index and returns the value. It should be renamed as list.popAndGet(index)
Same thing in dict package. dict.pop(key)removes the item with the specified key and returns its value. A better name for this one can be dict.popAndGet(key)*

2. How does a dictionary differ from a list? (i.e. What is the underlying data structure of each container.)

*The underlying data structure for dictionary is a hash table, while for list, the underlying data structure is an array that is dynamically sized.*

3. Does a list allow for random access? Meaning can I access any element(e.g. myList[7])?

*Yes*

4. Observe that all the container data structures (i.e. list, set, dictionary, etc.) can work with any data type (integers, floats, custom data types, etc.). 
What do you think are the pros/cons of a library that can work with any data type?

*Pros: (1) easy to use (2) provide generality*

*Cons: (1) type safety concern (2) performance is slower with complex underlying implementation*

## requests

1. Take a look at the requests API documentation here: https://requests.readthedocs.io/en/latest/  
Comment if the functions are well named in the Requests module (Follow the previous link to the documentation to see if you can find the Requests module (hint: look for API Reference)).

*I think the functions are well named. For example, requests.head() sends a head request, and requests.post() sends a post request. No additional functionalities that are not covered by the function name is implemented.*

2. Take a look at the [Requests](https://requests.readthedocs.io/en/latest/api/#lower-level-classes) class. APIs that have more than say 5 arguments in a function can be confusing or error prone to use. This is a heuristic of course, but do you see any member functions that include lots of arguments?

*Yes. In the lower level class Request, there are 10 arguments that can be put in. However I think this is still robust by setting these arguments optional*

3. Take another look at the Requests class. Note that many of the methods includes `**kwargs` as an argument. What is `**kwargs`? Why might it be good for a method to have a `**kwargs` argument? Why might it be bad?  

*(1)**kwargs means "keyword arguments"

(2)It's good because it adds flexibility to arguments that can be passed in. It allows user to directly pass in any number of arguments in a key=value pattern.

(3)This can be bad because it is more error proned and also it's not very explicit in its name.*

4. Take a look at the [Session class.] (https://requests.readthedocs.io/en/latest/api/#request-sessions) Not only can you read the API's for that class, you can also view the source code by clicking the 'source' text. 
Notice how some methods have arguments that are set to `None` while other arguments are not set to anything. Why is that? Can arguments be set to anything besides `None`? Why might it be good to set an argument by some predetermined value?


*The `None` is set so that the argument is optional. If the argument is not set to anything, the argument is required. Yes, they can be set to specific default value. It can be good to set it to predetermined value because it makes the code less error-proned by providing a default value to the argument. It also makes the code more user-friendly because users won't have to manually set every argument every time.*
