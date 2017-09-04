from imdb_class import Imdb

#performa a statistical and sentiment analysis of reviews parsed from the Internet Movie Data Base (IMDB)


csv_file = "raw_data.csv"

#create instance of imdb class
imdb_object = Imdb(csv_file)

#plot histograms

imdb_object.plot_dicts()

#perform two-sample wilcoxon test for independent samples
# a.k.a Mann Whitney U

imdb_object.u_test()

#print n most common word in dictionaries, choose "plus" for positive reviews, "minus for the negative"

n = 5
print imdb_object.common_words(n, "plus")

#remove 65 overly common words (mostly articles, connectives and adverbs)
#as for the remaining words, plot only those with a count discrepancy of 80

imdb_object.plot_significant()


