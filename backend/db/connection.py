from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, Session
from typing import Iterator

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


db_connection = DBConnection()
