#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import mysql.connector

conn = mysql.connector.connect(user='root', password='1', database='test')

cursor=conn.cursor()
#create 'user' table
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
#add a record
cursor.execute('insert into user (id, name) values (%s, %s)', ('2', 'xiaoqiang'))
print('rowcount=', cursor.rowcount)
#commit trans
conn.commit()
cursor.close()

#query
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)

#close conn
cursor.close()
conn.close()
