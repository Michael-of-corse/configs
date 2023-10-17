import sqlite3 as sq
import random as r
import string as s

table="ctf"

def exist_tables():
    conn= sq.connect('test.db')
    conn.execute('CREATE TABLE if not exists ' + table_name +''' (
                id integer primary key AUTOINCREMENT,
                fn text not null,
                ln text not null,
                gn text not null,
                tg text not null UNIQUE ON CONFLICT IGNORE,
                klas text not null,
                team text,
                nikname text,
                passwd text,
                date datatime);''')
    conn.close()

def add_from_Ya(data):
    conn=sq.connect('ctf.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO '+table+' (fn,ln,gn,tg,klas) VALUES (?,?,?,?,?);',data)
    conn.commit()
    conn.close()

def set_passwd(telegram):
    conn=sq.connect('ctf.db')
    cur=conn.cursor()
    password=''.join(r.sample(s.ascii_letters+s.digits+s.punctuation,16))
    cur.execute('UPDATE '+table+'SET passwd = ? WHERE tg = ?;',(password,telegram))
    conn.commit()
    conn.close()
    return password

def set_nikname(telegram):
    conn=sq.connect('ctf.db')
    cur=conn.cursor()
    cur.execute('UPDATE '+table+'SET nikname = ? WHERE tg = ?;',(nik,telegram))
    conn.commit()
    conn.close()

def get_team_count(team):
    conn.sq.connect('ctf.db')
    cur=conn.cursor()
    cur.execute('SELECT COUNT(team) FROM '+table);
    return cur.fetchone()
