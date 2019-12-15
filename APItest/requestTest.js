var request = require('request');

request('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=OIBR3.SA&interval=5min&outputsize=full&apikey=5KSLO2ETFG0W0I4Q', function (error, response, body) {
  console.log('error:', error); // Print the error if one occurred
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the HTML for the Google homepage.
});
