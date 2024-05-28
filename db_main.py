from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from models import table_ORM, Base

engine = create_engine(
    url=f"postgresql+psycopg2://postgres:1234@localhost:5432/db", #задаётся ссылка на бд
    echo=False, #сыпем все запросы в терминал (или же нет)
    pool_size=5, #5 подключений к бд максимум
    max_overflow=10 #если подключений свыше 5
)

session_factory = sessionmaker(engine)

# Функция создаёт таблицу в базе данных
def create_tables():
    Base.metadata.drop_all(engine) # можно убрать, если не надо предварительно удалить таблицу
    Base.metadata.create_all(engine)

# Вставляет в таблицу ссылку на обычное фото (с яндекс диска)
def insert_url(url):
    table = table_ORM(photo_url = url)
    with session_factory() as session:
        session.add(table)
        session.commit()

# Вставляет в таблицу ссылку на сегментированное фото (с яндекс диска)
def insert_segm_url(url, id):
    with session_factory() as session:
        obj = session.query(table_ORM).filter(table_ORM.id == id).first()
        obj.photo_url_segmented = url
        session.commit()

# Функция запрашивает ссылку на скачивание фото с яндекс диска
def get_url(id):
    with session_factory() as session:
        url = session.get(table_ORM, id)
        query = select(
            table_ORM.photo_url
            )
        result = session.execute(query)
        url = result.scalar()
        session.commit()
    return url