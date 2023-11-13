import pymysql


class MariaDB:
    def __init__(self):
        self.db = pymysql.connect(
            host='localhost', user='eunhye', password='0619', db='water_level')
        self.cur = self.db.cursor()
        print("connect")

    def add(self, level_1, level_2):
        sql = "insert into flood(level) values('{}','{}')".format(
            level_1, level_2)
        self.cur.execute(sql)
        self.db.commit()
        return level_1, level_2

    def selectAll(self):
        sql = "select * from flood"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result
