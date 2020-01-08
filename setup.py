# #######################################################################################
# ---------------------------------------------------------------------------------------
# File:   setup.py
# Author: Luis Monteiro
#
# Created on nov 11, 2019, 22:00 PM
# ---------------------------------------------------------------------------------------
# #######################################################################################
# imports
from setuptools import setup, find_packages
# -----------------------------------------------------------------------------
# helpers
# -----------------------------------------------------------------------------
with open("README.md", "r") as fh:
    long_description = fh.read()
# -----------------------------------------------------------------------------
# setup
# -----------------------------------------------------------------------------
setup(
    name='translatex',  
    version='0.3',
    author="Luis Monteiro",
    author_email="monteiro.lcm@gmail.com",
    description="TranslateXML",
    long_description=long_description,
    url="",
    packages=[
        'translatex',
        'translatex.native'
    ],
    package_data={
        'translatex.native': ['TranslateXml', 'TranslateXml.exe']
    },
    install_requires=[
        'progressbar2',
        'gtranslate @ https://github.com/lcmonteiro/tool-gtranslate/tarball/master/#egg=gtranslate',
    ],
    entry_points={
      'console_scripts': [
          'translatex = translatex:main_translate',
      ]
    }
 )
# #######################################################################################
# ---------------------------------------------------------------------------------------
# End
# ---------------------------------------------------------------------------------------
# #######################################################################################
