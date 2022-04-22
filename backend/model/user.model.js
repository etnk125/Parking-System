const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// need not to hash anymore bc. contact doesn't store password
// const bcrypt = require("bcryptjs");
const userSchema = new Schema({
  email: { type: String },
  password: { type: String },
  token: { type: String },
});

module.exports = mongoose.model("users", userSchema);
