#!/usr/bin/node

//get module
const request = require("request");

//get command line argument
const movieId = process.argv[2];

let baseUrl = "https://swapi-api.alx-tools.com/api/";
let filmUrl = baseUrl + "films/" + movieId;

request(filmUrl, (error, _response, body) => {
  //log error
  if (error) console.log(error.message);
  //parse to json
  info = JSON.parse(body);
  charUrls = info["characters"];

  for (let url of charUrls) {
    request(url, (error, _response, body) => {
      //log error
      if (error) console.log(error.message);
      //parse json
      personInfo = JSON.parse(body);
      console.log(personInfo["name"]);
    });
  }
});
