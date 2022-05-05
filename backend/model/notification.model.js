const mongoose = require("mongoose");
const Schema = mongoose.Schema;
// create schema
const notificationSchema = new Schema({
  token: { type: String },
  message: { type: String },
});

module.exports = mongoose.model("notifications", notificationSchema);
