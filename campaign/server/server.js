const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const mailchimp = require("@mailchimp/mailchimp_marketing");
require("./config/dbConfig");
require("dotenv").config();

const MAILCHIMP_KEY = process.env.MAILCHIMP_KEY;

// set up Express app
const app = express();
const server = require("http").createServer(app);
mailchimp.setConfig({
  apiKey: MAILCHIMP_KEY,
  server: "us5",
});

app.use(bodyParser.json());
app.use(cors());

// import schema
const Questionnaire = require("./models/questionnaire");

const getLists = async () => {
  const lists = await mailchimp.lists.getAllLists();
  return lists["lists"][0]["stats"]["member_count_since_send"];
};

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

// return the number of subscribers of the mailing list
app.get("/subscribers", (req, res) => {
  const response = getLists().then((data) => {
    res.json({
      count: data,
    });
  });
});

server.listen(5000, () => {
  console.log("Initialized");
});
