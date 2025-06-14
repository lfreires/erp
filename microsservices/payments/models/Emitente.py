from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    CHAR
)

from sqlalchemy.orm import relationship
from . import Base 

class Emitente(Base):
    __tablename__ = 'emitentes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cnpj_emitente = Column(String(14), nullable=False)
    razao_social_emitente = Column(String(100), nullable=False)
    inscricao_estadual_emitente = Column(String(20))
    endereco_emitente = Column(String(200))
    municipio_emitente = Column(String(100))
    uf_emitente = Column(CHAR(2))

    notas = relationship("NotaFiscal", back_populates="emitente")