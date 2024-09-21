from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    sessionmaker,

)

# Veritabanına bağlanmayı sağlayan motorun oluşturulması
engine = create_engine(
    "sqlite:///app.db",
    echo=True,  # Bu argüman sayesinde sorgular terminalde (sys.stdout) görüntülenecek
)

# Fabrika tasarım deseni temelinde oturum yapılandırmasının oluşturulması
Session = sessionmaker(bind=engine)


# Modeller için temel sınıfın deklarasyonu
# ORM'deki ilişkilerin gerçekleştirilmesi için gerekli
class Base(DeclarativeBase):
    ...


def create_db():
    '''
    Meta verilerin başlatılması,
    veritabanı yoksa oluşturur,
     modellerden (Base'den türetilen) tablolara göre veritabanı oluşturur,
    eğer hiçbiri yoksa
    '''
    Base.metadata.create_all(engine)


def drop_db():
    '''
    Meta verilerin yok edilmesi,
    veritabanı varsa siler,
    tüm tabloları siler
    '''
    Base.metadata.drop_all(engine)