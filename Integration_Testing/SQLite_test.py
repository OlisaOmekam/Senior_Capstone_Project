#!/usr/bin/python
 
import sqlite3
import sys
from sqlite3 import Error
 
 
def create_connection():
    """ create a  connection to the SQLite 
        specified by the db_file
    :param db_file:  file
    :return: Connection object or None
    """
    db_file= "gro_log.db"
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def profile_table_setup():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS profiles (name STRING NOT NULL,user_db STRING NOT NULL);")

def create_profile(name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO profiles (name,user_db) values (\""+str(name)+"\",\""+str(name.lower())+"_db\");")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS "+str(name.lower())+"_db(barcode INTEGER NOT NULL,item_name STRING NOT NULL, exp DATE);")
def delete_profile(name):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM profiles WHERE name =\""+name+"\";")
    cur.execute("DROP "+ str(name.lower())+"_db;")


 
def select_all_profiles():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM profiles;")
 
    rows = cur.fetchall()
    
    for row in rows:
        print(row[0]+", "+row[1])
 
def select_inventory(name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM "+str(name.lower())+"_db;")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row[0])

def add_inventory(name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO "+str(name.lower())+" (name,user_db) values (\""+str(name)+"\",\""+str(name.lower())+"_db\");")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row[0])

def select_profile_db(name):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param name: name of profile wanted
    :return:
    """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT name FROM profiles WHERE name=\""+name+"\";")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row[0])


 
 
def main():

         profile_table_setup()
        #--------Add Profile Test------------
        #add = raw_input("Name you would like to add:")
        #create_profile(conn,add)

        #-------Delete Profile Test----------
        #delete= input("Name you would like to delete:")
        #delete_profile(conn,delete)

        #-------Select Profile Test----------
        #name= raw_input("Name you would like to select:")
        #select_profile_db(conn,name)
 
        #-------Show All Profiles Test-------
        #print("\n2. Query all profiles")
        #select_all_profiles(conn)
 
 
if __name__ == '__main__':
    main()