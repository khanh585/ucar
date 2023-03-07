from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from typing import Iterator
from db.base import Base

SQLALCHEMY_DATABASE_URL = "postgresql://myuser:mypassword@localhost:5430/ucar-01"



class DBConnection():

    def __init__(self):
        self.engine = create_engine(
            SQLALCHEMY_DATABASE_URL
        )

    def get_session(self) -> Iterator[Session]:
        Session  = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        session = Session()
        try:
            yield session
            session.commit()
        except Exception as exc:
            print(exc)
            session.rollback()
            raise exc
        finally:
            session.close()

    def check_connection(self):

        Session  = sessionmaker(autocommit=True, bind=self.engine)
        session = Session()
        session.execute(text("SELECT 1;"))

    def check_table_exists(self, table_name, schema):
        Session  = sessionmaker(autocommit=True, bind=self.engine)
        session = Session()
        sql = text("""SELECT COUNT(table_name)
                FROM information_schema.tables
                WHERE table_schema = '{schema}' AND table_name = '{table_name}';""")
        result = session.execute(sql)
        for row in result:
            return row[0] == 1
    
    def create_table_model(self):
        if (not self.check_table_exists('car_brand', 'ucar-01') 
            and not self.check_table_exists('car_model', 'ucar-01')):
            Base.metadata.create_all(self.engine)
            print("CREATED TABLE")




db_connection = DBConnection()
