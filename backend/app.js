// connect to mongodb atlas
require("./config/database").connect();

const express = require("express");

// import controller
const reserveController = require("./controller/reserve.controller");
const checkoutController = require("./controller/checkout.controller");
const getTokenController = require("./controller/getToken.controller");
const loginController = require("./controller/login.controller");
const registerController = require("./controller/register.controller");
// const deleteController = require("./controller/delete.controller");
// const loginController = require("./controller/login.controller");

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

app.post("/reserve/:name/:token", reserveController);
app.post("/checkout/:name", checkoutController);

// // add one contact
// app.post("/contacts", postController);
// // edit one contact
// app.post("/contacts/:id", editController);

// login
app.post("/login", loginController);
// register
app.post("/register", registerController);
// app.get("/login", loginController);
// get request should not have body
// get work in postman but not work in browser

module.exports = app;
