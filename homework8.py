# 1 график 20 самых высоких баскетболитстов в NBA

players = pd.read_csv("Players.csv")
players.head(20)
players = players.dropna()
players = players[["Player", "height"]].sort_values('height', ascending=False).head(20)
plt.xlabel('Height')
plt.ylabel('Names')
plt.barh(players['Player'], players['height'])

#из графика видим что самые высокие ребята с ростом в районе 2.30


#2 топ 10 универов которые выпустили максимальное количество баскетболистов

players = pd.read_csv("Players.csv")
players.head(20)

players = players.dropna()

players = players[["Player", "collage"]]
players['count'] = players.groupby(['collage']).transform('count')

players = players.drop_duplicates("collage").sort_values("count", ascending = False)

players = players[["collage", "count"]].head(20)

plt.xlabel('Collage')
plt.ylabel('Count')
plt.barh(players['Count'], players['Collage'])

# Видим какие универы поставляют больше всего игроков и их отношение к остальным универам


# 3. Видим соотношение веса и роста баскетболистов

players = pd.read_csv("Players.csv")
players = players.dropna()

sns_plot = sns.pairplot(
    players[["height", "weight"]]
)

sns_plot


# 4 Видим распределение роста среди баскетболистов
players = pd.read_csv("Players.csv")
players = players.dropna()

sns.distplot(players.height)

#5 Видим количество и соотношения городов которые породили больше всего звезд NBA

players = pd.read_csv("Players.csv")
players.head(20)

players = players.dropna()

players = players[["Player", "birth_city"]]

players['count'] = players.groupby(['birth_city']).transform('count')

players = players.sort_values("count", ascending = False).drop_duplicates('birth_city')
players = players[["birth_city", "count"]].head(20)
players.set_index("birth_city").plot(kind = "bar")
