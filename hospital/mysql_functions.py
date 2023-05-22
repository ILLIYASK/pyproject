from mysql import connector

class MysqlFunction:
    def __init__(self):
        self.my_db=connector.connect(host='localhost',user='root',password='root1234',
                                     database='hms')

    def create_account(self,usr_name,password):

        self.my_cursor=self.my_db.cursor()
        query="insert into login_credential values(%s,%s)"
        value=(usr_name,password)
        self.my_cursor.execute(query,value)
        self.my_db.commit()
        self.my_cursor.close()


    def show_table(self):
        self.my_cursor=self.my_db.cursor()
        self.my_cursor.execute('select  * from login_credential')
        for i in self.my_cursor:
            print(i)
        self.my_cursor.close()


if __name__=="__main__":
    print('hi')