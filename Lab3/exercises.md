# Exercises

Update your answers to the following questions, make sure to commit this file and your improved code as well!


## Task 1 - oop.py

1. Is MObject an abstract or a concrete class? Explain why:
	- No. 
	- In order to make the class abstract, MObject class should inherit the ABC class (Abstract Base Class).

1. The 'Image' class has commented code for a `__del__` method. What does this commented-out method do?
	- The method is called "destructor", which is called when an instance of a class is ready to be destroyed. "Destroy" in this case means that the memory location of the class instance drops to zero and garbage collector reclaims its memory.

1. What class does Texture inherit from?
	- Image.

1. What methods and attributes does the Texture class inherit from 'Image'? 
	- attributes:
		- m_width
        - m_height
        - m_colorChannels
        - m_Pixels
	- methods:
		- getWidth
		- getHeight
		- getPixelColorR
		- getPixels
		- setPixelsToRandomValue

1. Do you think a texture should have a 'has-a' (composition) or 'is-a'(inheritance) relationship with 'Image'? If you think it is a 'has-a' relationship, refactor the code. As long as you defend your decision in the response below it could be either--but defend your position well!
	- It should be a 'has-a' relationship, because each image item should have its own texture.

1. I did not declare a constructor for Texture. Does Python automatically create constructors for us? 
	- Yes.

## Task 2 - Singleton

1. Refactor the singleton.py file such that:
  - The first time the logger is constructed, it will print out:
  	-  `Logger created exactly once`
  - If the logger is already initialized, it will print:
  	-  `logger already created`
Note: You do not 'have' a constructor, but you construct the object in the *instance* member function where you will create an object.  
Hint: Look at Lecture 3 slides for an example of creating a Singleton in Python

1. Are singleton's in Python thread safe? Why or why not?

	- Without proper locking, singleton is not thread safe. It is possible that two threads are checking if the instance is None, and resulted in the creation of two instances, which defeated the purpose of singleton.
  
