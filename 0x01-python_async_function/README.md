# 0x01. Python - Async
## `Python` `Back-end` 

# Learining Outcomes
* I learned about async programming in Python.
* I learned about asyncio, async and await syntax.
* I learned about async generators.
* I leanrned how to run concurrent coroutines.
* I learned how to create asyncio tasks.

## Tasks
### 0. The basics of async
In this task I wrote an asynchronuous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and max_delay seconds and finally returns it.

#### output
```
simontagbor@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

simontagbor@ubuntu:~/0x01$ ./0-main.py
8.010297259495044
1.3713171118642546
13.872428531315565

```

### 1. Let's execute multiple coroutines at the same time with async
In this task I wrote a function called `wait_n` that takes in 2 arguments - an integer `n` and an integer `max_delay`. It returns a list of all the delays. The list of the delays was sorted  in ascending order without using sort().

#### output
```
simontagbor@ubuntu:~/0x01$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

simontagbor@ubuntu:~/0x01$ ./1-main.py
[0.108471849, 0.109773162, 0.114173936, 0.115634768, 0.118821355]
[0.102867399, 0.104015933, 0.105026927, 0.105744588, 0.106849474, 0.107247278, 0.107618819, 0.108350189, 0.108471849, 0.109773162]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

```

