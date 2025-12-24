# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='instacheck',
    version="1.31",
    packages=find_packages(),
    author="hypo112111",
    install_requires=["argparse","requests","phonenumbers","pycountry"],
    description="It is a tool written to retrieve basic info on Instagram accounts",
    long_description="It is a tool written to retrieve basic info on Instagram accounts",
    include_package_data=True,
    url='http://github.com/hypo112111/instacheck',
    entry_points = {'console_scripts': ['instacheck = instacheck.core:main']},
    classifiers=[
        "Programming Language :: Python",
    ],
)
