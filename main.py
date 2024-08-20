from jinja2 import Environment, FileSystemLoader
from yaml import safe_load

# Load and parse the YAML config
config = safe_load(open('linkjinja.yaml'))

# Set up the Jinja2 environment and load the template
file_loader = FileSystemLoader('templates')  # Directory where template.html is located
env = Environment(loader=file_loader)
template = env.get_or_select_template('template.jinja')

# Render the template with the config and write it to linkjinja.html
output = template.render(config)

with open('linkjinja.html', 'w') as f:
    f.write(output)

print('Done! Saved as linkjinja.html')
