from setuptools import setup, find_packages

setup(
    name='click_command_script',
    version='1.0',
    description = '命令行管理工具',
    long_description  = '此版本是基于click模块开发的易于管理常用脚本命令'
                        '同时复用函数模块',
    # 可以指定packages, 也可以用find_packages函数查找
    packages = find_packages(),
    # packages = ['main'],
    include_package_data=True,
    install_requires=[
        'click',
        # Colorama is only required for Windows.
        'Colorama'
    ],
    entry_points='''
        [console_scripts]
        click_command_run=main:click_command
    '''
)
