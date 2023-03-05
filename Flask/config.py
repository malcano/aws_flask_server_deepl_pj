import pymysql

conn = pymysql.connect(
    host = "deepl-db.cozq2mkojhyv.ap-northeast-2.rds.amazonaws.com",
    port = 3306,
    user = 'admin',
    password  = 'alsgh5600',
    db = 'deepldb'
)

