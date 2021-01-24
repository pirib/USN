import random
import time

#################################################################################DATABASES

realmadrid = {0:[96,48,92,"Ronaldo"], 1:[89,60,78,"Bale"], 2:[97,65,90,"Isco"],
              3:[85,83,80,"Modric"],4:[90,80,80,"Kroos"],5:[91,95,96,"Casemiro"],
              6:[27,97,96,"Ramos"],7:[80,92,90,"Marcelo"],8:[55,90,89,"Carvajal"],
              9:[50,91,85,"Pepe"],10:[10,87,99,"Navas"]}
realmadrid_subs = {0:[87,26,78,"Benzema"], 1:[87,27,78,"Morata"], 2:[73,32,69,"Mariano"],
              3:[89,44,72,"Rodriguez"],4:[86,90,91,"Casemiro"],5:[73,63,75,"Kovacic"],
              6:[71,40,64,"Vazquez"],7:[51,32,35,"Odegaard"],8:[45,84,81,"Fernandez"],
              9:[70,78,79,"Danilo"],10:[10,79,99,"Casialla"]}

barcelona = {0:[99,45,82,"Messi"], 1:[98,48,83,"Neymar"], 2:[99,60,93,"Suarez"],
              3:[82,70,72,"Iniesta"],4:[84,59,66,"Rakitic"],5:[59,83,81,"Busquets"],
              6:[75,95,87,"Pique"],7:[73,86,80,"Alba"],8:[53,85,80,"Mascherano"],
              9:[70,85,82,"Umtiti"],10:[10,90,99,"Terstegen"]}
barcelona_subs = {0:[87,26,78,"Benzema"], 1:[87,27,78,"Morata"], 2:[73,32,69,"Mariano"],
              3:[89,44,72,"Rodriguez"],4:[86,90,91,"Casemiro"],5:[73,63,75,"Secret"],
              6:[71,40,64,"Kovacic"],7:[51,32,35,"Odegaard"],8:[45,84,81,"Fernandez"],
              9:[70,78,79,"Danilo"],10:[10,79,99,"Casialla"]}

luton = {0:[73,30,83,"Collins"], 1:[66,36,57,"Mcquoid"], 2:[61,49,72,"Hylton"],
              3:[60,30,56,"Green"],4:[48,61,72,"Mccormack"],5:[57,64,81,"Doyle"],
              6:[63,22,61,"Cook"],7:[34,60,81,"Cuthbert"],8:[51,59,66,"Shehaan"],
              9:[47,62,70,"Mullins"],10:[10,65,99,"Walton"]}
luton_subs = {0:[87,26,78,"Benzema"], 1:[87,27,78,"Morata"], 2:[73,32,69,"Mariano"],
              3:[89,44,72,"Rodriguez"],4:[86,90,91,"Casemiro"],5:[73,63,75,"Kovacic"],
              6:[71,40,64,"Kovacic"],7:[51,32,35,"Odegaard"],8:[45,84,81,"Fernandez"],
              9:[70,78,79,"Danilo"],10:[10,79,99,"Casialla"]}

tranmere = {0:[75,30,50,"Cook"], 1:[65,40,60,"Alabi"], 2:[69,50,70,"Norwood"],
              3:[72,52,80,"Tollitt"],4:[64,55,72,"C.Jennings"],5:[58,60,82,"Harris"],
              6:[52,60,65,"Ridehalgh"],7:[41,63,58,"Buxton"],8:[48,63,62,"McEveley"],
              9:[50,65,45,"McNulty"],10:[10,65,99,"Davies"]}
tranmere_subs = {0:[65,26,72,"Mangan"], 1:[55,39,57,"Dunn"], 2:[52,32,53,"Waring"],
              3:[57,44,47,"Gumps"],4:[60,56,60,"Hughes"],5:[50,60,58,"Sutton"],
              6:[63,50,64,"Norburn"],7:[58,48,35,"Kirby"],8:[59,45,55,"Wallace"],
              9:[39,55,56,"Dawson"],10:[10,58,99,"Pilling"]}

dreamteam = {0:[100,100,100,"Ola"], 1:[100,100,100,"Piri"], 2:[99,99,99,"Maradona"],
              3:[99,99,99,"Pele"],4:[99,99,99,"Zidane"],5:[99,99,99,"Beckenbauer"],
              6:[99,99,99,"Puskas"],7:[99,99,99,"Aldridge"],8:[99,99,99,"Odd Franzen"],
              9:[99,99,99,"Cruef"],10:[10,100,99,"Higuita"]}
