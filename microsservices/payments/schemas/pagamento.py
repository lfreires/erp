# schemas/pagamento.py
from typing import Annotated, Optional
from decimal import Decimal
from pydantic import BaseModel, Field

class PagamentoNotaBase(BaseModel):
    forma_pagamento: Annotated[Optional[str], Field(None, max_length=50)]
    valor_pago:       Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_troco:      Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True

class PagamentoNotaRead(PagamentoNotaBase):
    id: int

class PagamentoNotaUpdate(BaseModel):
    forma_pagamento: Annotated[Optional[str], Field(None, max_length=50)]
    valor_pago:       Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_troco:      Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True
