#!/usr/bin/python
# -*- coding: utf-8 -*-

# This file is part of nose-docker-fabric.
# https://github.com/naphthalen/nose-docker-fabric

# Inspired by nose-docker by heynemann:
# https://github.com/heynemann/nose-docker

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2016 Pavel Sadikov ops@bitsighttech.com


from setuptools import setup, find_packages
from nose_docker_fabric import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='nose-docker-fabric',
    version=__version__,
    description='nose-docker-fabric tests fabric tasks by targeting the container',
    long_description='''
nose-docker allows you to run tests inside or against docker containers.
''',
    keywords='fabric',
    author='Pavel Sadikov',
    author_email='ops@bitsighttech.com',
    url='https://github.com/naphthalene/nose-docker-fabric',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'nose',
        'sh',
        'lxml',
        'cssselect',
        'pyyaml',
        'docker-py',
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'nose.plugins': (
            "docker_fabric=nose_docker_fabric.plugin:NoseDockerFabricPlugin",
        ),
    },
)
