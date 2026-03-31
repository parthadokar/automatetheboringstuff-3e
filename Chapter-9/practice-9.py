import re
lazy_pattern = re.compile(r'<.*?>')
match1 = lazy_pattern.search('<To serve man> for dinner.>')
match1.group()

greedy_re = re.compile(r'<.*>')
match2 = greedy_re.search('<To serve man> for dinner.>')
match2.group()
