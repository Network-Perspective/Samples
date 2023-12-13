#!/bin/bash
script_path="$(dirname "${BASH_SOURCE[0]}")"
target_path="$script_path/python/np_client"

echo "$target_path"

rm -rf "$target_path"
openapi-generator-cli generate \
    -i http://host.docker.internal:5000/swagger3/ext-v1/swagger.json \
    -g python \
    -o $target_path \
    -c $script_path/python/np_client_config.yaml

    