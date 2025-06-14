from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    CHAR,
    ForeignKey
)

from sqlalchemy.orm import relationship
from . import Base 

class Destinatario(Base):
    __tablename__ = 'destinatarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota_id = Column(Integer, ForeignKey('notas_fiscais.id'), nullable=False)
    cnpj_cpf_destinatario = Column(String(14), nullable=False)
    razao_social_destinatario = Column(String(100), nullable=False)
    inscricao_estadual_destinatario = Column(String(20))
    endereco_destinatario = Column(String(200))
    municipio_destinatario = Column(String(100))
    uf_destinatario = Column(CHAR(2))

    nota = relationship("NotaFiscal", back_populates="destinatarios")