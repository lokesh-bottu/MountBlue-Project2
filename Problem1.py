import csv
from collections import defaultdict
import matplotlib.pyplot as plt


with open('Maharashtra.csv',newline='',encoding='ISO-8859-1') as csvfile:
    data= csv.DictReader(csvfile)

    less_than_lac = 0
    between_1L_and_10L = 0
    between_10L_and_1Cr = 0
    between_1Cr_and_10Cr = 0
    more_than_10Cr = 0


    for row in data:
        authorized_cap = int(float(row["AUTHORIZED_CAP"]))

        if authorized_cap <= 100000:
            less_than_lac += 1
        elif 100000 < authorized_cap <= 1000000:
            between_1L_and_10L += 1
        elif 1000000 < authorized_cap <= 10000000:
            between_10L_and_1Cr += 1
        elif 10000000 < authorized_cap <= 100000000:
            between_1Cr_and_10Cr += 1
        else:
            more_than_10Cr += 1


    categories = ["<= 1L", "1L to 10L", "10L to 1Cr", "1Cr to 10Cr", "> 10Cr"]
    counts = [less_than_lac, between_1L_and_10L, between_10L_and_1Cr, between_1Cr_and_10Cr, more_than_10Cr]
    #Create a bar plot for the histogram
    plt.hist(categories, bins=len(categories), weights=counts)



plt.xlabel("Authorized Capital Ranges")
plt.ylabel("Count")
plt.title("Histogram of Authorized Capital Ranges")

# Show the plot
plt.show()