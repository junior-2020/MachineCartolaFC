from pydfs_lineup_optimizer import Site, Sport, get_optimizer


optimizer = get_optimizer(Site.YAHOO, Sport.BASKETBALL)
optimizer.load_players_from_csv("yahoo-NBA.csv")
for lineup in optimizer.optimize(10):
    print(lineup)