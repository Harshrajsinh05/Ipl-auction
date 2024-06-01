import random
import matplotlib.pyplot as plt
class Trade:
    def __init__(self,team):
        self.team=team
        self.b_price=0
        
    def buy_player(self,data,r_number,team_player):
        
        while (True):        
            n = random.randint(1, 10)
            if n!=r_number:
                self.r_num.add(n)
                price=data[-1]
                
                b_price=float(price)+self.b_price
                self.b_price+=500000
                if(n==1 and self.team["chennai super kings"]>=b_price and len(team_player["csk"])<16):
                    print("----------------------------------------------")
                    print("csk goes to : ", b_price)
                    print("----------------------------------------------")
                    return "csk "+"1 "+str(b_price)
                elif(n==2 and self.team["kolkata knight riders"]>=b_price and len(team_player["kkr"])<16):
                    print("----------------------------------------------")
                    print("kkr goes to : ", b_price)
                    print("----------------------------------------------")
                    return "kkr "+"2 "+str(b_price)
                elif(n==3 and self.team["delhi capital"]>=b_price and len(team_player["dc"])<16):
                    print("----------------------------------------------")
                    print("dc goes to : ", b_price)
                    print("----------------------------------------------")
                    return "dc "+"3 "+str(b_price)
                elif(n==4 and self.team["mumbai Indians"]>=b_price and len(team_player["mi"])<16):
                    print("----------------------------------------------")
                    print("mi goes to : ", b_price)
                    print("----------------------------------------------")
                    return "mi "+"4 "+str(b_price)
                elif(n==5 and self.team["Royal Chellenger Bangalor"]>=b_price and len(team_player["rcb"])<16):
                    print("----------------------------------------------")
                    print("rcb goes to : ", b_price)
                    print("----------------------------------------------")
                    return "rcb "+"5 "+str(b_price)
                elif(n==6 and self.team["Gujarat Titan"]>=b_price and len(team_player["gt"])<16):
                    print("----------------------------------------------")
                    print("gt goes to : ", b_price)
                    print("----------------------------------------------")
                    return "gt "+"6 "+str(b_price)
                elif(n==7 and self.team["Rajasthan Royal"]>=b_price and len(team_player["rr"])<16):
                    print("----------------------------------------------")
                    print("rr goes to : ", b_price)
                    print("----------------------------------------------")
                    return "rr "+"7 "+str(b_price)
                elif(n==8 and self.team["punjab kings"]>=b_price and len(team_player["pbks"])<16):
                    print("----------------------------------------------")
                    print("pbks goes to : ", b_price)
                    print("----------------------------------------------")
                    return "pbks "+"8 "+str(b_price)
                elif(n==9 and self.team["sunrisers hyderabad"]>=b_price and len(team_player["srh"])<16):
                    print("----------------------------------------------")
                    print("srh goes to : ", b_price)
                    print("----------------------------------------------")
                    return "srh "+"9 "+str(b_price)
                elif(n==10 and self.team["lakhnau super giants"]>=b_price and len(team_player["lsg"])<16):
                    print("----------------------------------------------")
                    print("lsg goes to : ", b_price)
                    print("----------------------------------------------")
                    return "lsg "+"10 "+str(b_price)
                else:
                    continue
            else:
                continue  

    def  purse(self,name,bit_price):

        if(name=="csk"):
            self.team["chennai super kings"]=float(self.team["chennai super kings"])-bit_price
            print("Rupees left : ",self.team["chennai super kings"])
        elif(name=="kkr"):
            self.team["kolkata knight riders"]=float(self.team["kolkata knight riders"])-bit_price
            print("Rupees left : ",self.team["kolkata knight riders"])
        elif(name=="dc"):
            self.team["delhi capital"]=float(self.team["delhi capital"])-bit_price
            print("Rupees left : ",self.team["delhi capital"])
        elif(name=="mi"):
            self.team["mumbai Indians"]=float(self.team["mumbai Indians"])-bit_price
            print("Rupees left : ",self.team["mumbai Indians"])
        elif(name=="rcb"):
            self.team["Royal Chellenger Bangalor"]=float(self.team["Royal Chellenger Bangalor"])-bit_price
            print("Rupees left : ",self.team["Royal Chellenger Bangalor"])
        elif(name=="gt"):
            self.team["Gujarat Titan"]=float(self.team["Gujarat Titan"])-bit_price
            print("Rupees left : ",self.team["Gujarat Titan"])
        elif(name=="rr"):
            self.team["Rajasthan Royal"]=float(self.team["Rajasthan Royal"])-bit_price
            print("Rupees left : ",self.team["Rajasthan Royal"])
        elif(name=="pbks"):
            self.team["punjab kings"]=float(self.team["punjab kings"])-bit_price
            print("Rupees left : ",self.team["punjab kings"])
        elif(name=="srh"):
            self.team["sunrisers hyderabad"]=float(self.team["sunrisers hyderabad"])-bit_price
            print("Rupees left : ",self.team["sunrisers hyderabad"])
        elif(name=="lsg"):
            self.team["lakhnau super giants"]=float(self.team["lakhnau super giants"])-bit_price
            print("Rupees left : ",self.team["sunrisers hyderabad"])
        else:
            print("Error")

    
