import os
import csv

def read_palette_from_file(palette_filename):
    my_dict = dict()
    my_dir = os.path.dirname(os.path.realpath(__file__))
    palette_filename = 'CHROMA.MAP.csv'
    with open (my_dir+'/'+palette_filename,'r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            key = int(row[0])
            value = (int(row[1]),int(row[2]),int(row[3]))
            my_dict[key] = value
    print (my_dict)
    return my_dict
