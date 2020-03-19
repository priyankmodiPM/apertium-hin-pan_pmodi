# apertium-hin-pan_pmodi

# Directory Structure
```
apertium-hin-pan_pmodi
│   README.md   
│   apertium-hin   
│   apertium-pan   
│   apertium-hin-pan   
│   apertium-init.py   
│
└───apertium-hin
│   │   apertium-hin.hin.dix
│   │   apertium-hin.hin.rlx
│   │   autogen.sh
│   
└───apertium-pan
|   │   apertium-pan.pan_Guru.dix
|   |   apertium-pan.pan_Guru.acx
|   |   autogen.sh
|
└───apertium-hin-pan
|   │   apertium-hin-pan.hin-pan_Guru.dix
|   │   apertium-hin-pan.hin-pan.t1x
|   │   apertium-hin-pan.hin-pan.t2x
|   │   apertium-hin-pan.hin-pan.t3x
|   │   autogen.sh
|   │   test_pan.txt (contains text after translation)
|   │   word_freq.py
|   │   word_freq.txt
│   └───texts/
│   |   │   story.hin.txt (contains source language test data)
|
└───────────────────────────────────────
```
----------------------------------------------------------------------------

# How to Run
```sh
$ cd apertium-hin
$ ./autogen.sh; make -j
$ cd ../apertium-pan
$ ./autogen.sh; make -j
$ cd ../apertium-hin-pan
$ ./autogen.sh --with-lang1=../apertium-hin --with-lang2=../apertium-pan; make -j
$ head -10  texts/story.hin.txt  | apertium -d . hin-pan_Guru > test_pan.txt
$ python word_freq.py > word_freq.txt
```

# Translated files
The translated file is available at /apertium-hin-pan_pmodi/apertium-hin-pan/test_pan.txt
The file word_freq.txt provides frequencies of all words to give an idea about what words remain to be translated