dreamteam_subs = {0:[99,99,99,"Bergkamp"], 1:[99,99,99,"Steinar Antonsen"], 2:[99,99,99,"Solskjaer"],
              3:[99,99,99,"Kenny Hole"],4:[99,99,99,"Gascoigne"],5:[99,99,99,"Best"],
              6:[99,99,99,"Clough"],7:[99,99,99,"Mykland"],8:[99,99,99,"Hulsker"],
              9:[99,99,99,"Carlos"],10:[10,99,99,"Buffon"]}

norway = {0:[75,47,76,"Berget"], 1:[68,30,62,"King"], 2:[48,72,75,"Skjelbred"],
              3:[71,73,72,"Tettey"],4:[77,66,81,"Henriksen"],5:[72,40,53,"Elyounoussi"],
              6:[53,79,79,"Nordtveit"],7:[57,70,81,"Svensson"],8:[55,70,70,"Elabdellaui"],
              9:[53,73,78,"Forren"],10:[10,85,99,"Jarstein"]}
norway_subs = {0:[72,75,37,"Soderlund"], 1:[78,52,75,"Helland"], 2:[65,62,74,"Jenssen"],
              3:[75,48,70,"Zahid"],4:[80,52,75,"Samuelsen"],5:[30,80,79,"Rogne"],
              6:[64,68,70,"Hedenstad"],7:[51,32,35,"Odegaard"],8:[55,68,64,"Linnes"],
              9:[67,69,79,"Konradsen"],10:[10,74,99,"Nyland"]}

liverpool = {0:[85,52,83,"Firmino"], 1:[86,35,77,"Sturridge"], 2:[81,67,79,"Lallana"],
              3:[73,45,66,"Salah"],4:[83,88,90,"Can"],5:[93,48,91,"Mane"],
              6:[86,42,75,"Coutinho"],7:[48,86,80,"Matip"],8:[40,82,81,"Lovren"],
              9:[33,81,84,"Sakho"],10:[10,82,99,"Karius"]}
liverpool_subs = {0:[76,31,77,"Origi"], 1:[74,35,70,"Ings"], 2:[67,24,60,"Solanke"],
              3:[80,60,74,"Wijnaldum"],4:[70,76,81,"Henderson"],5:[76,69,76,"Milner"],
              6:[61,79,76,"Clyne"],7:[48,79,77,"Klavan"],8:[68,70,74,"Moreno"],
              9:[60,71,77,"Robertson"],10:[10,78,99,"Mignolet"]}
              
arsenal = {0:[97,50,92,"Sanchez"], 1:[90,47,89,"Giroud"], 2:[82,34,76,"Lacazette"],
              3:[86,31,72,"Perez"],4:[85,30,70,"Ozil"],5:[82,73,80,"Ramsey"],
              6:[78,57,64,"Cazorla"],7:[63,87,83,"Mustafi"],8:[45,92,81,"Mertesacker"],
              9:[40,85,78,"Koscielny"],10:[10,88,99,"Cech"]}
arsenal_subs = {0:[75,34,79,"Welbeck"], 1:[100,100,100,"Banner the Wonderful Dog"], 2:[65,28,69,"Sanogo"],
              3:[87,46,75,"Walcott"],4:[66,72,77,"Xhaka"],5:[76,69,76,"Oxlade-Chamberlain"],
              6:[55,81,75,"Bellerin"],7:[53,81,73,"Monreal"],8:[65,79,77,"Debuchy"],
              9:[57,80,72,"Gibbs"],10:[10,79,99,"Ospina"]}

manchesterunited = { 0:[99,52,98,"Ibrahimovic"], 1:[82,34,84,"Lukaku"], 2:[79,35,71,"Rashford"], 
                    3:[91,84,94,"Pogba"], 4:[85,80,85, "Herrera"], 5:[91,73,89, "Mkhitaryan"], 
                    6:[80,35,60, "Mata"], 7:[80,88,92, "Valencia"], 8:[50,89,89,"Smalling"], 
                    9:[58,84,84,"Shaw"], 10:[10,95,99,"Gea"]}

manchesterunited_subs = { 0:[67,25,62,"Wilson"], 1:[88,57,89,"Rooney"], 2:[85,50,83,"Martial"],
                          3:[82,85,94,"Fellaini"], 4:[81, 80, 78,"SCHWEINSTEIGER"], 5:[63,80,82, "Scheiderlin"], 
                          6:[70,81,88,"Matic"], 7:[41,82,83,"Bailly"], 8:[56,81,76,"Blind"], 
                          9:[58,80,75,"Darmian"], 10:[10,68,99,"Romero"]}

juventus = {0:[99,50,96,"Higuain"], 1:[98,45,88,"Dybala"], 2:[84,45,88,"Mandzukic"],
            3:[85,90,92, "Khedira"], 4:[80,66,71, "Pjanic"],5:[84,60,78,"Cuadrado"],
            6:[74,76,75,"Marchisio"], 7:[62,99,98,"Chielini"], 8:[84,89,82,"Alves"],9:[80,92,91,"Sandro"], 
            10:[10,95,99,"Buffon"]}
