Tool-Translatex
---------------
XML translator for vector/canoe simulation 

Requirements:
-------------
- python 3.6 > 
- chrome 79

Features
--------
- Translation recursively of XML files   

Installation
------------
``` sh
  $ pip install git+https://github.com/lcmonteiro/tool-translatex.git@master
```

Usage
-------------

``` sh
  $ translatex -h
  usage: translatex [-h] [--scheme SCHEME] [--from-lang FROM_LANG]
                    [--to-lang TO_LANG]
                    [path]

  positional arguments:
    path                  path for parent folder

  optional arguments:
    -h, --help            show this help message and exit
    --scheme SCHEME, -s SCHEME
    --from-lang FROM_LANG, -f FROM_LANG
    --to-lang TO_LANG, -t TO_LANG
```
Output
------
``` 
[ 2020-01-08 22:59:20 ] [  INFO   ] [ Arguments ] [ {
    "i":".",
    "l":"INFO",
    "m":"export",
    "o":/tmp/tmp0hgtbv_k/data",
    "p":"canoe"
} ]
[ 2020-01-08 23:00:02 ] [  INFO   ] [ Export ] [ file= ./data/aaa.xvp ]
...
DevTools listening on ws://127.0.0.1:62377/devtools/browser/4936eb98-ba43-4f51-ae77-5df34c1b5cbb
translating | 100% (49 of 49) |########################################################################| Elapsed Time: 0:17:21 Time:  0:17:21                                
[ 2020-01-08 23:17:38 ] [  INFO   ] [ Arguments ] [ {
    "i":"Temp/tmps4jl4jvc/data",
    "l":"INFO",
    "m":"import",
    "o":".",
    "p":"canoe"
} ]
[ 2020-01-08 23:17:39 ] [  INFO   ] [ Import ] [ file= ./data/aaa.xvp ]
...
```

Author
------
[Luis Monteiro @ linkdin](<https://www.linkedin.com/in/luis-monteiro-918a3033/>)

