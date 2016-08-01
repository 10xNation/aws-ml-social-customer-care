#!/bin/bash


# Clear existing node modules
rm -rf node_modules/

# Install AWS SDK
npm install aws-sdk

# Clear existing python env
virtualenv --clear local-python

# Activate python env
source local-python/bin/activate

# Install python packages
pip install --upgrade pip
pip install ndg-httpsclient pyasn1 pyopenssl python-twitter unicodecsv
pip install boto
