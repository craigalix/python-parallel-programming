# Python-parallel-programming
Asyncio [coroutines], Multi Processing, Multi Threading and baseline comparison

This Repo will demonstrate the different parallel processing methods in python.
Example used: we send http requests and wait for response.

# Note 
1) multi processing: spawn processes in multiple cores, independent of each other parallely (Actually doing parallel programming)
2) multi threading: spawn multiple threads, lightweight compared to processes, thread is a sagment of processes. (Uses context switching between threads)
   but due to Global Intepreter Lock, cannot parallelize execution. only allow 1 thread to execute at a time
   still can be fast due to contacts switching between threads, almost like coroutines but with multiple threads.
3) Asyncio: does contact switching for concurrency, use single thread, it is your code that decides when to leave control of the running thread so that some other portion of code can take control of main thread. (Uses context switching between tasks)

Benchmark:
- Standard = 44 seconds
- Multi Processing = 8.8 seconds (more sutable for cpu bound tasks)
- Multi Threading = 3.3 seconds (can cause problems, dead lock, race condition, overhead of threads)
- Asyncio = 3.3 seconds (single thread, where code decides when to leave a task on a single thread)
