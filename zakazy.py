import datetime
import sqlalchemy
from sqlalchemy import orm
from db_session import SqlAlchemyBase


class Zakazy(SqlAlchemyBase):
    __tablename__ = 'zakazy'


    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    Name = sqlalchemy.Column(sqlalchemy.String)
    Phone = sqlalchemy.Column(sqlalchemy.String)
    Kol_vo = sqlalchemy.Column(sqlalchemy.Integer)
    Tyr_id = sqlalchemy.Column(sqlalchemy.Integer)