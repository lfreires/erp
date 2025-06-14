from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    SmallInteger,
    ForeignKey,
    CHAR,
    Numeric
)

from sqlalchemy.orm import relationship
from . import Base 

class TransporteNota(Base):
    __tablename__ = 'transporte_nota'

    nota_id = Column(Integer, ForeignKey('notas_fiscais.id'), primary_key=True)
    modalidade_frete = Column(SmallInteger)                # 0=sem frete,1=emitente,2=destinatário...
    cnpj_transportadora = Column(String(14))
    nome_transportadora = Column(String(100))
    placa_veiculo = Column(String(10))
    uf_veiculo = Column(CHAR(2))
    valor_frete = Column(Numeric(15,4))

    nota = relationship("NotaFiscal", back_populates="transporte")