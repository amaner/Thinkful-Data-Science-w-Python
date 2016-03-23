import collections
pop2010 = collections.defaultdict(int)
landarea = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[7] = int(line[7])
        if line[1] == 'Total National Population':
        	pop2010[line[0]] += line[5]
        	landarea[line[0]] += line[7]

for key in pop2010.keys():
	pop2010[key] = float(pop2010[key])
	landarea[key] = float(landarea[key])
	print "population density in {} is {}".format(key, pop2010[key]/landarea[key]) + " persons per sq km"