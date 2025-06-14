# schemas/total.py
from typing import Annotated, Optional
from decimal import Decimal
from pydantic import BaseModel, Field

class TotalNotaBase(BaseModel):
    valor_total_produtos: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_frete:           Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_seguro:          Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_desconto:        Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_total_nota:      Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_icms_total:      Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_ipi_total:       Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_pis_total:       Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_cofins_total:    Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True

class TotalNotaRead(TotalNotaBase):
    pass

class TotalNotaUpdate(BaseModel):
    valor_total_produtos: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_frete:           Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_seguro:          Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_desconto:        Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_total_nota:      Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_icms_total:      Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_ipi_total:       Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_pis_total:       Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_cofins_total:    Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True
