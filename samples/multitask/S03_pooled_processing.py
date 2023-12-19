#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4) # 进程池的大小是4，所以output里 前4个进程结束后，第五个进程才能开始。如果process pool为5，则5个进程可以同时跑。
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

'''
Output:
Parent process 37809.
Waiting for all subprocesses done...
Run task 0 (37812)...
Run task 1 (37811)...
Run task 2 (37813)...
Run task 3 (37814)...
Task 0 runs 0.27 seconds.
Run task 4 (37812)...
Task 2 runs 0.85 seconds.
Task 3 runs 1.35 seconds.
Task 4 runs 1.63 seconds.
Task 1 runs 2.62 seconds.
All subprocesses done.

'''
