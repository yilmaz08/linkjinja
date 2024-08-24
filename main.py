from jinja2 import Environment, FileSystemLoader
from yaml import safe_load
import argparse

# Parse the command line arguments
parser = argparse.ArgumentParser(description='Render a Jinja2 template with a YAML config')
parser.add_argument('config', help='Path to the YAML config file')
parser.add_argument('-t', '--template', help='Path to the Jinja2 template file (if not set interactively selects)', default=None, nargs='?')
parser.add_argument('-o', '--output', help='Path to the output file (if not set prints the result)', default=None, nargs='?')
args = parser.parse_args()

# Load and parse the YAML config
config = safe_load(open(args.config))

if args.template:
    env = Environment(loader=FileSystemLoader('.'))
    template_path = args.template
else:
    env = Environment(loader=FileSystemLoader('./templates/'))
    print('Available templates:')
    for template in env.list_templates():
        print(template)
    template_path = input('Enter the name of the template file: ')


# Load the Jinja2 template
template = env.get_template(template_path)

# Render the template with the config and write it to linkjinja.html
output = template.render(config)

if args.output:
    with open(args.output, 'w') as f:
        f.write(output)
        print(f'Output written to {args.output}')
else:
    print(output)