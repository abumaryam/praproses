import sys
import nltk
import re
import string
from nltk.tokenize import word_tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def cekSingkatan(text):
    status = False
    with open("res/kumpulansingkatan.txt", "r") as ins:
        kata = []
        for line in ins:
            kata.append(line.rstrip('\n'))

        for i in kata:
            if str(text)==i:
                status = True
    return status

def tambahkanSingkatan(text):
    f = open("res/kumpulansingkatan.txt", "a+")
    f.write(str(text)+"\r\n")

def identifikasi(kalimat):
    katakata = nltk.tokenize.word_tokenize(kalimat)
    try:
        with open('res/kata-dasar.txt', 'rU') as infile:
            wordSet = set(line.strip() for line in infile)
    except IOError:
        print('error opening file')

    for kata in katakata:
        if not kata in wordSet:
            if(not cekSingkatan(str(kata))):
                tambahkanSingkatan(str(kata))