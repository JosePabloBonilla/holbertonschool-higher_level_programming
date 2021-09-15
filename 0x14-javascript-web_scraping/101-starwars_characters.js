#!/usr/bin/node
const request = require('request');
request(`https://swapi-api.hbtn.io/api/films/${process.argv[2]}`, (err, response, body) => {
  if (err) throw err;
  else {
    send(JSON.parse(body).characters, 0);
  }
});

function send (person, i) {
  if (i >= person.length) {
    return;
  }
  request(person[i], (err, response, body) => {
    if (err) throw err;
    else {
      console.log(JSON.parse(body).name);
      return send(person, ++i);
    }
  });
}
