const express = require("express");
require("./config/dbConfig");

const app = express();
const server = require("http").createServer(app);

app.get("/save-form-data", (req, res) => {});

server.listen(5000, () => {
  console.log("Initialized");
});
