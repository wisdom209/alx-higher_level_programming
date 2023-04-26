#!/usr/bin/node
/* prints all characters of a Star Wars movie: */
const request = require('request');
// const util = require('util');

const personList = [];
// const requestPromise = util.promisify(request);
if (process.argv.length >= 3) {
  const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

  request(filmUrl, (err, response, body) => {
    if (err == null) {
      body = JSON.parse(body);
      const characters = body.characters;
      for (const charUrl in characters) {
        personList.push(characters[charUrl]);
      }
    }
    const allChars = personList.map(url => {
      return new Promise((resolve, reject) => {
        request(url, (e, res, bd) => {
          if (e) {
            reject(e);
          } else {
            resolve(JSON.parse(bd).name);
          }
        });
      });
    });

    Promise.all(allChars)
      .then(results => {
        for (const x in results) {
          console.log(results[x]);
        }
      })
      .catch(err => {
        console.log(err);
      });
  });
}
