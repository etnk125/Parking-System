const User = require("../model/user.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    // destructoring
    const { email, password } = req.body;
    if (!(email && password)) {
      return res.status(400).send({ msg: "all input are require" });
    }
    // may use req.body instead
    const resp = await User.findOne({ email: email, password: password });
    res.json(resp);
  } catch (err) {
    console.log(`ID or password incorrect`);
    console.error(err);
    return res.status(400).end();
  }
};
