const Parking = require("../model/parking.model");
const Notification = require("../model/notification.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const resp = await Parking.findOne({ name: req.params.name });
    await Parking.updateOne(
      { name: req.params.name },
      { token: "", date: null }
    );
    const diff = Date.now() - resp.date;
    const hours = Math.floor(diff / (1000 * 60 * 60));
    const minuit = Math.floor(diff / (1000 * 60)) % 60;
    const sec = Math.floor(diff / 1000) % 60;
    await Notification.create({
      token: resp.token,
      message: `you have been parked for ${hours} hours, ${minuit} minutes, ${sec} seconds`,
    });
    res.json(resp);
  } catch (err) {
    console.log(err);
  }
};
