# 0x02. Python - Async Comprehension
#### `Python` `Back-end`

## Learning Outcomes:
Over the course of this project, i learned:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Tasks:

### [0. Async Generator](./0-async_generator.py)
<details><summary> I wrote  a coroutine called async_generator that takes no arguments. The coroutine loops 10 times, each time asynchronously wait 1 second, then yields a random number between 0 and 10. </summary><br>

#### Output:
```
simontagbor@ubuntu:~/0x02$ cat 0-main.py
#!/usr/bin/env python3
import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

asyncio.run(print_yielded_values())

simontagbor@ubuntu:~/0x02$ ./0-main.py
[0.9663727496594015, 8.261936687465552, 0.5528219747790605, 2.585038182588586, 7.167781156792787, 7.973445876332369, 8.34438916552449, 2.4344384042993777, 2.854908756914767, 9.535089550908602]

```
</details>

### [1. Async Comprehensions](./1-async_comprehension.py)
<details><summary> I wrote a coroutine called async_comprehension that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers. </summary><br>

#### Output:
```
simontagbor@ubuntu:~/0x02$ cat 1-main.py
#!/usr/bin/env python3

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main():
    print(await async_comprehension())

asyncio.run(main())

simontagbor@ubuntu:~/0x02$ ./1-main.py
[8.50030478415313, 0.4731139672368344, 6.890311985446557, 3.8025572102464326, 8.491030504740187, 4.287389539831404, 7.150701429787124, 0.8710267183340311, 8.108020739727831, 7.193454802259802]

```
</details>

### [2. Run time for four parallel comprehensions](./2-measure_runtime.py)
<details><summary> I wrote a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather. </summary><br>

#### Output:
```
simontagbor@ubuntu:~/0x02$ cat 2-main.py
#!/usr/bin/env python3

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main():
    return await measure_runtime()

print(asyncio.run(main()))

simontagbor@ubuntu:~/0x02$ ./2-main.py
10.106887817382812

```
</details>

