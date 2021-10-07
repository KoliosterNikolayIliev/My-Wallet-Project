const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
require("./config/dbConfig");

// set up Express app
const app = express();
const server = require("http").createServer(app);

app.use(bodyParser.json());
app.use(cors());

// import schema
const Questionnaire = require("./models/questionnaire");

app.post("/save-form-data", (req, res) => {
  console.log(req.body);
});

server.listen(5000, () => {
  console.log("Initialized");
});
