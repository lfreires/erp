const fs = require("fs");
const path = require("path");
const dadosPath = path.join(__dirname, "../data/relatorios.json");

exports.listarRelatorios = (req, res) => {
  const data = JSON.parse(fs.readFileSync(dadosPath));
  const obra = data.find(o => o.obraId === req.params.id);
  if (!obra) return res.status(404).send("Obra não encontrada");
  res.render("index", { obra });
};

exports.verRelatorio = (req, res) => {
  const data = JSON.parse(fs.readFileSync(dadosPath));
  const obra = data.find(o => o.obraId === req.params.id);
  if (!obra) return res.status(404).send("Obra não encontrada");

  const relatorio = obra.relatorios.find(r => r.id === req.params.rid);
  if (!relatorio) return res.status(404).send("Relatório não encontrado");

  const { obra: filtroObra, dataFiltro, ordenacao } = req.query;

  res.render("detalhe", {
    obraNome: obra.obraNome,
    relatorio,
    filtros: {
      obra: filtroObra || "",
      dataFiltro: dataFiltro || "",
      ordenacao: ordenacao || "desc"
    }
  });
};

exports.listarTodasObras = (req, res) => {
  const data = JSON.parse(fs.readFileSync(dadosPath));
  const { obra, dataFiltro, ordenacao } = req.query;
  const resultados = [];

  data.forEach(o => {
    o.relatorios.forEach(r => {
      if (
        (!obra || o.obraId === obra) &&
        (!dataFiltro || r.data.startsWith(dataFiltro))
      ) {
        resultados.push({
          obraId: o.obraId,
          obraNome: o.obraNome,
          ...r
        });
      }
    });
  });

  resultados.sort((a, b) => {
    return ordenacao === "asc"
      ? new Date(a.data) - new Date(b.data)
      : new Date(b.data) - new Date(a.data);
  });

  res.render("home", {
    relatorios: resultados,
    filtroObra: obra || "",
    filtroData: dataFiltro || "",
    ordenacao: ordenacao || "desc" 
  });
};
