import collections
pop2010 = collections.defaultdict(int)
pop2100 = collections.defaultdict(int)

with open('lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv','rU') as inputFile:
    header = next(inputFile)

    for line in inputFile:
        line = line.rstrip().split(',')
        line[5] = int(line[5])
        line[6] = int(line[6])
        if line[1] == 'Total National Population':
        	pop2010[line[0]] += line[5]
        	pop2100[line[0]] += line[6]

for key in pop2010.keys():
    print "population change 2010 to 2100 in {} is {}".format(key,pop2100[key]-pop2010[key])
    pop2100[key] = float(pop2100[key])
    pop2010[key] = float(pop2010[key])
    print "percentage change is {}".format(100*(pop2100[key]-pop2010[key])/pop2010[key])+"%"
