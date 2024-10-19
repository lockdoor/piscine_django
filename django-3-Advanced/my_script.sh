#!/bin/bash

if [ ! -f '.env' ]; then
    echo ".env file not found! Exiting..."
    return 1 
fi

# Load variables from .env file
set -a  # Automatically export all variables
source .env
set +a  # Stop automatically exporting variables

if [ ! -d "$HOME/venv$PWD" ]; then
    python3 -m venv $HOME/venv$PWD
    echo "Make venv finished"
else
    echo "venv already exists."
fi

. ~/venv/$PWD/bin/activate
pip install --upgrade pip >/dev/null 2>&1
pip install -r requirement.txt >/dev/null 2>&1

# Superuser to connect to PostgreSQL
PG_SUPERUSER="postgres"
# PG_SUPERPASS="postgres_password"

# Function to check if PostgreSQL user exists
check_user() {
    USER_EXISTS=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_roles WHERE rolname='$DB_USER';")
    if [ "$USER_EXISTS" == "1" ]; then
        echo "User '$DB_USER' already exists."
    else
        echo "User '$DB_USER' does not exist. Creating user..."
        create_user
    fi
}

# Function to create PostgreSQL user
create_user() {
    sudo -u postgres psql -c "CREATE USER $DB_USER WITH PASSWORD '$DB_PASS';"
    if [ $? -eq 0 ]; then
        echo "User '$DB_USER' created successfully."
    else
        echo "Error: Failed to create user '$DB_USER'."
        return 1
    fi

    sudo -u postgres psql -c "ALTER USER $DB_USER CREATEDB;"
}

# Function to check if PostgreSQL database exists
check_database() {
    DB_EXISTS=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname='$DB_NAME';")
    if [ "$DB_EXISTS" == "1" ]; then
        echo "Database '$DB_NAME' already exists."
    else
        echo "Database '$DB_NAME' does not exist. Creating database..."
        create_database
    fi
}

# Function to create PostgreSQL database
create_database() {
    sudo -u postgres psql -c "CREATE DATABASE $DB_NAME OWNER $DB_USER;"
    if [ $? -eq 0 ]; then
        echo "Database '$DB_NAME' created successfully."
        python3 manage.py makemigrations
        python3 manage.py migrate
        python3 manage.py loaddata data.json
    else
        echo "Error: Failed to create database '$DB_NAME'."
        return 1
    fi
}

# Main logic
check_user
check_database
# python3 ./manage.py runserver 0.0.0.0:8000
