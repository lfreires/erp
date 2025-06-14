from sqlalchemy import (
    Column, 
    Integer,
    ForeignKey,
    Numeric
)

from sqlalchemy.orm import relationship
from . import Base 

class TotalNota(Base):
    __tablename__ = 'totais_nota'

    nota_id = Column(Integer, ForeignKey('notas_fiscais.id'), primary_key=True)
    valor_total_produtos = Column(Numeric(15,4))
    valor_frete = Column(Numeric(15,4))
    valor_seguro = Column(Numeric(15,4))
    valor_desconto = Column(Numeric(15,4))
    valor_total_nota = Column(Numeric(15,4))
    valor_icms_total = Column(Numeric(15,4))
    valor_ipi_total = Column(Numeric(15,4))
    valor_pis_total = Column(Numeric(15,4))
    valor_cofins_total = Column(Numeric(15,4))

    nota = relationship("NotaFiscal", back_populates="totais")