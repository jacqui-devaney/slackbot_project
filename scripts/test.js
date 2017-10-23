var finalItemsList;

var PythonShell = require('python-shell');

PythonShell.run('scripts/scrape.py', function (err) {
  if (err) throw err;
  console.log('finished');

  var json = require('./filename.json'); //with path

  var popular_items;
  var listNum = 0;
  var arrayItemsList = [];

  for (var key in json) {
      if (json.hasOwnProperty(key)) {
          popular_items = json[key];
      }
  }

  popular_items.forEach(function(element) {
      listNum++;
      var popItemsList = listNum + ". " + element;
      arrayItemsList.push(popItemsList);
  });

  finalItemsList = arrayItemsList.join(" ");

  // console.log(finalItemsList);
});

module.exports = function(bot) {
  bot.hear(/top stories/, function(res) {
       return res.send((finalItemsList));
   });
};
