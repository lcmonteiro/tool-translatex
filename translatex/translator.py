# #################################################################################################
# -------------------------------------------------------------------------------------------------
# File:   translate.py
# Author: Luis Monteiro
#
# Created on dec 13, 2019, 22:00 PM
# -------------------------------------------------------------------------------------------------
# #################################################################################################
# -------------------------------------------------------------------------------------------------
# Translator 
# -------------------------------------------------------------------------------------------------
class Translator:
    # ----------------------------------------------------------------------------------
    # providers
    # ----------------------------------------------------------------------------------
    class TranslateProvider:
        def __init__(self, to_lang='en', from_lang=None, server='mymemory'):
            from translate  import Translator
            self.__from   = from_lang if not None else 'autodetect'
            self.__to     = to_lang 
            self.__engine = Translator(
                to_lang=self.__to, from_lang=self.__from, provider=server)
        def translate(self, chunk):
            print('4')
            return map(lambda x: self.__engine.translate(x), chunk)
    class GoogleProvider:
        def __init__(self, to_lang='en', from_lang=None):
            from googletrans import Translator
            self.__from   = from_lang if not None else 'auto'
            self.__to     = to_lang 
            self.__engine = Translator()
        def translate(self, chunk):
            print('3')
            return map(
                lambda x : x.text, 
                self.__engine.translate(chunk, self.__to, self.__from))
    # ----------------------------------------------------------------------------------
    # initialization
    # ----------------------------------------------------------------------------------
    def __init__(self, to_lang='en', from_lang=None):
        self.__providers = [
            Translator.GoogleProvider   (to_lang, from_lang),
            Translator.TranslateProvider(to_lang, from_lang, 'microsoft')]
    # ----------------------------------------------------------------------------------
    # translate
    # ----------------------------------------------------------------------------------
    def translate(self, chunk):
        print('1')
        for provider in self.__providers:
            try:
                return provider.translate(chunk)
            except:
                pass
        raise RuntimeError('translation failed')
# #################################################################################################
# -------------------------------------------------------------------------------------------------
# end
# -------------------------------------------------------------------------------------------------
###################################################################################################