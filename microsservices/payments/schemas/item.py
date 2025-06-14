from typing import Annotated, Optional
from decimal import Decimal
from pydantic import BaseModel, Field

class ItemNotaBase(BaseModel):
    n_item: Annotated[int, Field(...)]
    codigo_produto: Annotated[str, Field(..., max_length=50)]
    descricao_produto: Annotated[Optional[str], Field(None, max_length=200)]
    ncm: Annotated[Optional[str], Field(None, max_length=8)]
    cfop: Annotated[Optional[str], Field(None, max_length=4)]
    quantidade_comercial: Annotated[Decimal, Field(..., gt=0, max_digits=15, decimal_places=4)]
    unidade_comercial: Annotated[Optional[str], Field(None, max_length=10)]
    valor_unitario: Annotated[Decimal, Field(..., gt=0, max_digits=15, decimal_places=4)]
    valor_total_item: Annotated[Decimal, Field(..., max_digits=15, decimal_places=4)]
    valor_desconto: Annotated[Decimal, Field(..., max_digits=15, decimal_places=4)]
    origem_mercadoria: Annotated[Optional[int], Field(None)]
    cst_icms: Annotated[Optional[str], Field(None, max_length=3)]
    csosn: Annotated[Optional[str], Field(None, max_length=3)]
    aliquota_icms: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_icms: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    aliquota_ipi: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_ipi: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    aliquota_pis: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_pis: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    aliquota_cofins: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_cofins: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True

class ItemNotaRead(ItemNotaBase):
    id: int

class ItemNotaUpdate(BaseModel):
    n_item: Annotated[Optional[int], Field(None)]
    codigo_produto: Annotated[Optional[str], Field(None, max_length=50)]
    descricao_produto: Annotated[Optional[str], Field(None, max_length=200)]
    ncm: Annotated[Optional[str], Field(None, max_length=8)]
    cfop: Annotated[Optional[str], Field(None, max_length=4)]
    quantidade_comercial: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    unidade_comercial: Annotated[Optional[str], Field(None, max_length=10)]
    valor_unitario: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_total_item: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    valor_desconto: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    origem_mercadoria: Annotated[Optional[int], Field(None)]
    cst_icms: Annotated[Optional[str], Field(None, max_length=3)]
    csosn: Annotated[Optional[str], Field(None, max_length=3)]
    aliquota_icms: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_icms: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    aliquota_ipi: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_ipi: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    aliquota_pis: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_pis: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]
    aliquota_cofins: Annotated[Optional[Decimal], Field(None, max_digits=5, decimal_places=2)]
    valor_cofins: Annotated[Optional[Decimal], Field(None, max_digits=15, decimal_places=4)]

    class Config:
        orm_mode = True