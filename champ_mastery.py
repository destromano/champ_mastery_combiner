import csv
import pprint

champMastery = {}
with open('input.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        champ = row[0]
        # get rid of commas in number so we can convert to integer
        mastery = int(row[2].replace(",",""))
        print("Champ: {} Mastery: {}".format(champ, mastery))

        champMastery[champ] = champMastery.get(champ, 0) + mastery

# sort dictionary by values and print
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(sorted(champMastery.items(), key=lambda x:x[1], reverse=True))