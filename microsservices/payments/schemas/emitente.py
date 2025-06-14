from typing import Annotated, Optional
from pydantic import BaseModel, Field

class EmitenteBase(BaseModel):
    cnpj_emitente: Annotated[str, Field(..., min_length=14, max_length=14)]
    razao_social_emitente: Annotated[str, Field(..., max_length=100)]
    inscricao_estadual_emitente: Annotated[Optional[str], Field(None)]
    endereco_emitente: Annotated[Optional[str], Field(None, max_length=200)]
    municipio_emitente: Annotated[Optional[str], Field(None, max_length=100)]
    uf_emitente: Annotated[Optional[str], Field(None, min_length=2, max_length=2)]

    class Config:
        orm_mode = True

class EmitenteRead(EmitenteBase):
    id: int

class EmitenteUpdate(BaseModel):
    cnpj_emitente: Annotated[Optional[str], Field(None, min_length=14, max_length=14)]
    razao_social_emitente: Annotated[Optional[str], Field(None, max_length=100)]
    inscricao_estadual_emitente: Annotated[Optional[str], Field(None)]
    endereco_emitente: Annotated[Optional[str], Field(None, max_length=200)]
    municipio_emitente: Annotated[Optional[str], Field(None, max_length=100)]
    uf_emitente: Annotated[Optional[str], Field(None, min_length=2, max_length=2)]

    class Config:
        orm_mode = True