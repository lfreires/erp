from sqlalchemy import (
    Column, 
    Integer, 
    String, 
    DateTime, 
    SmallInteger,
    ForeignKey
)

from sqlalchemy.orm import relationship
from . import Base 

class NotaFiscal(Base):
    __tablename__ = 'notas_fiscais'

    id = Column(Integer, primary_key=True, autoincrement=True)
    emitente_id = Column(Integer, ForeignKey('emitentes.id'), nullable=False)
    chave_acesso = Column(String(44), unique=True, nullable=False)
    numero_nfe = Column(Integer, nullable=False)
    serie = Column(Integer, nullable=False)
    modelo = Column(String(2), nullable=False)
    data_emissao = Column(DateTime, nullable=False)
    data_saida_entrada = Column(DateTime, nullable=False)
    tipo_operacao = Column(SmallInteger, nullable=False)
    natureza_operacao = Column(String(100))
    finalidade_nfe = Column(String(20))

    itens = relationship("ItemNota", back_populates='nota', cascade="all, delete-orphan")
    destinatarios = relationship("Destinatario", back_populates="nota", cascade="all, delete-orphan")
    transporte = relationship("TransporteNota", back_populates="nota", uselist=False, cascade="all, delete-orphan")
    emitente = relationship("Emitente", back_populates="notas", uselist=False)
    totais = relationship("TotalNota", back_populates="nota", uselist=False, cascade="all, delete-orphan")
    pagamentos = relationship("PagamentoNota", back_populates="nota", cascade="all, delete-orphan")
    autorizacao = relationship("AutorizacaoNota", back_populates="nota", uselist=False, cascade="all, delete-orphan")