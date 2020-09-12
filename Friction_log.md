# DSA Certs - Friction Log

## DB parked
It was a bit frustrating getting hit with errors in the middle of coding/testing only to realise that the DB instance got parked.

## Auth token 
While downloading the auth token via curl was easy, I could not pull it via an XMLHttpRequest in javascript due to CORS policy issues (even though I unblocked CORS and managed to get data from the db with other XMLHttpRequests). This meant we had to abandon the initial HTML/Javascript only approach. I still don't know why the XMLHttpRequest failed.

Missed an example how to get to the token with NodeJS async functions. In the end switched to Python, where this was better documented and much easier to get started

Need an example for renewing the auth token after expiration.



