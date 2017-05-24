#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0', 'numpy', 'scipy',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='Complexity',
    version='0.3.1',
    description=" ",
    long_description=readme + '\n\n' + history,
    author="Joanna Palewicz",
    author_email='asiapalewicz@gmail.com',
    url='https://github.com/dykra/Complexity',
    packages=[
        'Complexity',
    ],
    package_dir={'Complexity':
                 'Complexity'},
    entry_points={
        'console_scripts': [
            'Complexity=Complexity.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='Complexity',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
