const express = require("express");
require("./config/dbConfig");

// set up Express app
const app = express();
const server = require("http").createServer(app);

// import schema
const Questionnaire = require("./models/questionnaire");

app.get("/save-form-data", (req, res) => {});

server.listen(5000, () => {
  console.log("Initialized");
});
