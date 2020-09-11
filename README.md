# DataStax Academy Certificate Lookup POC
In July 2020, the [**DataStax Academy**](https://academy.datastax.com) site migrated to a new learning management system (LMS). The LMS however is not capable of hosting the certificates of the DBAs and developers who have successfully passed the Apache Cassandra™ 3 exam.

This app is a proof-of-concept attempt at providing a mechanism for certified users to be able to download a copy of their certificates.

## Getting started

This is for Python 3.6 and newer.

Recommend to run this in a virtual python environment.

Install dependencies:

```
pip install flask
pip install requests
```

Set the following environment variables

```
export FLASK_APP=app.py
export ASTRA_DB_USERNAME=
export ASTRA_DB_PASSWORD=
export ASTRA_DB_ID=
export ASTRA_DB_REGION=
```

## Running the app

To run:

```
flask run
```

Navigate to `localhost:5000/hello`

Search by last name for certificates.

## TODO

Add search forms for search by email and first name

build docker file and test container

## Acknowledgements

Thanks Erick for all the ground work, and thanks Denise for the Python example which was very helpful.


## Authors
[Bettina Swynnerton](https://github.com/bettinaswynnerton) and [Erick Ramirez](https://github.com/flightc).
