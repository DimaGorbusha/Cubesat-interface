import psycopg2


class DB:
    def DB_connect(self):
        self.connection = psycopg2.connect(dbname='database', 
                                    user='db_user', 
                                    password='mypassword',
                                    host='localhost')


    def __init__(self):
        self.DB_connect()
        self.connection.close()


    def create_table(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.autocommit = True
                cursor.execute("CREATE TABLE IF NOT EXISTS tests \
                (test_id SMALLINT AUTO_INCREMENT PRIMARY KEY, \
                duration SMALLINT, brh_opn SMALLINT, brh_cls SMALLINT, \
                before_time INT, status BOOLEAN, time_after_start SMALLINT, \
                akb_voltage DOUBLE, pressure DOUBLE, tank_temp DOUBLE, engine_wall_temp DOUBLE, \
                valve_temp DOUBLE, valve_current DOUBLE, heating_current DOUBLE)")

        finally:
            self.connection.close()

    
    def insert_data(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.autocommit = True
            # код вставки новых данных
        finally:
            self.connection.close()

    
    def update_data(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.autocommit = True
            # код апдейта данных
        finally:
            self.connection.close()

    
    def export_data_json(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                cursor.autocommit = True
            # экспорт джсон пакета по идентификатору
        finally:
            self.connection.close()
