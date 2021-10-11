const mongoose = require("mongoose");

// create questionaire schema
const questionnaireSchema = new mongoose.Schema({
  author: String,
  response1: String,
  response2: String,
  response3: String,
});

module.exports = mongoose.model("Questionnaire", questionnaireSchema);
