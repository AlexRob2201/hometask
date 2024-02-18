import mysql.connector

class MySql:
    def __init__(self, host, user, password):
        max_retries = 30
        retries = 0
        while True:
            try:
                self.mysql_connect = mysql.connector.connect(
                host=host,
                user=user,
                password=password
                #database=database
                )   
                self.mysql_cursor = self.mysql_connect.cursor()
                print(f'Connect to database successfully')
                break
            except Exception as e:
                print(f"Waiting for MySQL...{e}")
                time.sleep(1)
                retries += 1

                if retries >= max_retries:
                    print("Unable to connect to MySQL. Exiting.")
                    exit(1)
