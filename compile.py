import re

code = open("hello_world.acts").read()

class regex:
  requ = r'require "(.+)" @(.+)'
  func = r'\.(\w+)\((\w*)\) \{(.+?)\n\}'
  call = r'\$(\w+)\.(\w+)\s*\{([^}]+)\}'

# Use re.sub() to replace the matched pattern with the desired output format
_code = re.sub(regex.requ, r'import \1 from \2',  code)
_code = re.sub(regex.func, r'def \1(\2):\3', _code, flags=re.DOTALL)
_code = re.sub(regex.call,  lambda m: f'{m.group(1)}.{m.group(2)}(' + ', '.join(f'"{k.strip()}"={v.strip()}' for k,v in re.findall(r'(\w+)\s*:\s*([^;]+);', m.group(3))) + ')', _code)

print(_code)

