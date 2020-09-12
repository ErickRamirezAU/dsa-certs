# DSA Certs - Friction Log

## DB parked
It was a bit frustrating getting hit with errors in the middle of coding/testing only to realise that the DB instance got parked.

We need to address this since we know that it's a bad experience for end-users. We run into this problem during Dev Workshops and it's horrible.

## Auth token 
While downloading the auth token via curl was easy, I could not pull it via an XMLHttpRequest in javascript due to CORS policy issues (even though I unblocked CORS and managed to get data from the db with other XMLHttpRequests). This meant we had to abandon the initial HTML/Javascript only approach. I still don't know why the XMLHttpRequest failed.

Missed an example how to get to the token with NodeJS async functions. In the end switched to Python, where this was better documented and much easier to get started.

Need an example for renewing the auth token after expiration.

## Messaging
The details of the Stargate usage wasn't readily obvious to me. The examples made it look more complicated until I came to realise how simple it is to use Stargate.

I think examples with `curl` to get an auth token, insert or retrieve data would be a more powerful way of illustrating how elegantly simple it is to access Astra using Stargate.

## Response times
Most of the time, queries are almost immediate accessing the Astra in `europe-west1` region from Melbourne, Australia. But sometimes, requests take 5+ seconds. So for the video, I had to pre-load some app screens because we didn't want to be stuck waiting for a response during the demo.

I think this is a function of the free tier but we need to address this so end-users don't think this is the norm when using Astra.
