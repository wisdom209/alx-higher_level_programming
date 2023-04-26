#!/usr/bin/node
/* computes the number of tasks completed by user id. */
const request = require('request');

if (process.argv.length >= 3) {
  const url = process.argv[2];
  const newObj = {};
  request(url, (err, response, body) => {
    body = JSON.parse(body);

    const userIds = new Set();
    if (err == null) {
      for (const x in body) {
        userIds.add(body[x].userId);
      }
      userIds.forEach(val => {
        let completed = 0;
        for (const x in body) {
          if (body[x].userId === val && body[x].completed === true) {
            completed++;
          }
        }
        newObj[val] = completed;
      });

      let jsonString = JSON.stringify(newObj, null, 2);
      jsonString = jsonString.slice(3, -2);
      jsonString = '{' + jsonString + ' }';
      jsonString = jsonString.replace(/"/g, "'");
      console.log(jsonString);
    }
  });
}
