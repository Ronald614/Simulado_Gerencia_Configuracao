const fs = require('fs');
const path = require('path');

module.exports = (req, res) => {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  try {
    let filePath = path.join(__dirname, '..', 'artefatos', 'provas.json');
    if (!fs.existsSync(filePath)) {
      filePath = path.join(__dirname, '..', 'public', 'provas.json');
    }
    const fileContent = fs.readFileSync(filePath, 'utf-8');
    const data = JSON.parse(fileContent);

    const { id } = req.query;
    if (id) {
      const prova = data.provas.find(p => p.id === id);
      if (!prova) {
        return res.status(404).json({ erro: 'Prova nao encontrada', id });
      }
      return res.status(200).json(prova);
    }

    return res.status(200).json(data);
  } catch (error) {
    return res.status(500).json({ erro: 'Falha ao carregar dados das avaliacoes', detalhe: error.message });
  }
};
