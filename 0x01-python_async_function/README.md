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

### 1. Let's execute multiple coroutines at the same time 
