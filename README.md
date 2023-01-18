# PY4E_Mod_11_2_Python_RegEx_Averager
## Directions
1. Write a program to look for lines of the form `New Revision: {some integer here}` (i.e. `New Revision: 1234` or `New Revision: 546464` would both qualify). 
2. Extract the number from each of the lines using a regular expression and the `findall()` method. 
3. Compute the average of the numbers and print out the average as an integer.

mbox-long.txt and mbox-short.txt will be your test files.  Both are included in this repo.  You will need to write the logic to open and read through the files in your method.

## Starter Code
```python
def average_new_revision_lines():
    file_name = input("Enter file: ")


if __name__ == "__main__":
    average_new_revision_lines()
```

## Expected Output

```
Enter file: mbox-short.txt
39756
```

## Test
You can use `pytest` to test your code.  When all tests pass, you should be good to go!
