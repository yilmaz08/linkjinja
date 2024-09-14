It is just a YAML passed to the Jinja2 template with a dead simple CLI.

## Usage
```
# clone
git clone https://github.com/yilmaz08/linkjinja.git
cd linkjinja

# install
py -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# edit
nvim ./linkjinja.yaml

# render
python3 main.py -t ./templates/template.jinja -o linkjinja.html linkjinja.yaml
```

## Contribution
Anyone can contribute new templates or source code changes.
