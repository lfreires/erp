const express = require("express");
const router = express.Router();
const controller = require("../controllers/obrasController");

router.get("/obra/:id", controller.listarRelatorios);
router.get("/obra/:id/relatorio/:rid", controller.verRelatorio);
router.get("/", controller.listarTodasObras);

module.exports = router;
