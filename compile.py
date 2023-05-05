import re

code = open("hello_world.acts").read()

class regex:
  requ = r'require "(.+)" @(.+)'
  func = r'\.(\w+)\((\w*)\) \{(.+?)\n\}'

# Use re.sub() to replace the matched pattern with the desired output format
_code = re.sub(regex.requ, r'import \1 from \2',  code)
_code = re.sub(regex.func, r'def \1(\2):\3', _code, flags=re.DOTALL)

print(_code)

