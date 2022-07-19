import pandas as pd

url = "https://en.wikipedia.org/wiki/World_population"
tables = pd.read_html(url)
#print(len(tables))

#print(tables[0])
worldPopulation = tables[0]

worldPopulation = worldPopulation.drop(11, axis=0)
worldPopulation = worldPopulation.drop('#', axis=1)

worldPopulation.columns = ['Country', '2000', '2015', '2030']

worldPopulation.to_html('.\OUTPUT\\worldPopulation.html')
#worldPopulation.to_html('.\OUTPUT\\worldPopulation.html',index=False)