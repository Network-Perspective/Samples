#!/bin/bash

npm install @openapitools/openapi-generator-cli -g
# Install openapi-python-client
# pipx install openapi-python-client --include-deps

# Install Python dependencies
pip3 install --upgrade pip

cd python
pip3 install --user -r requirements.txt
pip3 install --user -r requirements-dev.txt

# Keep the container running
#tail -f /dev/null
