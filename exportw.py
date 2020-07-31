import csv
import pymysql
import pandas as pd

conn=pymysql.connect(host='sqlserver.ga',user='datam',passwd='######',db='datam')

c=conn.cursor()
c.execute("select title,body from wanted;")
allrows=c.fetchall()
conn.close()
fp = open('file.csv', 'w') ##different path but you get the idea
myFile = csv.writer(fp, lineterminator='\n')
myFile.writerows(allrows)
print(allrows[1])
fp.close()
#conn.close()
