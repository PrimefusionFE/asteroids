curl -LsSf https://astral.sh/uv/install.sh | sh
cd ~/dev/bootdev
uv init asteroids
cd asteroids
un venv
source .venv/bin/activate
uv add pygame==2.6.1
un run main.py
