from setuptools import find_packages,setup

setup(
    name='word-blocks',
    author='Kyle Pericak',
    author_email='kyle@pericak.com',
    packages=find_packages(),
    install_requires=[
        'click',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'word-blocks = words.entry_point:main',
        ],
    }
)
