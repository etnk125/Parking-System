const Parking = require("../model/parking.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const parking = await Parking.find({});
    // res.json(parking.map((slot) => slot.token || ""));
    res.json(parking);
  } catch (err) {
    console.log(`Error to find token`);
    console.error(err);
  }
};