juventus_subs = {0:[72,30,74,"Pjaca"], 1:[75,48,63,"Costa"], 2:[76,81,85,"Khedira"], 
                 3:[71,55,66,"Hernanes"], 4:[73,71,76,"Asamoah"], 5:[73,36,64,"Bernardeschii"],
                 6:[68,74,79,"Sturaro"],7:[66,64,78,"Lemina"], 8:[65,92,90,"Bonucci"], 9:[37,89,84,"Barzagli"],
                 10:[10,85,99,"Szczesny"]}

teamname = []


################################################################################START SCREEN HERE

print("\n","""                           _ajjaa
                          _Q???4Qf    
       _,...,_            ) a/]QQb     
     .'@/~~~\@'.              jQQba     
    //~~\___/~~\\          _, .?QQ#[ _  
   |@\__/@@@\__/@|         ]m _.7   "asLaas_a/ 
   |@/  \@@@/  \@|        , ,\J#L -!4Wba        
   \\__/~~~\__//       [aL[    \    \jmm     jP  
     '.@\___/@.'  	 ,b#'"[     \jmmmmm    _P.  
       ``````        a##'      "4P#mmm#   _ya 
                     _P          !4####m  ?]aa/  
                    /'        aaJ#U###m#   4QP' 
                   '         aa,/4!44! '     
               jf         _'jQQQQyb7b /     
               '.         '.QQQQ4QQPb  )?    
                            QQQ'QQP?'  jg/ f 
                          _yQP']QQb aa  
                        a#W?..QQQQ?)?   ?
                       ##  _jQQP'    
                      .j?  [ jQQ'  
                 aJ  jmaaX#L???   
                 ? am'         
               _QjQQQ/ 
               )QQQP?   
                4QQQ/ 
""", "\n !!! WELCOME TO OLA AND PIRI'S INCREBILE FOOTBALL MANAGER SIMULATION © 0.1.0.0 !!! ")




def goalscorer(team):
    playerscore = []
    playerscorelst = []
    
    playerscore.clear()
    playerscorelst.clear()
        
    for i in range(0,3):
        playerscorelst = [1,2,3]
        playerscorelst[i] = team[random.randint(0,10)][0]
        
    playerscoreatk = max(playerscorelst)
    
    try:
        for i in range(0,11):
            while len(playerscore) > 1: playerscore.pop(len(playerscore)-1)
            if playerscoreatk == team[i][0]:
                playerscore.append(team[i][3])
        scorername = playerscore[0]   
    except:
        scorername = team[0][3]
    
    playerscore.clear()
    playerscorelst.clear()
      
    return scorername

def stats_counter(team):
    attack = 0
    defence = 0
    physic = 0

    for i in team:                                  #Loops for attac in a team
        attack = team[i][0] + attack
    attack = round(attack / 11)                            #Finds and returns average    
     
    for i in team:                                  #Loops for def in a team
        defence = team[i][1] + defence
    defence = round(defence / 11 )                          #Finds and retursn average
    
    for i in team:                                  #Loops for def in a team
        physic = team[i][2] + physic
    physic = round(physic / 11)                        #Finds and retursn average
    
    stats_list = [attack, defence, physic]
    return(stats_list)
    
    
def match(team1, team2):
    s1a = stats_counter(team1)[0]
    s1d = stats_counter(team1)[1]
    s1f = stats_counter(team1)[2]    
    s2a = stats_counter(team2)[0]
    s2d = stats_counter(team2)[1]
    s2f = stats_counter(team2)[2]
    score1 = 0
    score2 = 0
    print("\n              ...GET YOUR STAR PANTS READY FOR...               ")
    time.sleep(1)
    print("___ ///   ", teamname[len(teamname)-2],"  \\\  VS  ///  ", teamname[len(teamname)-1], "  \\\ ___ \n")
    time.sleep(0.5)
    print("                     THE GAME BEGINS!                     \n")
    
    def scoreprint():
        sentences = ["Astonishing kick from 300 meters", "The day is saved", "A penalty score", "A SCISSOR KICK", "A magnificent header" ]
        return random.choice(sentences)
    
    
    for i in range(1,91):
        time.sleep(0.1)
        s1a = s1a - s1a*s1f/15000
        s1d = s1d - s1d*s1f/15000
        s2a = s2a - s2a*s2f/15000
        s2d = s2d - s2d*s2f/15000

        probScore1 = random.randint(-1000,round((s1a-s2d)))
        probScore2 = random.randint(-1000,round((s2a-s1d)))
      
        if probScore1>-30:
            score1 += 1
            print( goalscorer(team1), i,"-", scoreprint(), "for", teamname[len(teamname)-2],"!")
            
        if probScore2>-30:
            score2 += 1
            print( goalscorer(team2),i,"-" ,scoreprint(), "for", teamname[len(teamname)-1], "!")
    print("")
    print(teamname[len(teamname)-2],"|" ,score1,"|", teamname[len(teamname)-1], "|" ,score2,"|")


