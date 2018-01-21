import psycopg2
from datetime import datetime, timedelta
from time import mktime

class MyDatabase():
    def __init__(self, db="autoqa", user="postgres", password='ultimate'):
        self.conn = psycopg2.connect(database=db, user=user, password=password)
        self.conn.autocommit = True
        self.cur = self.conn.cursor()

    def query(self, query):
        print(query)
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

class DbMethods():
    def queryTestInsert(self,testname,start,end,result,time):
        #start = datetime.datetime.now()
        print(start)
        print(end)
        starttime = start.strftime("%Y-%m-%d %H:%M:%S")
        #end = datetime.datetime.now()
        endtime = end.strftime("%Y-%m-%d %H:%M:%S")
        actualresult1 = result
        query = "insert into tests(testname,starttime,endtime,status,seconds_taken\
) values('"+testname+"','" + str(starttime) + "','" + str(endtime) + "','" + str(actualresult1) + "',"+str(time)+")"
        return query

    def timeDiff(self,start,end):
        difference_in_seconds = abs(mktime(start.timetuple()) - mktime(end.timetuple()))
        return difference_in_seconds
#db=MyDatabase()
#db.query("SELECT * FROM company;")

#
# conn = psycopg2.connect(host="localhost",database="autoqa", user="postgres", password="ultimate")
# cur = conn.cursor()
# cur.execute('''CREATE TABLE COMPANY
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME           TEXT    NOT NULL,
#       AGE            INT     NOT NULL,
#       ADDRESS        CHAR(50),
#       SALARY         REAL);''')
# conn.commit()
# conn.close()
# #
# def dbconnector():
#     connectionstring = pymysql.connect(host='localhost', port=3306, user='root', passwd='root', db='pythonauto')
#     dbdriver = connectionstring.cursor()
#     return dbdriver
# dbdriver.execute("Select testid,testname,starttime,endtime from tests")
# for r in dbdriver:
#     print(r)
# dbdriver.close()
# connectionstring.close()
# start = datetime.datetime.now()
# start=start.strftime("%Y-%m-%d %H:%M")
# end = datetime.datetime.now()
# end = end.strftime("%Y-%m-%d %H:%M")
# actualresult1=True
# query= "insert into tests(testid,testname,starttime,endtime,status\
# ) values(2,'Valid Login Test','"+ str(start) +"','"+str(end)+"','"+str(actualresult1)+"')"
# print(query)
# db.query(query)
# db.close()
# print(query)
# a.execute(query)
# a.close()