team={"chennai super kings":900000000,"kolkata knight riders":850000000, "delhi capital":750000000, "mumbai Indians":900000000,"Royal Chellenger Bangalor":850000000,"Gujarat Titan":800000000,"Rajasthan Royal":750000000,"punjab kings":790000000,"sunrisers hyderabad":750000000,"lakhnau super giants":850000000}
team_player={"csk":[],"kkr":[],"dc":[],"mi":[],"rcb":[],"gt":[],"rr":[],"pbks":[],"srh":[],"lsg":[]}
T=Trade(team)
player=open("Player.txt","r")
sold_player=open("Sold_players.txt","a+")
unsold_player=open("Unsold_players.txt","a+")
while True:
    print("**********************************************")
    print("*                                            *")
    print("*             Ipl Players Trade              *")
    print("*                                            *")
    print("**********************************************")
    print("1. press 1 for details of trade")
    print("2. press 2 for go to trade")
    print("3. press 3 for quite")
    choice_t=input("choice : ")
    if choice_t=="1":
        while True:
            print("**********************************************")
            print("*                                            *")
            print("*                  Details                   *")
            print("*                                            *")
            print("**********************************************")
            print("press 1 for show purse of team")
            print("press 2 for show total spending money by each team")
            print("press 3 for show most expensive player")
            print("press 4 for details of trade in the form of graph")
            print("press 5 for exit")
            c=input("Choice : ")
            if c=="1":
                print("**********************************************")
                print("*                                            *")
                print("*           Team Purse Details               *")
                print("*                                            *")
                print("**********************************************")
                for key, value in team.items():
                    print(key, ":", value)
                print("")
                print("-------------------------------------------")
            elif c=="2":
                print("**********************************************")
                print("*                                            *")
                print("*       Total Spend Money BY Team            *")
                print("*                                            *")
                print("**********************************************")
                while(True):
                    print("Enter team name like.. csk,mi,kkr ")
                    n=input("Enter team name : ")
                    if n in (team_player.keys()):
                        if team_player[n]==[]:
                            print(n+" is not spend any money")
                            break
                        else:
                            players=team_player[n]
                            player_price=[]
                            for i in range(len(players)):
                                data=players[i].split(" ")
                                player_price.append(float(data[-1]))
                            print(n+" is spend : "+str(sum(player_price))+" rupees")
                            break
                    else:
                        print("Enter valid team name") 

            elif c=="3":
                print("**********************************************")
                print("*                                            *")
                print("*          Most Expensive Player              *")
                print("*                                            *")
                print("**********************************************")
                sold_players_data = []  # List to store sold player data
                for team_players in team_player.values():
                    for player_info in team_players:
                        player_data = player_info.split(" ")
                        team_key=[key for key, value in team_player.items() if value == team_players]
                        sold_players_data.append((player_data[0] + " " + player_data[1], float(player_data[-1]), team_key[0]))
                if not sold_players_data:
                    print("No players have been sold yet.")

                else:
                    max_price = max(sold_players_data, key=lambda x: x[1])[1]
                    max_price_players = [players for players in sold_players_data if players[1] == max_price]
                    if len(max_price_players) == 1:
                        print("--------------------------------------------------")
                        print("Player :", max_price_players[0][0])  # Name
                        print("Price:", max_price_players[0][1], " rupees")         # Price
                        print("Team:", max_price_players[0][2])  # Team Name 
                        print("--------------------------------------------------")

                    else:
                        for players in max_price_players:
                            print("--------------------------------------------------")
                            print("Player:", players[0])  # Name
                            print("Price:", players[1], " rupees")   # Price
                            print("Team:", players[2])  # Team Name
                        print("--------------------------------------------------")

            elif c=="4":
                while(True):
                    print("**********************************************")
                    print("*                                            *")
                    print("*             For Graph Purpose              *")
                    print("*                                            *")
                    print("**********************************************")
                    print("press 1 for show purse deatils graph")
                    print("press 2 for show buy players by each team")
                    print("press 3 for exit")
                    d=input("Choice : ")
                    if d=="1":
                        if team:
                            team_name=team.keys()
                            team_price=team.values()
                            plt.bar(list(team_name),list(team_price),color="green")
                            plt.xlabel("Teams",color="blue")
                            plt.ylabel("Price in 10 cr.",color="blue")
                            plt.title("BAR GRAPH OF PURSE DETAILS",color="red")
                            # Rotate x-axis labels
                            plt.xticks(rotation=45,ha="right")
                            plt.tight_layout()
                            plt.show()
                        else:
                            print("")
                        
                    elif d=="2":
                        print("")
                        while(True):
                            print("Enter team name like.. csk,mi,kkr ")
                            n=input("Enter team name : ")
                            if n in (team_player.keys()):
                                if team_player[n]==[]:
                                    print("Any players not buy by this team")
                                    break
                                else:
                                    players=team_player[n]
                                    player_name=[]
                                    player_price=[]
                                    for i in range(len(players)):
                                        data=players[i].split(" ")
                                        player_name.append(data[0]+" "+data[1])
                                        player_price.append(float(data[-1]))
                                    plt.title(n +"'s players",color="red")
                                    plt.xlabel("Player",color="blue")
                                    plt.ylabel("price in cr.",color="blue")
                                    plt.bar(player_name,player_price,color="green",width=0.5)
                                    plt.xticks(rotation=45,ha="right")
                                    plt.tight_layout()
                                    plt.show()
                                    break
                            else:
                                print("Enter valid team name")
                        
                    elif d=="3":
                        break
                    else:
                        print("Invalid choice")

            elif c=="5":
                break                                   
            else:
                print("Invalid choice")

    elif choice_t=="2":
        while True:
            print("**********************************************")
            print("*                                            *")
            print("*     WELCOME TO THE IPL PLAYERS TRADE       *")
            print("*                                            *")
            print("**********************************************") 
            
            lines=player.readlines()
            
            sold_player.write("****   Sold Players    *****")
            sold_player.write("\n")
            sold_player.write("\n")

            
            unsold_player.write("****   Unsold Players    *****")
            unsold_player.write("\n")
            unsold_player.write("\n")

            for  i in range(len(lines)):
                line=lines[i].split(" ")
                T.r_num = set()
                #print(line)
                print("")
                print("---Player details------")
                print("")
                print("name : ",line[0]," ",line[1])
                print("Team : ",line[3])
                print("Type : ",line[5])
                print("Base Price : ",line[7])
                print("------------------------")
                t_name=""
                list_team=[]
                r_number=0
                while(True):
                
                    choice=input(("Are you go for bit(Enter Yes or No) : "))
                    if  (choice.lower()=="yes"):
                    
                        # print(r_number)
                        t_name=T.buy_player(line,r_number,team_player)
                        list_team=t_name.split(" ")
                        r_number=int(list_team[1])

                    elif(choice.lower()=="no"):
                        if t_name=="":
                            print(line[0]," ",line[1]," unsold..")
                            unsold_player_name="Name : "+line[0]+" "+line[1]
                            unsold_player_price="Base Price : "+ line[7]
                            unsold_player.write(unsold_player_name+"\n")
                            unsold_player.write(unsold_player_price+"\n")
                            unsold_player.write("------------------------------------------------------------------------\n")
                            break
                        else:
                            # list_team=t_name.split(" ")
                            T.b_price=0
                            print(line[0]," ",line[1]," who is going out in",list_team[0]," at ",list_team[-1])
                            list_name=line[0]+" "+line[1]
                            T.purse(list_team[0],float(list_team[-1]))
                            sold_player_name="Name : "+line[0]+" "+line[1]
                            sold_player_team="Team : "+list_team[0]
                            sold_player_price="Sold Price : "+(list_team[-1])
                            team_player[list_team[0]].append(list_name+" "+str(list_team[-1]))
                            # print(team_player)
                           # print(team_player)
                            sold_player.write(sold_player_name+"\n")
                            sold_player.write(sold_player_team+"\n")
                            sold_player.write(sold_player_price+"\n")
                            sold_player.write("----------------------------------------------------------------\n")
                            break
                    elif(choice.lower()=="q"):
                        sold_player.close()
                        unsold_player.close()
                        quit()
                    else:
                        print("Invalid Choice")
            else:
                print("Round 1 complete..")
                break
    elif choice_t=="3":
        print("**********************************************")
        print("*                                            *")
        print("*       Thanks For coming in Ipl Trade       *")
        print("*                                            *")
        print("**********************************************")
        player.close()
        sold_player.close()
        unsold_player.close()
        quit()
    else:
        print("Invalid choice") 