from itertools import islice
from collections import defaultdict
from sys import exit, argv
import os
import re
from time import time

from matplotlib import pyplot as plt

from space_saving_count import counter
from export_outputs import export

def check_file(file_path):
    return os.path.exists(file_path) 

def usage():
    print("Usage:\n python3 code/space-saving-count.py <text file>")
    exit()

if __name__ == '__main__':
    if len(argv) < 2 :
        usage()

    file_path = argv[1]
    if not check_file(file_path):
        print("Incorrect file!")
        exit()
    
    counting = counter(file_path)
    counting.read_file()
    cardinality = len(counting.exact_counter)
    print("Cardinality: " + str(cardinality))
    precision_dict = []
    recall_dict = []

    array_k=[500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000, 3250, 3500, 3750, 4000, 4250, 4500]
    for k in array_k:
        print("K={}".format(k))
        start_time = time()
        counting.space_saving_counter(k)
        a = export(counting.exact_counter, counting.space_saving_count,  counting.ammount_of_words, k)
        final_time = time() - start_time
        print("Time to k={}: {}".format(k, final_time))
        a.group_bar_chart()


        frequent_threshold = ((1 / k) * len(counting.words))
        #print("frequent_threshold : " + str(frequent_threshold))
        frequent_items = dict(filter(lambda e: e[1] > frequent_threshold, counting.exact_counter.items()))

        #print("frequent_items" + str(frequent_items))
        precision_dict.append(
            len(dict(filter(lambda e: e[0] in frequent_items, counting.space_saving_count.items()))) / len(counting.space_saving_count)
        )
        recall_dict.append(
            len(dict(filter(lambda e: e[0] in frequent_items, counting.space_saving_count.items()))) / len(frequent_items) if len(
                frequent_items) > 0 else None
        )

    print("precision: " + str(len(precision_dict)))
        
    print("recall : " + str(len(recall_dict)))
 
    a =[kl for kl in range(500, cardinality, 250)]
    plt.clf()
    
    fig = plt.figure()
    plt.figure().clear()
    plt.close()
    plt.cla()
    plt.clf()
    plt.plot(array_k, precision_dict, marker="o", label="precision")
    plt.plot(array_k, recall_dict, marker="D", label="recall")
    plt.legend()
    plt.xlabel("k")
    plt.title("Metrics in function of k")
    plt.show()


    