def team_numbers(team):
  if team == 1:
    teamname.append("Barcelona")
    return barcelona
    
  elif team == 2:
    teamname.append("Real Madrid")
    return realmadrid

  elif team == 3:
    teamname.append("Luton Town")
    return luton

  elif team == 4:
    teamname.append("Tranmere Rovers")
    return tranmere

  elif team == 5:
    teamname.append("Dreamteam")
    return dreamteam

  elif team == 6:
    teamname.append("Norway")
    return norway

  elif team == 7:
    teamname.append("Liverpool")
    return liverpool

  elif team == 8:
    teamname.append("Arsenal")
    return arsenal

  elif team == 9:
    teamname.append("Manchester United")
    return manchesterunited

  elif team == 10:
    teamname.append("Juventus")
    return juventus

    
def subs(team):
    
    def subteam(team):    
        
        if team == realmadrid:
            return realmadrid_subs
        
        elif team == barcelona:
            return barcelona_subs
        
        elif team == luton:
            return luton_subs
        
        elif team == tranmere:
            return tranmere_subs
        
        elif team == dreamteam:
            return dreamteam_subs
        
        elif team == norway:
            return norway_subs
        
        elif team == liverpool:
            return liverpool_subs
        
        elif team == arsenal:
            return arsenal_subs

        elif team == manchesterunited:
            return manchesterunited_subs
        
        elif team == juventus:
            return juventus_subs
    
    subsmenu = 1
    while subsmenu == 1:         
        team_sub = subteam(team)    
        
        print("\nPLAYING TEAM")
        for i in range(0,11):
            print("%-40s" %(team[i][3]),"  Atk:", team[i][0] ,"  Def:", team[i][1], "  Phy:", team[i][2] ,"   ", i )
        
        print("\nSUBS TEAM")            
        for i in range(0,len(team_sub)):
            print("%-40s" %(team_sub[i][3]),"  Atk:", team_sub[i][0] ,"  Def:", team_sub[i][1], "  Phy:", team_sub[i][2] ,"   ", i )
   
        sub_out = int(input("What player would you want to remove? "))
        print("You are kicking", team[sub_out][3], "out")
        sub_in = int(input("Sub player in: "))
        print("You are getting", team_sub[sub_in][3], "in")
        
        
        temp_out = team[sub_out]
        temp_in = team_sub[sub_in]
        
        team[sub_out] = temp_in
        team_sub[sub_in] = temp_out
        
        subsmenu = int(input("Quit subbing     (0)\nMake another sub (1) \n"))
        if subsmenu == 1:
            print("\n")
        elif subsmenu == 0:
            print("\n")
        else:
            subsmenu = int(input("Quit subbing(0)\nMake another sub(1) \n"))
    
menu = 2  

while menu == 2: 
    menu = int(input("To manage a team choose (0)\nTo play a game choose   (1)\nTo exit the game choose (3) \n"))
        
    if menu == 0:
        print("\n AVAILABLE TEAMS \n%-25s 1 %-25s 2 %-25s 3 %-25s 4 %-25s 5 %-25s 6%-25s 7 %-25s 8 %-25s 9 %-25s 10\n"%("\nBarcelona:","\nReal Madrid:","\nLuton:","\nTranmere:","\nDreamteam:","\nNorway:", "\nLiverpool:", "\nArsenal:", "\nManchester United:", "\nJuventus:" ))
        subs( team = team_numbers(int(input("Choose a team to make subs: "))) )
        menu = 2
        
    elif menu == 1:
        
        print("\n AVAILABLE TEAMS \n%-25s 1 %-25s 2 %-25s 3 %-25s 4 %-25s 5 %-25s 6%-25s 7 %-25s 8 %-25s 9 %-25s 10\n"%("\nBarcelona:","\nReal Madrid:","\nLuton:","\nTranmere:","\nDreamteam:","\nNorway:", "\nLiverpool:", "\nArsenal:", "\nManchester United:", "\nJuventus:" ))
        home = team_numbers(int(input("Home team: ")))
          #Set hometeamname in variabel and print with result
        away = team_numbers(int(input("Away team: ")))
          #Set awayteam in variabel and print with result        
        rematch = 1
        while rematch == 1:
          match(home,away)
          rematch = int(input("Rematch? (1)\nTo menu  (0) \n"))
          menu = 2
    elif menu == 3:
        print("So Long, and Thanks for All the Fish!")
    else:
        menu = 2
