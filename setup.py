from setuptools import setup, find_packages

setup(
    name='AtomUI',
    version='0.1',
    packages=find_packages(),
    url='https://github.com/mingminyu/AtomUI',
    license='Apache 2.0',
    author='mingminyu',
    author_email='yu_mingm623@163.com',
    description='基于 NiceGUI 的增强 UI 框架',
    install_requires=[
        "nicegui",
        "signe",
        "pandas",
        "fastapi",
        "markdown-it-py",
    ],
)
