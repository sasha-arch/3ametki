from sqlalchemy import Column, Integer, String, create_engine, update
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class Note(Base):
    def __init__(self, text='Текст заметки', lable='Новая заметка'):
        self.text = text
        self.lable = lable

    __tablename__ = 'notes'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    text = Column(String(700), default='Текст заметки')
    lable = Column(String(100), default='Новая заметка')

db_connect_string = 'sqlite:///notes.db'
engine = create_engine(db_connect_string)
Session = sessionmaker(bind=engine)


class DbCommands():

    db = Session()

    @staticmethod
    def get_all_notes():
        return DbCommands.db.query(Note).all()

    @staticmethod
    def create_note():
        new_note = Note()
        DbCommands.db.add(new_note)
        DbCommands.db.commit()
        return new_note

    @staticmethod
    def delete_note(id):
        DbCommands.db.query(Note).filter_by(id=id).delete()
        DbCommands.db.commit()

    @staticmethod
    def update_note(id, text):
        note = DbCommands.db.query(Note).get(id)
        note.text = text
        DbCommands.db.commit()