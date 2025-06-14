const fs = require("fs");
const path = require("path");
const dadosPath = path.join(__dirname, "../data/relatorios.json");

exports.receberRelatorioDoBot = (req, res) => {
  try {
    const {
      obraId,
      obraNome,
      data,
      usuario,
      descricao,
      imagem
    } = req.body;

    if (!obraId || !obraNome || !data || !usuario || !descricao) {
      return res.status(400).json({ erro: "Campos obrigatórios ausentes." });
    }

    const relatoriosData = JSON.parse(fs.readFileSync(dadosPath));

    let obra = relatoriosData.find(o => o.obraId === obraId);

    if (!obra) {
      obra = {
        obraId,
        obraNome,
        relatorios: []
      };
      relatoriosData.push(obra);
    }

    const novoRelatorio = {
      id: "r" + Date.now(),
      data,
      usuario,
      descricao,
      imagem: imagem || null
    };

    obra.relatorios.push(novoRelatorio);

    fs.writeFileSync(dadosPath, JSON.stringify(relatoriosData, null, 2));
    return res.json({ status: "ok", mensagem: "Relatório salvo com sucesso" });
  } catch (erro) {
    console.error(erro);
    return res.status(500).json({ erro: "Erro ao processar relatório." });
  }
};
