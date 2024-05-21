#!/usr/bin/node
const request = require('request');

const myarg = process.argv[2];
const thefilms = `https://swapi-api.alx-tools.com/api/films/${myarg}`;

request.get(thefilms, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const filmdata = JSON.parse(body);
  const CharacterData = filmdata.characters;
  CharacterData.forEach(theurls => {
    request.get(theurls, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const thecharacters = JSON.parse(body);
      console.log(thecharacters.name);
    });
  });
});
