from setuptools import setup  # type: ignore

setup(
    name='atomui',
    version='0.1',
    packages=['atomui'],
    url='https://github.com/mingminyu/atomui',
    license='Apache 2.0',
    author='mingminyu',
    author_email='yu_mingm623@163.com',
    description='基于 NiceGUI 的增强 UI 框架',
    install_requires=[
        "nicegui",
        "signe",
        "pandas",
    ],
)
