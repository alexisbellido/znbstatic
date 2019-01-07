#!/bin/bash
set -e

source /env/bin/activate

if [ "$1" == "production" ]; then
	export USER=root
	export GROUP=root
else
	exec "$@"
fi