import dbs.dbtblLaporanPost as Laporan
import prepro.simplepreprocess as pp

for data in Laporan.selectAll():
    kalimat = data[4]
    print("before: ",kalimat)
    kalimat = pp.filterKata(kalimat)
    kalimat = pp.cleanKataSatuKarakter(kalimat)
    kalimat = pp.hapusStopWords(kalimat)
    kalimat = pp.hapusStopWordsNama(kalimat)
    Laporan.updateLaporan(data[0],kalimat)
    print("after: ",kalimat)
    print("---------------------------\n")