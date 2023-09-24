import pandas
data = pandas.read_csv("2018_NYCP_Squirrel_Census.csv")

COLOR_COLUMN = "Primary Fur Color"

# Generate a list of unique colors in the table
color_types = data[COLOR_COLUMN].unique()

# Create an empty list for storing count list for each color
color_count = []
# Find the count of columns where each color is found and store it in the color count list
for fur_color in color_types:
    count = data[data[COLOR_COLUMN] == fur_color].count()[COLOR_COLUMN]
    color_count.append(count)

# Create a dictionary for storing results
summary = {"fur color": color_types, "count": color_count}

# Convert the dictionary to data frame
output_data = pandas.DataFrame(summary)
output_data.to_csv("squirrel_count.csv")
