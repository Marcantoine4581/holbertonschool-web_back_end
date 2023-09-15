const Utils = require('./utils')

function getPaymentRequestToApi(success) {
  if (success === true) {
    return new Promise((resolve) => {
      resolve({data: 'Successful response from the API' })
    })
  }
}

module.exports = getPaymentRequestToApi;
