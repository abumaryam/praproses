import sys
import nltk
import re
import string
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def caseFoldingKalimat(kalimat):
    kalimat = kalimat.lower()
    return kalimat

def hapusAngka(kalimat):
    # menghapus angka
    kalimat = re.sub(r"\d+", "", kalimat) 
    return kalimat

def gantiTandaTitik(kalimat):
    # mengganti titik dengan spasi
    kalimat = kalimat.replace("."," ") 
    return kalimat

def hapusTandaBaca(kalimat):
    # Menghapus tanda baca
    kalimat = kalimat.translate(str.maketrans(" "," ",string.punctuation))
    return kalimat

def stemmingKalimat(kalimat):
    katakata = nltk.tokenize.word_tokenize(kalimat)
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    output = []
    for kata in katakata:
        stemmed = stemmer.stem(kata)
        output.append(stemmed)

    kalimat = " ".join(output)
    return kalimat

def filterKata(kalimat):
    #filtering seperti singkatan dan istilah-istilah tidak umum
    katahasil = []
    for kata in kalimat.split():
        with open("res/transtakbaku.txt", "r") as ins:
            katasumber = []
            for line in ins:
                katasumber.append(line.rstrip('\n'))

            for i in katasumber:
                x = i.split("~")
                if str(kata)==x[0]:
                    kata = x[1]
        katahasil.append(kata.rstrip('\n'))
    
    katahasil = ' '.join(katahasil)
    return katahasil


def cleanKataSatuKarakter(kalimat):
    # Membuang kata yang terdiri atas satu huruf saja
    katahasil = kalimat
    kata = kalimat.split()
    for wordelimination in kata:
        if(len(wordelimination)<=1):
            katahasil = ' '.join([xx for xx in kata if xx not in wordelimination])
    return katahasil

def hapusStopWords(kalimat):
    token = nltk.tokenize.word_tokenize(kalimat)
    daftarstopword =  set(stopwords.words('indonesian'))
    
    katahasil = []
    for t in token:
        if t not in daftarstopword:
            katahasil.append(t)
    kalimat = ' '.join(katahasil) 
    return kalimat

def hapusStopWordsNama(kalimat):
    # untuk menggunakannya silahkan copy file namalabel.txt ke /home/namuser/nltk_data/corpora/stopwords dan rename menjadi 'nama'
    token = nltk.tokenize.word_tokenize(kalimat)
    daftarstopword =  set(stopwords.words('nama'))
    katahasil = []
    for t in token:
        if t not in daftarstopword:
            katahasil.append(t)
    kalimat = ' '.join(katahasil) 
    return kalimat