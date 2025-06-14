const express = require("express");
const path = require("path");
const app = express();
const obrasRoutes = require("./routes/obras");
const entradaRoute = require("./routes/entrada");

app.use("/", entradaRoute);
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.static("public"));
app.use("/", obrasRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log("Work Docs rodando na porta", PORT);
});
