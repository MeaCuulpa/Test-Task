from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

# Простейшая таблица для сохранение ссылок с яндекс диска
class table_ORM(Base):
    __tablename__ = 'photos'
    id: Mapped[int] = mapped_column(primary_key=True)
    photo_url: Mapped[str]
    photo_url_segmented: Mapped[str] = mapped_column(nullable=True)