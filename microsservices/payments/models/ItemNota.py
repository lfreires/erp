from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    Numeric,
    ForeignKey
)

from sqlalchemy.orm import relationship
from . import Base 

class ItemNota(Base):
    __tablename__ = 'itens_nota'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota_id = Column(Integer, ForeignKey('notas_fiscais.id'), nullable=False)
    n_item = Column(Integer, nullable=False)               # seq do item
    codigo_produto = Column(String(50), nullable=False)
    descricao_produto = Column(String(200))
    ncm = Column(String(8))
    cfop = Column(String(4))
    quantidade_comercial = Column(Numeric(15,4))
    unidade_comercial = Column(String(10))
    valor_unitario = Column(Numeric(15,4))
    valor_total_item = Column(Numeric(15,4))
    valor_desconto = Column(Numeric(15,4))

    nota = relationship(
        "NotaFiscal", # Se relaciona com NotaFiscal
        back_populates="itens") # Nome do atribudo que se relaciona em NotaFiscal