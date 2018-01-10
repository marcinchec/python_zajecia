#zmodyfikuj poprzednie zadanie tak aby transakcja dodawania wartosci zostala anulowana.
#Przetestuj rowniez inne metody zarzadzajace transakcjami

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import  declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import NUMERIC

Base=declarative_base()

class Test(Base):
    __tablename__= 'test'
    id = Column(Integer, primary_key=True)
    name=Column(String(100))
    value=Column(String(100))

engine = create_engine('sqlite:///example.db',echo=True)

Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()

new_test = Test(
    id=8,
    name=u'ORM',
    value=u'sfsdfsdf'
)
session.add(new_test)

new_test = Test(
    id=10,
    name=u'saff',
    value=u'sadasd'
)
session.add(new_test)
session.rollback()
session.commit()