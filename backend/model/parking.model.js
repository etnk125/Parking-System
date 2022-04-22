const mongoose = require("mongoose");
const Schema = mongoose.Schema;
// create schema
const parkingSchema = new Schema({
  name: { type: String, required: true },
  token: { type: String },
  date: { type: Date },
});

module.exports = mongoose.model("parkings", parkingSchema);
