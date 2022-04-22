const Parking = require("../model/parking.model");
const User = require("../model/user.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const { date } = await Parking.findOne({ name: req.params.name });
    const resp = await Parking.updateOne(
      { name: req.params.name },
      { token: req.params.token, date: date ? date : Date.now() }
    );
    res.json(resp);
  } catch (err) {
    console.log(err);
  }
};
