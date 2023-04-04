from setuptools import find_packages
from setuptools import setup

setup(
    name="RobotNotice",
    version="0.0.2",
    license="GNU General Public License v3 (GPLv3)",
    author="Yathon",
    author_email="yathon@dyxt.com",
    description="提供方便通用的钉钉群和企业微信群机器人消息通知接口。",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/yathon/RobotNotice",
    project_urls={
        "Bug Report": "https://github.com/yathon/RobotNotice/issues/new"
    },
    install_requires=[
        "asyncio",
        "aiohttp",
        "requests",
    ],
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    py_modules=["RobotNotice"],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
