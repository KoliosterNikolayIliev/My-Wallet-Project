const express = require("express");

const app = express();
const server = require("http").createServer(app);

app.get("/save-form-data", (req, res) => {
  res.send("Hello World!");
});

server.listen(5000, () => {
  console.log("Initialized");
});
