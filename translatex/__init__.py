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
def translate(data, from_lang='en', to_lang='de'):
    from gtranslate   import Translator
    from random       import randint
    from time         import sleep
    from progress.bar import Bar
    generator  = fibonacci()
    translator = Translator(to_lang, from_lang)
    result     = []
    # preprocessing  
    data = map(lambda x: x.replace('_', ' '), data)
    # split in to chunks
    data = split(data, 1000)
    # translate
    bar = Bar('translating', max=len(data))
    for chunk in data:
        bar.next()
        while True:
            try:
                for item in translator.translate(chunk):
                    result.append(item)
                break
            except Exception as ex:
                print('error::{}'.format(str(ex)))
                print('sleep::translation failed ...')
                translator = Translator(to_lang, from_lang)
                sleep(randint(10, next(generator)))
    bar.finish()
    return result
# -----------------------------------------------------------------------------
# translate process
# -----------------------------------------------------------------------------
def translate_process(path, schema, from_lang, to_lang):
    print("tranlate --schema={} {}".format(schema, path))
    try:
        # extract data
        data = extract(path, schema)
        # translate data
        data = translate(data, from_lang, to_lang)
        # load data
        load(data, path, schema)
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
    parser.add_argument('--scheme', '-s',
        type    = str, 
        default = 'canoe')
    parser.add_argument('--from-lang', '-f',
        type    = str, 
        default = 'auto')
    parser.add_argument('--to-lang',  '-t',
        type    = str, 
        default = 'en')
    args = parser.parse_args(args=args)
    return translate_process(
        args.path, args.scheme, args.from_lang, args.to_lang)
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