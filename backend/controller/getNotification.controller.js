const notification = require("../model/notification.model");

// using promise when searching
module.exports = async (req, res) => {
  try {
    const notificationList = await notification.find({});
    notification.deleteMany({}, (err, _) => {
      if (err) {
        console.log(`Error to delete notification `);
        console.error(err);
      }
    });
    res.json(notificationList);
  } catch (err) {
    console.log(`something went wrong`);
    console.error(err);
  }
};
