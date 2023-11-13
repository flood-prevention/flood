import pymysql


class MariaDB:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost', user='eunhye', password='0619', db='water_level')
        self.cur = self.db.cursor()
        print("connect")

    def add(self, level):
        sql = "insert into water_level(level) values('{0}')".format(level)
        self.cur.execute(sql)
        self.db.commit()
        return level

    def selectAll(self):
        sql = "select * from water_level"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
