curl -LsSf https://astral.sh/uv/install.sh | sh
cd ~/dev/bootdev
uv init asteroids
cd asteroids
uv venv
source .venv/bin/activate
uv add pygame==2.6.1
uv run main.py
