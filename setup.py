from setuptools import setup

setup(
    name='pipx',
    version='1.13.0',
    description='Install and Run Python Applications in Isolated Environments',
    author_email='Chad Smith <chadsmith.software@gmail.com>',
    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3.14',
    ],
    install_requires=[
        'argcomplete>=1.9.4',
        'colorama>=0.4.4; sys_platform == "win32"',
        'packaging>=20',
        'platformdirs>=2.1',
        'tomli; python_version < "3.11"',
        'userpath!=1.9,>=1.6',
    ],
    extras_require={
        'uv': [
            'uv>=0.4',
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
