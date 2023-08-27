import pandas as pd
# read csv file
reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)
# unique countries and number of reviews
uniq_country_reviews = reviews['country'].value_counts()
# average points for unique countries rounded to 1 decimal point
average_points = reviews.groupby('country')['points'].mean().round(1)
# summary dataframe
summary_df = pd.DataFrame.merge(uniq_country_reviews, average_points, on='country', how='inner')
# writing the data to csv
summary_df.to_csv("data/reviews-per-country.csv")