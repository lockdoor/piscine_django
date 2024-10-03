#! /bin/bash
curl --head --silent "$1" | grep "Location" | cut -d ' ' -f 2
