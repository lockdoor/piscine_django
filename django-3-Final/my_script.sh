#! source

if [ ! -d "$HOME/venv$PWD" ]; then
    python3 -m venv "$HOME/venv$PWD"
    echo "Created venv successful"
else
    echo "Venv already existed"
fi

source $HOME/venv$PWD/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirement.txt

