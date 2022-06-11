#!/bin/bash

GRAPHQL_URL='http://localhost:8080/'

curl -vv -X POST $GRAPHQL_URL --header "content-type: application/json" --data '{"query":"query{books{title}}"}'
