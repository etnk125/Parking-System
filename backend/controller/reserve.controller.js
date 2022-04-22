const Parking = require("../model/parking.model");
const User = require("../model/user.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const resp = await Parking.updateOne(
      { name: req.params.name },
      { token: req.params.token, date: Date.now() }
    );
    res.json(resp);
  } catch (err) {
    console.log(err);
  }
};
