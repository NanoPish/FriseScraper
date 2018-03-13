import pymysql

class mysql_database:
    def __init__(self):
        self.db_name = 'lafrise'
        try:
            self.cnx = pymysql.connect(user='lafrise',
                                       password='lafrise',
                                       host='localhost',
                                       database='lafrise',
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)
        except pymysql.InternalError as error:
            code, message = error.args
            print('>>>>>>>>>>>>>', code, message)
        self.cur = self.cnx.cursor()
        
    def query(self, query, params):
        return self.cur.execute(query, params)

    def __del__(self):
        self.cnx.close()
