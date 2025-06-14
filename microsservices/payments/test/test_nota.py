from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importa Base e todos os Models do seu pacote models
from ..models import (
    Base,
    Emitente,
    NotaFiscal,
    ItemNota,
    Destinatario,
    TransporteNota,
    TotalNota,
    PagamentoNota,
    AutorizacaoNota
)

def main():
    # 1) Cria motor e tabelas em memória
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)

    # 2) Prepara sessão
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3) Cria emitente
    emit = Emitente(
        cnpj_emitente='12345678901234',
        razao_social_emitente='Empresa X Ltda',
        inscricao_estadual_emitente='123456789',
        endereco_emitente='Av. Paulista, 1000',
        municipio_emitente='São Paulo',
        uf_emitente='SP'
    )

    # 4) Cria nota já associada ao emitente
    nf = NotaFiscal(
        chave_acesso=''.join(['1']*44),
        numero_nfe=1,
        serie=1,
        modelo='55',
        data_emissao=datetime.now(),
        data_saida_entrada=datetime.now(),
        tipo_operacao=1,
        natureza_operacao='Venda de mercadorias',
        finalidade_nfe='normal',
        emitente=emit
    )

    # 5) Adiciona um item
    nf.itens.append(ItemNota(
        n_item=1,
        codigo_produto='PROD001',
        descricao_produto='Produto de Teste',
        ncm='10062000',
        cfop='5102',
        quantidade_comercial=2,
        unidade_comercial='UN',
        valor_unitario=50,
        valor_total_item=100,
        valor_desconto=0
    ))

    # 6) Adiciona destinatário
    nf.destinatarios.append(Destinatario(
        cnpj_cpf_destinatario='12345678000199',
        razao_social_destinatario='Cliente Y Comércio',
        inscricao_estadual_destinatario='987654321',
        endereco_destinatario='Rua das Flores, 200',
        municipio_destinatario='Rio de Janeiro',
        uf_destinatario='RJ'
    ))

    # 7) Adiciona transporte
    nf.transporte = TransporteNota(
        modalidade_frete=1,
        cnpj_transportadora='98765432000155',
        nome_transportadora='Transporte Z',
        placa_veiculo='ABC1234',
        uf_veiculo='SP',
        valor_frete=150
    )

    # 8) Adiciona totais
    nf.totais = TotalNota(
        valor_total_produtos=100,
        valor_frete=150,
        valor_seguro=0,
        valor_desconto=0,
        valor_total_nota=250,
        valor_icms_total=0,
        valor_ipi_total=0,
        valor_pis_total=0,
        valor_cofins_total=0
    )

    # 9) Adiciona pagamento
    nf.pagamentos.append(PagamentoNota(
        forma_pagamento='PIX',
        valor_pago=250,
        valor_troco=0
    ))

    # 10) Adiciona autorização
    nf.autorizacao = AutorizacaoNota(
        protocolo_autorizacao='PROTO123',
        data_autorizacao=datetime.now(),
        status_sefaz='autorizada',
        motivo_sefaz='',
        xml_integral='<xml></xml>'
    )

    # 11) Persiste no banco e dá commit
    session.add(nf)
    session.commit()

    # 12) Lê de volta e imprime
    nota = session.query(NotaFiscal).first()
    print(f"NotaFiscal ID: {nota.id} | Chave: {nota.chave_acesso}")
    print(f"Emitente: {nota.emitente.razao_social_emitente} ({nota.emitente.cnpj_emitente})\n")

    print("Itens:")
    for i in nota.itens:
        print(f"  {i.n_item}: {i.descricao_produto} – Qtd {i.quantidade_comercial} x {i.valor_unitario} = {i.valor_total_item}")

    print("\nDestinatários:")
    for d in nota.destinatarios:
        print(f"  {d.razao_social_destinatario} – {d.cnpj_cpf_destinatario}")

    print(f"\nTransporte: {nota.transporte.nome_transportadora} – Frete: {nota.transporte.valor_frete}")
    print(f"Totais: Produtos={nota.totais.valor_total_produtos} Frete={nota.totais.valor_frete} TotalNota={nota.totais.valor_total_nota}\n")

    print("Pagamentos:")
    for p in nota.pagamentos:
        print(f"  {p.forma_pagamento} – Pago: {p.valor_pago} Troco: {p.valor_troco}")

    print(f"\nAutorização: {nota.autorizacao.status_sefaz} – Protocolo: {nota.autorizacao.protocolo_autorizacao}")

if __name__ == '__main__':
    main()