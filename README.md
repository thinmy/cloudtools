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

## Usage
```bash
# List all ec2 instances
cloudtools ec2

# List all rds instances
cloudtools rds

# Lit all ec2 instances using different profile
cloudtools ec2 --profile {profile}
```

## Todos
- [ ] Allow to set the resources region