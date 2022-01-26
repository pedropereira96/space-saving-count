
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class export():
    def __init__(self):
        self.exact_counter = defaultdict(int)
        self.space_saving = defaultdict(int)
        self.ammount_of_words = 0
        self.k = 0

    def update(self, exact_counter, space_saving, ammount_of_words, k):
        """ New Constructor """
        self.exact_counter = exact_counter
        self.space_saving = space_saving
        self.ammount_of_words = ammount_of_words
        self.k = k

    def line_chart(self, words, space_save, exact, k):
        """Create line chart and save figure in the content/output folder, with name 'line_chart_(k value).png'"""
        plt.clf()
        fig, ax = plt.subplots()
        ax.plot(range(len(words)), space_save, label="Space Save")
        ax.plot(range(len(words)), exact, label="Exact")
        ax.legend()
        plt.xlabel('Words Rank')
        plt.ylabel('Counter')
        plt.title("Most frequent {} words".format(k))
        plt.savefig("content/output/lines_chart_"+str(self.k)+".png")
        #plt.show()

    def to_excel(self, lista, k):
        """Create excel file and save in the content/output folder, with name 'counters_results_(k value).xlsx'"""
        df2 = pd.DataFrame(np.array(lista), columns=['Words', 'Space Saving Count', 'Exact Count', 'Different', 'Exact counter percent in space save counter'])
        df2.to_excel("content/output/counters_results_"+str(k)+".xlsx")