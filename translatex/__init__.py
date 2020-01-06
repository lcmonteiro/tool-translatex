# #################################################################################################
# -------------------------------------------------------------------------------------------------
# File:   __init__.py
# Author: Luis Monteiro
#
# Created on nov 11, 2019, 22:00 PM
# -------------------------------------------------------------------------------------------------
# #################################################################################################
# ---------------------------------------------------------
# extern
# ---------------------------------------------------------
from argparse import ArgumentParser
# ---------------------------------------------------------
# internal
# ---------------------------------------------------------
from .native  import extract
from .native  import load
# #######################################################################################
# ---------------------------------------------------------------------------------------
# translate
# ---------------------------------------------------------------------------------------
# #######################################################################################
# -----------------------------------------------------------------------------
# generator
# -----------------------------------------------------------------------------
def fibonacci():
    x, y = 10, 10
    while True:
        yield x
        x, y = y, x + y
# -----------------------------------------------------------------------------
# split text
# -----------------------------------------------------------------------------
def split(text, max_size):
    result     = []
    chunk      = []
    chunk_size = 0
    for item in text:
        item_size = len(item)
        if (chunk_size + item_size) <= max_size:
            chunk.append(item)
            chunk_size  += item_size
        elif item_size <= max_size:
            result.append(chunk)
            chunk      = [item]
            chunk_size = item_size
    if chunk_size:
        result.append(chunk)
    return result
# -----------------------------------------------------------------------------
# translate text
# -----------------------------------------------------------------------------
def translate(data, dst='en', src='de'):
    from .translator import Translator
    from random      import randint
    from time        import sleep
    generator  = fibonacci()
    translator = Translator(dst, src)
    result     = []
    # preprocessing  
    data = map(lambda x: x.replace('_', ' '), data)
    # translate
    for chunk in split(data, 1000):
        while True:
            try:
                for item in translator.translate(chunk):
                    print(item)
                    result.append(item)
                break
            except Exception as ex:
                print('error::{}'.format(str(ex)))
                print('sleep::translation failed ...')
                translator = Translator(dst, src)
                sleep(randint(10, next(generator)))
    return result
# -----------------------------------------------------------------------------
# translate process
# -----------------------------------------------------------------------------
def translate_process(path, type):
    print("tranlate --type={} {}".format(type, path))
    try:
        # extract data
        data = extract(path, type)

        
        # translate data
        data = translate(data)
        print(len(data))
        print(data)
        # load data
        load(data, path, type)
    except Exception as ex:
        print(str(ex))
    return 0
# #######################################################################################
# ---------------------------------------------------------------------------------------
# entry point
# ---------------------------------------------------------------------------------------
# #######################################################################################
# -------------------------------------------------------------------
# main function
# -------------------------------------------------------------------  
def main_translate(args=None):
    parser = ArgumentParser()
    parser.add_argument('path',    
        help    = 'path for parent folder',  
        type    = str, 
        nargs   = '?',
        default = '.')
    parser.add_argument('--type', '-t',
        type    = str, 
        default = 'canoe')
    args = parser.parse_args(args=args)
    return translate_process(args.path, args.type)
# -------------------------------------------------------------------
# main file
# -------------------------------------------------------------------    
if __name__ == "__main__":
    main_translate()
# #################################################################################################
# -------------------------------------------------------------------------------------------------
# end
# -------------------------------------------------------------------------------------------------
###################################################################################################