#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio

async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

‘’‘
import asyncio

async def hello():
    print('Hello world!')
    await asyncio.sleep(1)
    print('Hello again!')

async def main():
    tasks = [asyncio.create_task(hello()), asyncio.create_task(hello())]
    await asyncio.wait(tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()


’‘’
