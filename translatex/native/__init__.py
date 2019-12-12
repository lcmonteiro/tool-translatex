# #######################################################################################
# ---------------------------------------------------------------------------------------
# File:   __init__.py
# Author: Luis Monteiro
#
# Created on nov 11, 2019, 22:00 PM
# ---------------------------------------------------------------------------------------
# #######################################################################################

# imports
from subprocess import call
from os.path    import dirname
from os.path    import abspath
from platform   import system
from tempfile   import TemporaryDirectory

# -----------------------------------------------------------------------------
# program path 
# -----------------------------------------------------------------------------
def program():
    if system() == 'Windows':
        return abspath('%s/TranslateXml.exe'%(dirname(__file__)))
    return abspath('%s/TranslateXml'%(dirname(__file__)))

# -----------------------------------------------------------------------------
# extract
# -----------------------------------------------------------------------------
def extract(path, type):
    from json    import load
    from os.path import join
    # container
    with TemporaryDirectory() as name:
        file = join(name, 'data')
        # export
        call([program(), 
            '-m','export', 
            '-i', path, 
            '-o', file,
            '-p', type])
        # convert
        with open(file, 'r') as f:
            return load(f)
# -----------------------------------------------------------------------------
# load
# -----------------------------------------------------------------------------
def load(data, path, type):
    from json    import dump
    from os.path import join
    # container
    with TemporaryDirectory() as name:
        file = join(name, 'data')
        # convert
        with open('./cache', 'w') as f:
        #with open(file, 'w') as f:
            dump(data, f)
        # import
        call([program(), 
            '-m', 'import', 
            '-i', file,
            '-o', path, 
            '-p', type])
# #######################################################################################
# ---------------------------------------------------------------------------------------
# End
# ---------------------------------------------------------------------------------------
# #######################################################################################