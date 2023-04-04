# -*- coding: utf-8 -*-
__all__ = ['notice', 'aionotice']

import asyncio
import aiohttp
import requests


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


def ding_notice(content, robot, timeout=10, at_all=True):
    if not content:
        print('未指定消息内容，无需处理发送请求')
        return
        # raise Exception('未指定消息内容，无需处理发送请求')
    if not robot:
        print('未指定机器人，无法处理发送请求')
        return
        # raise Exception('未指定机器人，无法处理发送请求')
    url = f'https://oapi.dingtalk.com/robot/send'
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
    }
    params = {
        'access_token': robot
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "isAtAll": at_all
        }
    }
    try:
        requests.post(url, params=params, headers=headers, json=data, timeout=(timeout, timeout))
        # resp = requests.post(url, params=params, headers=headers, json=data, timeout=(timeout, timeout))
        # if resp.status_code == requests.codes.ok:
        #     resp_data = resp.json()
        #     errcode = resp_data.get('errcode')
        #     errmsg = resp_data.get('errmsg')
        #     if errcode == 0 and errmsg == 'ok':
        #         return
        #     print(f'[{errcode}]{errmsg}')
        #     return
        #     # raise Exception(f'[{errcode}]{errmsg}')
        # print(f'[{resp.status_code}]{resp.reason}')
        # # raise Exception(f'[{resp.status_code}]{resp.reason}')
    except Exception as e:
        print(e)


async def ding_notice_async(content, robot, timeout=10, at_all=True):
    if not content:
        print('未指定消息内容，无需处理发送请求')
        return
        # raise Exception('未指定消息内容，无需处理发送请求')
    if not robot:
        print('未指定机器人，无法处理发送请求')
        return
        # raise Exception('未指定机器人，无法处理发送请求')
    url = f'https://oapi.dingtalk.com/robot/send'
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
    }
    params = {
        'access_token': robot
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content
        },
        "at": {
            "isAtAll": at_all
        }
    }
    try:
        async with aiohttp.ClientSession(
                headers=headers, conn_timeout=timeout, read_timeout=timeout
        ) as session:
            async with session.request(
                    method='post', url=url, params=params, data=data, verify_ssl=False
            ):
                # ) as r:
                # if r and (r.status == 200):
                #     print('send notice ok')
                # else:
                #     print('send notice error')
                pass
    except Exception as e:
        print(e)


def wecom_notice(content, robot, timeout=10):
    if not content:
        print('未指定消息内容，无需处理发送请求')
        return
        # raise Exception('未指定消息内容，无需处理发送请求')
    if not robot:
        print('未指定机器人，无法处理发送请求')
        return
        # raise Exception('未指定机器人，无法处理发送请求')
    url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send'
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
    }
    params = {
        'key': robot
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content,
            "mentioned_list": ["@all"]
        }
    }
    try:
        requests.post(url, params=params, headers=headers, json=data, timeout=(timeout, timeout))
        # resp = requests.post(url, params=params, headers=headers, json=data, timeout=(timeout, timeout))
        # if resp.status_code == requests.codes.ok:
        #     resp_data = resp.json()
        #     errcode = resp_data.get('errcode')
        #     errmsg = resp_data.get('errmsg')
        #     if errcode == 0 and errmsg == 'ok':
        #         return
        #     print(f'[{errcode}]{errmsg}')
        #     return
        #     # raise Exception(f'[{errcode}]{errmsg}')
        # print(f'[{resp.status_code}]{resp.reason}')
        # raise Exception(f'[{resp.status_code}]{resp.reason}')
    except Exception as e:
        print(e)


async def wecom_notice_async(content, robot, timeout=10):
    if not content:
        print('未指定消息内容，无需处理发送请求')
        return
        # raise Exception('未指定消息内容，无需处理发送请求')
    if not robot:
        print('未指定机器人，无法处理发送请求')
        return
        # raise Exception('未指定机器人，无法处理发送请求')
    url = f'https://qyapi.weixin.qq.com/cgi-bin/webhook/send'
    headers = {
        'User-Agent': 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 '
                      '(KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'Content-Type': 'application/json'
    }
    params = {
        'key': robot
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": content,
            "mentioned_list": ["@all"]
        }
    }
    try:
        async with aiohttp.ClientSession(
                headers=headers, conn_timeout=timeout, read_timeout=timeout
        ) as session:
            async with session.request(
                    method='post', url=url, params=params, data=data, verify_ssl=False
            ):
                # ) as r:
                # if r and (r.status == 200):
                #     print('send notice ok')
                # else:
                #     print('send notice error')
                pass
    except Exception as e:
        print(e)
