# schemas/autorizacao.py
from typing import Annotated, Optional
from datetime import datetime
from pydantic import BaseModel, Field

class AutorizacaoNotaBase(BaseModel):
    protocolo_autorizacao: Annotated[Optional[str], Field(None)]
    data_autorizacao:      Annotated[Optional[datetime], Field(None)]
    status_sefaz:          Annotated[Optional[str], Field(None)]
    motivo_sefaz:          Annotated[Optional[str], Field(None)]
    xml_integral:          Annotated[Optional[str], Field(None)]

    class Config:
        orm_mode = True

class AutorizacaoNotaRead(AutorizacaoNotaBase):
    pass

class AutorizacaoNotaUpdate(BaseModel):
    protocolo_autorizacao: Annotated[Optional[str], Field(None)]
    data_autorizacao:      Annotated[Optional[datetime], Field(None)]
    status_sefaz:          Annotated[Optional[str], Field(None)]
    motivo_sefaz:          Annotated[Optional[str], Field(None)]
    xml_integral:          Annotated[Optional[str], Field(None)]

    class Config:
        orm_mode = True
