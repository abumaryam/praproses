import dbs.dbhelper as dbh

TABLE_NAME = "tabel_coba"

def selectAll():
    query = "SELECT * FROM "+TABLE_NAME
    laporan = dbh.select(query)
    return laporan

def updateLaporan(id,text):
    sql = "UPDATE "+TABLE_NAME+" SET isi_laporan = %s WHERE id = %s"
    val = (text, id)
    dbh.update(sql,val)
