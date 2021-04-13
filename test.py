import csv
import math

class teams:
    def __init__(self,):
        self.teams = []

    def add(self, team, tick, cake):
        #print("startcake" + str(cake) + "Team name: " + team.name)
        if self.check(team, cake):
            #print(team.wins)
            #print("added team:" + team.name)
            if cake == 1:
                team.addWin()
            else:
                #print("stuff2")
                team.addLoss()
            self.teams.append(team)
            #self.print()
        else:
            #print("already in")
            if tick == 1:
                #print("ticktick")
                if cake == 1:
                    self.addChamp(team)
                else:
                    self.addChampLosses(team)

    def check(self, team, cake):
        counter = 0
        for team_name in self.teams:
            #print("counter: " + str(counter))
            #print(team_name.name + " vs. " + team.name)  #self.teams[counter].name)
            #print(team_name.name == team.name)
            if team_name.name == team.name: #self.teams[counter].name:
                #print("cake: " + str(cake))
                if cake == 1:
                    self.teams[counter].addWin()
                else:
                    #print("stuff")
                    self.teams[counter].addLoss()
                return False
            counter += 1
        return True

    def print(self):
        print("print names")
        for temp in self.teams:
            if temp.wins >= 10:
                print(temp.name + " had " + str(temp.wins) + " total wins.")
                if temp.champWins > 0:
                    print("and they won the championship " + str(temp.champWins) + " times.")
                    #print()
        #print(self.teams)

    def expo(self):
        rows = []
        for temp in self.teams:
            k = (temp.wins/(temp.wins+temp.losses))
            rows.append([temp.name, temp.wins, temp.champWins, temp.losses, temp.champLosses, k])
        #print(rows)
        field = ["Team", "Wins", "Championship Wins", "Losses", "Championship Losses", "Win Percentage"]
        filename = "total_wins.csv"
        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(field)
            csvwriter.writerows(rows)
        if not rows:
            return False
        else:
            return True

    def addChamp(self, champ):
        counter = 0
        for team_name in self.teams:
            #print(team_name.name + " vs. " + champ.name)  #self.teams[counter].name)
            if team_name.name == champ.name:
                #print("final adddd")
                self.teams[counter].addChamp()
                break
            counter += 1

    def addChampLosses(self, champ):
        counter = 0
        for team_name in self.teams:
            #print("losses:" + team_name.name + " vs. " + champ.name)  #self.teams[counter].name)
            if team_name.name == champ.name:
                #print("final losss adddd")
                self.teams[counter].addChampLosses()
                break
            counter += 1


class team:
    def __init__(self, team_name):
        self.name = team_name
        self.losses = 0
        self.wins = 0
        self.champWins = 0
        self.champLosses = 0
        #self.addWin()

    def print(self):
        print(self.name + " won " + str(self.wins) + " games.s")

    def addWin(self):
        self.wins += 1

    def addLoss(self):
        self.losses += 1

    def addChamp(self):
        self.champWins += 1

    def addChampLosses(self):
        self.champLosses += 1

    def name(self):
        return self.name


# csv file name
filename = "NCAA Mens March Madness Historical Results.csv"

# initializing the titles and rows list
fields = []
rows = []

# reading csv file
with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d"%(csvreader.line_num))

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))
the_teams = teams()
#  printing first 5 rows
print('\nFirst 5 rows are:\n')
for row in rows[:2050]:
    # parsing each column of a row
    count = 0

    tick = 0

    for col in row:
        count += 1
        #print(count)

        if count == 2:
            #print(col)
            if col == "National Championship":
                #print("The champes!!!!!!!!!!!!!!!!")
                tick = 1

        if count == 5:
            #print(col)
            a_team = team(col)
            #a_team.print()
            #print(a_team.champWins)
            if tick == 1:
                #print("champchamp")
                a_team.addChamp()
            #print(a_team.champWins)
            the_teams.add(a_team, tick, 1)
        #print("%10s"%col),

        if count == 8:
            #print("Coutn is 8")
            b_team = team(col)
            #print(b_team.losses)
            the_teams.add(b_team, tick ,0)


    #print('\n')
print("Now print team wins" + '\n')
the_teams.print()
print(the_teams.expo())
print("end")
