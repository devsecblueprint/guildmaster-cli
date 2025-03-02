from setuptools import setup

setup(
    name='dsb-discord-admin-cli',
    version='0.1',
    py_modules=['src'],
    install_requires=[
        'discord.py',
        'fire'
    ],
    entry_points={
        'console_scripts': [
            'src = src:main'
        ]
    },
    author='Damien Burks',
    description='CLI tool for DSB Discord admin tasks',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ]
)
