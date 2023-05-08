import re

code = open("hello_world.acts").read()

class regex:
  requ = r'require "(.+)" @(.+)'
  func = r'\.(\w+)\((\w*)\) \{(.+?)\n\}'
  call = r'\$(\w+)\.(\w+)\s*\{([^}]+)\}'
  vars = r'#\s*(\w+)\s*:\s*(\w+)\s*;?'
  objs = r'!\s*(\w+)\s*:\s*(\w+)\s*;?'

# Use re.sub() to replace the matched pattern with the desired output format
_code = re.sub(regex.requ, r'import \1 from \2',  code)
_code = re.sub(regex.func, r'def \1(\2):\3', _code, flags=re.DOTALL)
_code = re.sub(regex.call,  lambda m: f'{m.group(1)}.{m.group(2)}(' + ', '.join(f'"{k.strip()}"={v.strip()}' for k,v in re.findall(r'(\w+)\s*:\s*([^;]+);', m.group(3))) + ')', _code)
_code = re.sub(regex.vars, lambda m: f'vars["{m.group(1)}"] = {m.group(2)}', _code)
_code = """
.init() {
  !objekt: {
    "text": 10,
  }
}
"""
_code = re.sub(regex.objs, lambda m: f'objs["{m.group(1)}"] = {m.group(2)}', _code)

print(_code)

