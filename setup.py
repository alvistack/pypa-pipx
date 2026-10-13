from setuptools import setup

setup(
    name='pipx',
    version='1.17.14',
    description='Install and Run Python Applications in Isolated Environments',
    author_email='Chad Smith <chadsmith.software@gmail.com>',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
        'Programming Language :: Python :: 3.15',
    ],
    install_requires=[
        'argcomplete>=3.7.2',
        'colorama>=0.4.6; sys_platform == "win32"',
        'filelock>=4.0.9',
        'packaging>=26.3',
        'platformdirs>=4.12.2',
        'userpath!=1.9,>=1.9.2',
    ],
    extras_require={
        'uv': [
            'uv>=0.12.22',
        ],
    },
    entry_points={
        'console_scripts': [
            'pipx = pipx.main:cli',
        ],
    },
    packages=[
        'pipx',
        'pipx.backends',
        'pipx.commands',
    ],
    package_dir={'': 'src'},
)
