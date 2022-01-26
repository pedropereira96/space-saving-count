from itertools import islice
from collections import defaultdict
from sys import exit, argv
import os
import re
from time import time
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

from space_saving_count import counter
from export_outputs import export


def usage():
    print("Usage:\n python3 code/space-saving-count.py <text file>")
    exit()


def process(file_path):
    """ Counters process """
    exportation_data = export()
    
    counting = counter(file_path)
    counting.read_file()
    cardinality = len(counting.exact_counter)
    print("Cardinality: " + str(cardinality))
    precision_dict = []
    recall_dict = []

    # To use k like a percent of cardinality
    array_k=[0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

    for l in array_k:
        k= round(l * cardinality)

        start_time = time()
        counting.space_saving_counter(k)
        final_time = time() - start_time
        print("Time to k={}: {}".format(k, final_time))

        exportation_data.update(counting.exact_counter, counting.space_saving_count,  counting.ammount_of_words, k)

        exact = []
        space_save = []
        words=[]
        different=[]
        lista=[]
        error_range = []
        for x in counting.space_saving_count:
            #print(counting.space_saving_count[x])
            words.append(x)
            space_save.append(counting.space_saving_count[x] )
            exact.append(counting.exact_counter[x])
            lista.append([x,counting.space_saving_count[x] , counting.exact_counter[x], counting.space_saving_count[x] - counting.exact_counter[x],
            (  counting.exact_counter[x] ) * 100 / counting.space_saving_count[x] ])
            err_range = (  counting.exact_counter[x] ) * 100 / counting.space_saving_count[x] 
            error_range.append(err_range)

        exportation_data.to_excel(lista,k)
        exportation_data.line_chart(words, space_save, exact, k)

        print("\n")

def check_file(file_path):
    """Check if file exist"""
    return os.path.exists(file_path) 


if __name__ == '__main__':
    """ Initialization """
    if len(argv) < 2 :
        usage()

    file_path = argv[1]
    if not check_file(file_path):
        print("Incorrect file!")
        exit()
    process(file_path)