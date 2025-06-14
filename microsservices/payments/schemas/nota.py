from typing import Annotated, Optional, List
from datetime import datetime
from pydantic import BaseModel, Field

from .item import ItemNotaBase, ItemNotaRead
from .destinatario import DestinatarioBase, DestinatarioRead
from .emitente import EmitenteBase, EmitenteRead
from .transporte import TransporteNotaBase, TransporteNotaRead
from .total import TotalNotaBase, TotalNotaRead
from .pagamento import PagamentoNotaBase, PagamentoNotaRead
from .autorizacao import AutorizacaoNotaBase, AutorizacaoNotaRead

class NotaFiscalBase(BaseModel):
    chave_acesso: Annotated[str, Field(..., min_length=44, max_length=44)]
    numero_nfe: Annotated[int, Field(...)]
    serie: Annotated[int, Field(...)]
    modelo: Annotated[str, Field(..., max_length=2)]
    data_emissao: Annotated[datetime, Field(...)]
    data_saida_entrada: Annotated[datetime, Field(...)]
    tipo_operacao: Annotated[int, Field(...)]
    natureza_operacao: Annotated[Optional[str], Field(None)]
    finalidade_nfe: Annotated[Optional[str], Field(None)]
    emitente_id: Annotated[int, Field(...)]

    class Config:
        orm_mode = True

class NotaFiscalCreate(NotaFiscalBase):
    itens: Annotated[List[ItemNotaBase], Field(...)]
    destinatarios: Annotated[List[DestinatarioBase], Field(...)]
    transporte: Annotated[TransporteNotaBase, Field(...)]
    totais: Annotated[TotalNotaBase, Field(...)]
    pagamentos: Annotated[List[PagamentoNotaBase], Field(...)]
    autorizacao: Annotated[AutorizacaoNotaBase, Field(...)]

class NotaFiscalRead(NotaFiscalBase):
    id: int
    itens: Annotated[List[ItemNotaRead], Field(...)]
    destinatarios: Annotated[List[DestinatarioRead], Field(...)]
    transporte: Annotated[TransporteNotaRead, Field(...)]
    totais: Annotated[TotalNotaRead, Field(...)]
    pagamentos: Annotated[List[PagamentoNotaRead], Field(...)]
    autorizacao: Annotated[AutorizacaoNotaRead, Field(...)]

    class Config:
        orm_mode = True

class NotaFiscalUpdate(BaseModel):
    numero_nfe: Annotated[Optional[int], Field(None)]
    serie: Annotated[Optional[int], Field(None)]
    modelo: Annotated[Optional[str], Field(None, max_length=2)]
    data_emissao: Annotated[Optional[datetime], Field(None)]
    data_saida_entrada: Annotated[Optional[datetime], Field(None)]
    tipo_operacao: Annotated[Optional[int], Field(None)]
    natureza_operacao: Annotated[Optional[str], Field(None)]
    finalidade_nfe: Annotated[Optional[str], Field(None)]
    emitente_id: Annotated[Optional[int], Field(None)]

    class Config:
        orm_mode = True