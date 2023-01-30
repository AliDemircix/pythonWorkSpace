import pandas as pd

data = pd.read_csv(
    "Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_color_data_count = len(data[data["Primary Fur Color"] == "Gray"])
red_color_data_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_data_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_color_data_count,red_color_data_count,black_color_data_count)

data_dict= {
    "Fur Color":["Gray","Red","Black"],
    "Count":[grey_color_data_count,red_color_data_count,black_color_data_count]
}
df = pd.DataFrame(data_dict)
df.to_csv("Day25/squirrel_colors_data.csv")