# AWS CMD CloudTools

## Alias using Python venv
```bash
# Install dependencies
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt

# Copy environment file and edit as needed
cp .env.example .env
nano .env

# Create alias
echo "alias cloudtools='$(pwd)/venv/bin/python $(pwd)/main.py'" >> ~/.bash_aliases
```