# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='pipx',
    version='1.4.3',
    description='Install and Run Python Applications in Isolated Environments',
    author_email='Chad Smith <chadsmith.software@gmail.com>',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[
        'argcomplete>=1.9.4',
        'colorama>=0.4.4; sys_platform == "win32"',
        'packaging>=20',
        'platformdirs>=2.1',
        'tomli; python_version < "3.11"',
        'userpath!=1.9.0,>=1.6',
    ],
    entry_points={
        'console_scripts': [
            'pipx = pipx.main:cli',
        ],
    },
    packages=[
        'pipx',
        'pipx.commands',
    ],
    package_dir={'': 'src'},
)
