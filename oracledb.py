"""
    Oracle Database Connection Wrapper
    @author: Mohamed Riyad <@RyadPasha>
    @url: http://ryadpasha.com
    email: me@ryadpasha.com
    @license: MIT License
"""
import cx_Oracle


class OracleDB:
    """
        Usage:
            db = OracleDB("user", "pass", "yourserver.com", 1523, "YOUR_SID")
            db.connect()
            db.cursor.execute("SELECT yourcolumn FROM yourtable")
            result1 = [x[0] for x in db.cursor]
            db.close()
            db.connect()
            db.cursor.execute("SELECT yourothercolumn FROM yourothertable")
            result2 = [x[0] for x in db.cursor]
            db.close()
            # do stuff with result1 and result2 ...
    """
    def __init__(self, user, password, server, port, sid):
        self.tns = cx_Oracle.makedsn(server, port, sid)
        self.connection = None
        self.cursor = None
        self.user = user
        self.password = password

    def connect(self):
        self.connection = cx_Oracle.connect(self.user, self.password, self.tns)
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()
