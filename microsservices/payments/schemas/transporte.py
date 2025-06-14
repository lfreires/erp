from typing import Annotated, Optional
from decimal import Decimal
from pydantic import BaseModel, Field

class TransporteNotaBase(BaseModel):
    modalidade_frete: Annotated[Optional[int], Field(None)]
    cnpj_transportadora: Annotated[Optional[str], Field(None, max_length=14)]
    nome_transportadora: Annotated[Optional[str], Field(None, max_length=100)]
    placa_veiculo: Annotated[Optional[str], Field(None, max_length=10)]
    uf_veiculo: Annotated[Optional[str], Field(None, min_length=2, max_length=2)]
    valor_frete: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True

class TransporteNotaRead(TransporteNotaBase):
    pass

class TransporteNotaUpdate(BaseModel):
    modalidade_frete: Annotated[Optional[int], Field(None)]
    cnpj_transportadora: Annotated[Optional[str], Field(None, max_length=14)]
    nome_transportadora: Annotated[Optional[str], Field(None, max_length=100)]
    placa_veiculo: Annotated[Optional[str], Field(None, max_length=10)]
    uf_veiculo: Annotated[Optional[str], Field(None, min_length=2, max_length=2)]
    valor_frete: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True