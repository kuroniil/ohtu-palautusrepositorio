from player_reader import PlayerReader
from player_stats import PlayerStats
from rich import print
from rich.table import Table
from rich.padding import Padding
from rich.console import Console
from rich.text import Text

def main():
    console = Console()
    title = Padding("NHL statistics by nationality", 1)
    console.print(title)

    while True:
        season = console.input("Select season [bold magenta][2018-19/2019-20/2020-21/2021-22/2022-23/2023-24/2024-25/][/]: ")    
        nationality = console.input("Select nationality\n[bold magenta][AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR][/] ")
        
        url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
        reader = PlayerReader(url)
        stats = PlayerStats(reader)
        players = stats.top_scorers_by_nationality(nationality)

        title = Padding(f"Top scorers of {nationality}", 1)
        table = Table(title=title)

        table.add_column("name")
        table.add_column("team")
        table.add_column("goals")
        table.add_column("assists")
        table.add_column("points")

        for player in players:
            name = Text(player.name)
            name.stylize("bold cyan")
            team = Text(player.team)
            team.stylize("bold magenta")
            goals = Text(str(player.goals))
            goals.stylize("bold green")
            points = Text(str(player.points))
            points.stylize("bold green")
            assists = Text(str(player.assists))
            assists.stylize("bold green")
            table.add_row(name, team, goals, assists, points)
            
        print(table)

if __name__ == "__main__":
    main()
