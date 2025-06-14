from sqlalchemy import (
    Column, 
    Integer,
    ForeignKey,
    String,
    DateTime,
    Text
)

from . import Base 
from sqlalchemy.orm import relationship

class AutorizacaoNota(Base):
    __tablename__ = 'autorizacao_nota'

    nota_id = Column(Integer, ForeignKey('notas_fiscais.id'), primary_key=True)
    protocolo_autorizacao = Column(String(30))
    data_autorizacao = Column(DateTime)
    status_sefaz = Column(String(20))
    motivo_sefaz = Column(String(200))
    xml_integral = Column(Text)

    nota = relationship("NotaFiscal", back_populates="autorizacao")