const express = require("express");
const router = express.Router();
const controller = require("../controllers/entradaController");

router.post("/entrada", controller.receberRelatorio);

module.exports = router;
