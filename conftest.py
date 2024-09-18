from pytest import Item
import allure
import pytest
from typing import Dict

# 本地插件注册
pytest_plugins = [                   # noqa
    'plugins.pytest_playwright',     # noqa
    'plugins.pytest_base_url_plugin' # noqa
]


def pytest_runtest_call(item: Item):  # noqa
    # 动态添加测试类的 allure.feature()
    if item.parent._obj.__doc__:  # noqa
        allure.dynamic.feature(item.parent._obj.__doc__) # noqa
    # 动态添加测试用例的title 标题 allure.title()
    if item.function.__doc__: # noqa
        allure.dynamic.title(item.function.__doc__) # noqa


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args) -> Dict:
    """窗口最大化"""
    return {
        "args": ['--start-maximized'],
        **browser_type_launch_args,
    }


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright, pytestconfig) -> Dict:
    """窗口最大化"""
    return {
        "no_viewport": True,
        # 忽略https报错
        "ignore_https_errors": True,
        **browser_context_args,
    }
