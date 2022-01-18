
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd



##Funçao para receber ficheiros e exportalos
class export():
    def __init__(self, exact_counter, space_saving, ammount_of_words, k):
        self.exact_counter = exact_counter
        self.space_saving = space_saving
        self.ammount_of_words = ammount_of_words
        self.k = k

    def csv(self):
        pass

    def group_bar_chart(self):
        plt.clf()

        #sort space saving by counter
        self.space_saving = dict(sorted(self.space_saving.items(),key=lambda item:item[1],reverse=True))
        
        labels = list(self.space_saving.keys())
        Position = list(range(len(self.space_saving)))
        #exact counter
        exact_counter = []
        for i in self.space_saving.keys():
            exact_counter.append(self.exact_counter[i])
        
        # space saving counter
        space_saving_counter = []
        for i in self.space_saving.keys():
            space_saving_counter.append(self.space_saving[i])

        plt.figure(figsize=(20, 5))
        plt.subplots_adjust(bottom=0.3)
        ssp = plt.plot(Position, space_saving_counter,'o',color='green', label="Space Saving Count")
        plt.ylabel('Space Saving Counter')
        plt.xticks(Position, labels,rotation=90)
        exc = plt.plot(Position, exact_counter, 'o', color='blue', label="Exact ounter")
        plt.xlabel('Words')
        plt.title('Space Saving Counter (green bar)  Exact counte (blue point) k=' + str(self.k))
        plt.savefig("content/output/"+str(self.k)+".png")
        #plt.show()
