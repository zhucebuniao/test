#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='1', database='test')
cursor=conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

#close conn
cursor.close()
conn.close()
