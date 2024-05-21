#!/usr/bin/node
const request = require('request');

const myarg = process.argv[2];
const thefilms = `https://swapi-api.alx-tools.com/api/films/${myarg}`;

request.get(thefilms, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const filmdata = JSON.parse(body);
  const CharacterData = filmdata.characters;
  for (const url of CharacterData) {
    await new Promise((resolve, reject) => {
      request.get(url, (error, response, body) => {
        if (error) {
          reject(error);
        }
        const eachcharacter = JSON.parse(body);
        console.log(eachcharacter.name);
        resolve();
      });
    });
  }
});
