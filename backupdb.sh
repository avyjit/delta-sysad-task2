#!/bin/env bash

timestamp=$(date +%Y_%m_%d_%H_%M_%S)
filename="${timestamp}_backup"

# The db name is postgres
PGPASSWORD=postgres pg_dump -U postgres -h localhost -p 5432 -Fc -f $filename postgres

echo Backup written to $filename successfully...