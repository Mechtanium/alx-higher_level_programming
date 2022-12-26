# 0-run
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable `$PYFILE`

# 1-run_inline
Write a Shell script that runs Python code.

The Python code will be saved in the environment variable `$PYCODE`
```
guillaume@ubuntu:~/py/0x00$ export PYCODE='print(f"Best School: {88+10}")'
guillaume@ubuntu:~/py/0x00$ ./1-run_inline 
Best School: 98
guillaume@ubuntu:~/py/0x00$ 
```

# 2-print.py
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
```
guillaume@ubuntu:~/py/0x00$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
```

# 3-print_number.py
Complete this [source code](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

You can find the source code here
The output of the script should be:
the number, followed by `Battery street`,
followed by a new line
You are not allowed to cast the variable number into a string
Your code must be 3 lines long
You have to use f-strings [tips](https://alx-intranet.hbtn.io/rltoken/Ju0J8BxkuPX5yKZctyKfsQ)
```
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```