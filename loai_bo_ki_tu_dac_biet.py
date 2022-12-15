import re
text = 'text -- @# $% number '
new_text = re.sub(r"[^a-zA-Z0-9]" ,"", text)

print(new_text)