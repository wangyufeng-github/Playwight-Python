# !/usr/bin/env python
# _*_coding:utf-8 _*_
# @Time : 2024/9/18 14:26
# @Author : yufeng.wang@we-med.com
# @Site :
# @File : playwright基础.py
# @Software : PyCharm
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 创建浏览器驱动
    browser = p.chromium.launch(headless=False,slow_mo=500)
    context = browser.new_context()
    # context.route('**/*',lambda route:route.continue_())
    page = context.new_page()

    # 创建新页面并跳转到百度首页
    # page = browser.new_page()
    page.goto('https://www.baidu.com')
    print(page.title())
    # 输入搜索关键字并点击搜索按钮
    page.fill('#kw',"上海-悠悠博客")
    # 代替sleep()方法
    page.wait_for_timeout(1000)
    page.click('#su')
    page.pause()
    # browser.close()