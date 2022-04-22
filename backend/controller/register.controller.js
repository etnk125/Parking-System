const User = require("../model/user.model");

module.exports = async (req, res) => {
  const { email, password, token } = req.body;
  if (!(email && password && token)) {
    return req.status(400).json({ message: "all input are require!" });
  }
  const user = await User.findOne({ email: email });

  if (!!user) {
    return req.status(400).json({ message: "this email already taken!" });
  }

  User.create(req.body, (err, user) => {
    if (err) {
      console.log(`Error to add user `);
      console.error(err);
      return res.send(err);
    }
    res.json(user);
  });
};
