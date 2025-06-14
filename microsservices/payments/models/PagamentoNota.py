from sqlalchemy import (
    Column, 
    Integer,
    ForeignKey,
    Numeric,
    String
)

from sqlalchemy.orm import relationship
from . import Base 

class PagamentoNota(Base):
    __tablename__ = 'pagamentos_nota'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota_id = Column(Integer, ForeignKey('notas_fiscais.id'), nullable=False)
    forma_pagamento = Column(String(50))
    valor_pago = Column(Numeric(15,4))
    valor_troco = Column(Numeric(15,4))

    nota = relationship("NotaFiscal", back_populates="pagamentos")