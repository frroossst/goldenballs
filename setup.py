import mysql.connector
db=mysql.connector.connect(
    host='localhost',
    user='home',
    passwd='home',
    database='data_dump'
    )
print(db)
mycursor=db.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)
mycursor.execute("INSERT INTO player_elim VALUES ('player one',0)")
mycursor.execute("INSERT INTO player_elim VALUES ('player two',0)")
mycursor.execute("INSERT INTO player_elim VALUES ('player three',0)")
mycursor.execute("INSERT INTO player_elim VALUES ('player four',0)")
mycursor.execute("INSERT INTO split_steal VALUES (0,0)")
db.commit()
