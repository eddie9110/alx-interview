#!/usr/bin/node

const request = require('request');
const args = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + args;

function retrieveChars (character) {
    return new Promise((resolve, reject) => {
      request(character, (err, response, body) => {
        if (err) {
          reject(err);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  }

request(url, async (error, response, body) => {
    if (error) {
      throw error;
    } else {
      const charsList = JSON.parse(body).characters;
      for (const char_ of charsList) {
        const character = await retrieveChars(char_);
        console.log(character);
      }
    }
});
