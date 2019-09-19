import dbs.dbtblLaporanPost as Laporan
import prepro.penemuankataasing as pp

for data in Laporan.selectAll():
    kalimat = data[4]
    print("before: ",kalimat)
    pp.identifikasi(kalimat)
    