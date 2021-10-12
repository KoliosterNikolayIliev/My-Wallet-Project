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
  let author = req.body["author"];
  let quiz = req.body["quiz"];

  let questionnaireResponse = new Questionnaire({
    author,
    quiz,
  });

  questionnaireResponse.save((err, res) => {
    if (err) return console.log(err);
  });

  res.status(201);
  res.end();
});

server.listen(5000, () => {
  console.log("Initialized");
});
