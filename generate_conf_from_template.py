import yaml
from jinja2 import Template

data = yaml.safe_load(open('protocol_data.yml'))
print(data)

tmpl = Template(open('protocol_temp.j2').read())
conf = tmpl.render(data)
print(conf)
