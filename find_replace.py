lines = []
replacements = {"'":'"'}

with open('netstat_data_IP_formatted.json') as infile:
    for line in infile:
        for src, target in replacements.iteritems():
            line = line.replace(src, target)
        lines.append(line)
with open('netstat_data_IP_formatted.json', 'w') as outfile:
    for line in lines:
        outfile.write(line)
