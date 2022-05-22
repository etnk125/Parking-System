const Parking = require("../model/parking.model");
const Notification = require("../model/notification.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const { date } = await Parking.findOne({ name: req.params.name });
    const resp = await Parking.updateOne(
      { name: req.params.name },
      { token: req.body?.token || "", date: date ? date : Date.now() }
    );
    await Notification.create({
      token: req.body?.token,
      message: `your parking number is ${req.params.name}`,
    });
    res.json(resp);
  } catch (err) {
    console.log(err);
  }
};
