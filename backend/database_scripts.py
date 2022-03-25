import psycopg2


class DB:
    def DB_connect(self):
        self.connection = psycopg2.connect(dbname='database', 
                                    user='postgres', 
                                    password='$NS$//1907',
                                    host='localhost')


    def __init__(self):
        self.DB_connect()
        self.connection.close()

    def create_table(self):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                create_tb_query = """CREATE TABLE IF NOT EXISTS tbl_with_tests (
                    test_id BIGSERIAL PRIMARY KEY,
                    duration INTEGER, 
                    brh_opn INTEGER, 
                    brh_cls INTEGER, 
                    before_time INTEGER, 
                    status BOOLEAN, 
                    time_after_start INTEGER, 
                    akb_voltage DOUBLE PRECISION, 
                    pressure DOUBLE PRECISION, 
                    tank_temp DOUBLE PRECISION, 
                    engine_wall_temp DOUBLE PRECISION, 
                    valve_temp DOUBLE PRECISION, 
                    valve_current DOUBLE PRECISION, 
                    heating_current DOUBLE PRECISION)"""
                cursor.execute(create_tb_query)

        finally:
            self.connection.close()

    
    def insert_data(self, duration, brh_opn, brh_cls, before_time, status, time_after_start,
                akb_voltage, press, tank_temp, engine_wall_temp, valve_temp,
                valve_current, heating_current):
        self.DB_connect()
        try:
            with self.connection.cursor() as cursor:
                self.connection.autocommit = True
                insert_data_query = """INSERT INTO tbl_with_tests (duration, brh_opn, brh_cls, before_time, status, time_after_start,
                akb_voltage, press, tank_temp, engine_wall_temp, valve_temp,
                valve_current, heating_current) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                cursor.execute(insert_data_query, (duration, brh_opn, brh_cls, before_time, status,
                            time_after_start, akb_voltage, press, tank_temp, engine_wall_temp,
                            valve_temp, valve_current, heating_current))

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
