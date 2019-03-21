import re

# Simple script to generate cross-links
regex = re.compile('(@function|@mixin) ([^_].*) {')
i = 0
with open("../src/_string.scss") as f:
    for line in f:
        result = regex.match(line)
        i += 1
        if result != None:
            print('- [`' + result.group(2) + '`](https://github.com/timfayz/elementcss/blob/master/src/_string.scss#L' + str(i) + ')')