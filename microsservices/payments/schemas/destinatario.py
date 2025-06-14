from typing import Annotated, Optional
from pydantic import BaseModel, Field

class DestinatarioBase(BaseModel):
    cnpj_cpf_destinatario: Annotated[str, Field(..., min_length=11, max_length=14)]
    razao_social_destinatario: Annotated[str, Field(..., max_length=100)]
    inscricao_estadual_destinatario: Annotated[Optional[str], Field(None)]
    endereco_destinatario: Annotated[Optional[str], Field(None, max_length=200)]
    municipio_destinatario: Annotated[Optional[str], Field(None, max_length=100)]
    uf_destinatario: Annotated[Optional[str], Field(None, min_length=2, max_length=2)]

    class Config:
        orm_mode = True

class DestinatarioRead(DestinatarioBase):
    id: int

class DestinatarioUpdate(BaseModel):
    cnpj_cpf_destinatario: Annotated[Optional[str], Field(None, min_length=11, max_length=14)]
    razao_social_destinatario: Annotated[Optional[str], Field(None, max_length=100)]
    inscricao_estadual_destinatario: Annotated[Optional[str], Field(None)]
    endereco_destinatario: Annotated[Optional[str], Field(None, max_length=200)]
    municipio_destinatario: Annotated[Optional[str], Field(None, max_length=100)]
    uf_destinatario: Annotated[Optional[str], Field(None, min_length=2, max_length=2)]

    class Config:
        orm_mode = True