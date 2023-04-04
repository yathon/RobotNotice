# -*- coding: utf-8 -*-
__all__ = ['notice', 'aionotice']

import asyncio

from ding_notice import ding_notice, ding_notice_async
from wecom_notice import wecom_notice, wecom_notice_async


def notice(content, robot):
    if not content:
        print('未指定消息内容，无需处理发送请求')
        return
        # raise Exception('未指定消息内容，无需处理发送请求')
    if not robot:
        print('未指定机器人，无法处理发送请求')
        return
        # raise Exception('未指定机器人，无法处理发送请求')
    if len(robot) == 64:
        ding_notice(content=content, robot=robot)
    elif len(robot) == 36:
        wecom_notice(content=content, robot=robot)


async def aionotice(content, robot):
    if not content:
        print('未指定消息内容，无需处理发送请求')
        return
        # raise Exception('未指定消息内容，无需处理发送请求')
    if not robot:
        print('未指定机器人，无法处理发送请求')
        return
        # raise Exception('未指定机器人，无法处理发送请求')
    if len(robot) == 64:
        # asyncio.ensure_future(_aio_send(text, ding))
        asyncio.ensure_future(ding_notice_async(content=content, robot=robot))
    elif len(robot) == 36:
        asyncio.ensure_future(wecom_notice_async(content=content, robot=robot))
