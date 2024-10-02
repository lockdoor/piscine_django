#! /bin/bash
curl --head --silent $1 | grep "Location" | cut -wf 2
