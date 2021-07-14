<!-- 
What is the purpose of the data structure?

What is the performance of the data structure (you will need to talk about big O notation)?

What kind of problems can be solved using the data structure?

How would the data structure be used in Python (in some cases you will need to discuss recursion)?

What kind of errors are common when using the data structure? -->
# Table of Contents - Tree
Tree
* Recursion
* Tree

Implementation


Prove
* Coding Challenge
* Resolution

Resources

# Recursion
![Recursion-1](https://github.com/chloehuang18/Python-Data-Structure/blob/master/tree_recursion.png)

Figure 1 - Recursion

 Before we deep dive into tree, we need to learn recursion first.
 Recursion is a powerful technique in software development. It is often used in interviews for software developer positions. This method is to breaks down complex problems to small, simple, easily managed parts. 

When we use recursion, we must pay attention to the three laws: 

1. A recursive algorithm must have a base case.
2. A recursive algorithm must change its state and move toward the base case.
3. A recursive algorithm must call itself, recursively.

 ![Recursion-2](https://github.com/chloehuang18/Python-Data-Structure/blob/master/tree_recursion_law.png)

 Figure 2 - Law of Recursion

#
# Implementation
This is an example of recursion in action. We would like to create a finction to draw a same shape spiral. 
We first define the base case - The base case is the exit condition of the recursive algorithm. In line 15, when the line_length is greater than the max_length, the function will do nothing and return.
Second, we will need to decide what the small problem is, the small problem is to draw the spiral. And lastly, we need to use the recursive call. The function is being called which is the function we are currently using, We pass the length that increments, so that every time the function is call, we pass in an increased line length. 
[Example File](https://github.com/chloehuang18/Python-Data-Structure/blob/master/recursion.py)

![Recursion-2](https://github.com/chloehuang18/Python-Data-Structure/blob/master/tree_recursion_code.png)

 Figure 3 - Recursion Code

Here is the output

![Recursion-2](https://github.com/chloehuang18/Python-Data-Structure/blob/master/tree_recursion_example.png)

 Figure 4 - Recursion Output

#
# Tree



# Introduction tree
# Implementation
1. Create node class
```python
class Node:

    def __init__(self, data):
        # left child
        self.left = None
        # right child
        self.right = None
        # node's value
        self.data = data
```

2.  Create the insert function that compares the values of the node and decides whether to add the value to the left node or right node.

```python
def insert(self, data):
    if self.data:
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    else:
        self.data = data  

```

3. Traversing a BST 

# Example

We would like to use trees to solve the family tree problem. 

You can see trees as family trees, you are the root and it goes down to your parents, grandparents, and grand-grand-parent, and more. 



```python

```


#
### Real life examples
There are three importna la

1. Traversing hierarchical data structures: file systems, DOM tree
2. Data mining and database design and information retrieval
3. Most morden programming languages support recursion


#### Use family tree as example, the youngest would be the root

#
# Prove
### Challenage
Download [Tree Challenage](tree_challenage.py)

#
### Answer
Download [Tree Answer](tree_answer.py)

#
# Source
[Figure 1](https://prateekvjoshi.com/2013/10/05/understanding-recursion-part-i/)

[Turtle library -1](https://docs.python.org/3/library/turtle.html)

[Turtle library -2](https://realpython.com/beginners-guide-python-turtle/)

[Tree](https://www.educative.io/edpresso/binary-trees-in-python)