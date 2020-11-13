#!/usr/bin/env bash

APP_KEY=$(awk 'BEGIN { FS="=" }; { if ($1 == "application_key") print $2 }' ovh.conf)

RESPONSE=$(
  curl -XPOST \
  -H"X-Ovh-Application: $APP_KEY" \
  -H "Content-type: application/json" \
  https://ca.api.ovh.com/1.0/auth/credential \
  -d '{
    "accessRules": [
      {"method": "GET", "path": "/*"},
      {"method": "POST", "path": "/*"},
      {"method": "PUT", "path": "/*"},
      {"method": "DELETE", "path": "/*"}
    ]
  }'
)

CONSUMER_KEY=$(echo $RESPONSE | jq -r '.consumerKey')
VALIDATION_URL=$(echo $RESPONSE | jq -r '.validationUrl')

sed -i "s/consumer_key=\w*/consumer_key=$CONSUMER_KEY/" ovh.conf

echo "Please go to $VALIDATION_URL to approve the application."
