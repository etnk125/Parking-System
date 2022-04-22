const Parking = require("../model/parking.model");
const User = require("../model/user.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const resp = await Parking.findOne({ name: req.params.name });
    await Parking.updateOne(
      { name: req.params.name },
      { token: "", date: null }
    );
    res.json(resp);
  } catch (err) {
    console.log(err);
  }
};
