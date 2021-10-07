const { MongoClient } = require("mongodb");
const uri =
  "mongodb+srv://trivialAdmin:OZjhinrBmHRGiXHk@3vial.9mih9.mongodb.net/3vial-Campaign?retryWrites=true&w=majority";

// connect to db
mongoose.connect(uri, { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;
db.on("error", console.error.bind(console, "connection error:"));
db.once("open", () => {
  console.log("Connected to db");
});
