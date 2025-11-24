# LOOPS in Python

There are mainly **two types of loops** in Python: `for` loop and `while` loop.

---

## For Loop

`for` loop is mainly used to perform iterations over a **list**, **tuple**, **set**, or **string**.  
It is especially useful when the number of iterations is known or when you know the start, stop, and step points.

### Syntax

```python
# Example: Iterating over a list
fruits = ["apple", "banana", "kiwi"]

for i in fruits:
    print(i)
```
output  
apple   
banana  
kiwi  

---

## While Loop 

`while` loop is mainly used to perform operation where the number of iteration are unknown and we need to solve until the condition is **TRUE**.  
As mentioned above, the loop continues to execute the block of code until the condition is **TRUE**.  

## Syntax

```python
# Example: iterating over a 50 number to find the multiples of 3
i = 1
while i < 50:
    if i % 3 == 0:
        print(i)
    i = i + 1   

    

