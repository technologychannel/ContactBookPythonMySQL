import mysql.connector
class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        
        self.conn = None
        self.cursor = None
        self.connect()
    
    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
            print("Connected to the database")
        except:
            print("Error connecting to the database")
    
    def add_person(self, name, phone):
        sql = "INSERT INTO persons (name, phone) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, phone))
        self.conn.commit()
        print("Person added successfully")
        