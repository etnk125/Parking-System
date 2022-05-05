// connect to mongodb atlas
require("./config/database").connect();

const express = require("express");

// import controller
const reserveController = require("./controller/reserve.controller");
const checkoutController = require("./controller/checkout.controller");
const getTokenController = require("./controller/getToken.controller");
const loginController = require("./controller/login.controller");
const registerController = require("./controller/register.controller");

// incase using bcryptjs
// const bcrypt = require("bcryptjs");

const app = express();

// https://www.geeksforgeeks.org/express-js-express-json-function/
app.use(express.json());

const cors = require("cors");
app.use(cors());

const bodyParser = require("body-parser");
app.use(bodyParser.json());
app.use(
  bodyParser.urlencoded({
    extended: false,
  })
);

// frontend
// reserve
app.post("/reserve/:name", reserveController);
// checkout
app.post("/checkout/:name", checkoutController);
// login
app.post("/login", loginController);
// register
app.post("/register", registerController);

// backend
// get token
app.get("/token/:name", getTokenController);

module.exports = app;
