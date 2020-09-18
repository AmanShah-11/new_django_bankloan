from webscrape import Webscrape
import pandas as pd

# Performs webscraping
Test_1 = Webscrape()
Test_1.navigation()
rankings, names = Test_1.get_basketball_lists()
merged_list = Test_1.merge(rankings, names)
stats = Test_1.get_basketball_stats()

df = pd.DataFrame(merged_list, stats)
df.to_csv("C://Aman//PycharmProjects/unittest_basketball")

# if __name__ == "__main__":
#     main.py()