#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
‘’‘
This line is crucial. os.fork() creates a new child process. 
After this line, the rest of the code will run in two separate processes: 
    the parent 
    and the child. 
The fork() method returns 
    0 in the child process  
    and the child's process ID in the parent process.
’‘’
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

'''
Process (876) start...
I (876) just created a child process (877).
I am child process (877) and my parent is 876.
'''
