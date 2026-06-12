from setuptools import setup

setup(
    name='snip-cli',
    version='1.0.0',
    description='A blazing fast terminal snippet manager.',
    author='Your GitHub Username',
    py_modules=['snip'], 
    entry_points={
        'console_scripts': [
            'snip=snip:main', 
        ],
    },
)
