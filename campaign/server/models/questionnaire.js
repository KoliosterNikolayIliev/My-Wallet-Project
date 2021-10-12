const mongoose = require("mongoose");

// create questionaire schema
const questionnaireSchema = new mongoose.Schema({
  author: String,
  quiz: Object,
});

module.exports = mongoose.model("Questionnaire", questionnaireSchema);
