import MySQLdb
import MySQLdb.cursors as cursors
import traceback

class db_connect:
    def __init__(self, uname, password, db_name):
        self.uname = uname 
        self.password = password
        self.db_name = db_name

    def getRows(self, query):
        conn = MySQLdb.connect(host="localhost",user=self.uname,
                    passwd=self.password,db=self.db_name, cursorclass=cursors.SSCursor)
        # cursorclass = cursors.SSCursor. No need to create memory block, so using this specific parameter as it stores memory on server

        dbCursor = conn.cursor()

        try:
            dbCursor.execute(query)
            for row in dbCursor:
                yield row
        except Exception as e:
            traceback.print_exc()

if __name__ == '__main__':
    db_instance = db_connect('root', '', 'employees')
    query = 'SELECT first_name, salary, from_date FROM employees INNER JOIN salaries on employees.emp_no = salaries.emp_no'
    i = 0
    for row in db_instance.getRows(query):
        print(row)
        i += 1
    print('Number of rows: '+str(i))