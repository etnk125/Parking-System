const Parking = require("../model/parking.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const parking = await Parking.findOne({ name: req.params.name });
    res.json(parking);
  } catch (err) {
    console.log(`Error to find parking : ${res.params.name}`);
    console.error(err);
  }
};
