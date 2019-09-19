import dbs.dbtblLaporanPost as Laporan
import prepro.simplepreprocess as pp

for data in Laporan.selectAll():
    kalimat = data[4]
    print("before: ",kalimat)
    kalimat = pp.caseFoldingKalimat(kalimat)
    kalimat = pp.hapusAngka(kalimat)
    kalimat = pp.gantiTandaTitik(kalimat)
    kalimat = pp.hapusTandaBaca(kalimat)
    kalimat = pp.stemmingKalimat(kalimat)
    Laporan.updateLaporan(data[0],kalimat)
    print("after: ",kalimat)
    print("---------------------------\n")