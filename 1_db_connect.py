import MySQLdb
import MySQLdb.cursors as cursors
import traceback

def getRows():
    conn = MySQLdb.connect(host="localhost",user="root",
                  passwd="",db="employees", cursorclass=cursors.SSCursor)
    # cursorclass = cursors.SSCursor. No need to create memory block, so using this specific parameter as it stores memory on server

    dbCursor = conn.cursor()

    query = 'SELECT first_name FROM employees'
    try:
        dbCursor.execute(query)
        for row in dbCursor:
            yield row
    except Exception as e:
        traceback.print_exc()

i = 0
for row in getRows():
    print(row)
    i += 1
print(i)