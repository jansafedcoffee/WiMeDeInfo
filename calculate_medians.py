import statistics

# This Code is written by Jan Claußnitzer for his course
# Wissenschaftliche Methoden der Informatik :)

mergesort = [0.244, 0.273, 0.253, 0.263, 0.261, 0.25]
bubblesort = [0.304, 0.342, 0.2, 0.148, 0.271, 0.102]
quicksort = [0.169, 0.204, 0.188, 0.23, 0.232, 0.219]


def calculate_rounded_statistics(data, decimals_mean=3, decimals_std_dev=6):
    median = round(statistics.median(data), decimals_mean)
    mean = round(statistics.mean(data), decimals_mean)
    std_dev = round(statistics.stdev(data), decimals_std_dev)
    return median, mean, std_dev


median_mergesort, mean_mergesort, std_dev_mergesort = calculate_rounded_statistics(mergesort)
median_bubblesort, mean_bubblesort, std_dev_bubblesort = calculate_rounded_statistics(bubblesort)
median_quicksort, mean_quicksort, std_dev_quicksort = calculate_rounded_statistics(quicksort)

# ERGEBNIS AUFGABE 2.5 B
print("AUFGABE 2.5 B")

print("Mergesort - Median: {} ms, Mittelwert: {} ms, Standardabweichung: {} ms".format(median_mergesort, mean_mergesort,
                                                                                       std_dev_mergesort))
print("Bubblesort - Median: {} ms, Mittelwert: {} ms, Standardabweichung: {} ms".format(median_bubblesort,
                                                                                        mean_bubblesort,                                                                     std_dev_bubblesort))
print("Quicksort - Median: {} ms, Mittelwert: {} ms, Standardabweichung: {} ms".format(median_quicksort, mean_quicksort,

                                                                                       std_dev_quicksort))
# BEARBEITUNG AUFGABE 2.5 C
all_data = mergesort + bubblesort + quicksort

median_combined, mean_combined, std_dev_combined = calculate_rounded_statistics(all_data)

# ERGEBNIS AUFGABE 2.5 C
print("AUFGABE 2.5 C")
print("Alle Daten zusammen - Median: {} ms, Mittelwert: {} ms, Standartabweichung: {} ms".format(median_combined, mean_combined,
                                                                                     std_dev_combined))
