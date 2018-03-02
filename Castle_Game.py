# -----------------------------------------+
# Rusty Clayton                            |
# CSCI 107, Assignment 10                  |
# Last Updated: 12/5/2016                  |
# -----------------------------------------|
# Castle Game                              |
# -----------------------------------------+


##This is an adventure game where you must defeat the monster in the throne room by collecting the proper items
##and reading the proper books to gain knowledge on how to defeat him.  There are three randomly generated monsters
##that you can fight(so collecting the right sword won't always be the right answer, sometimes you must know the right spells).
##
##You move by using the arrow keys, press or hold, and you can find items by pressing the spacebar.
##
##The final boss fight is similar to say a pokemon battle style format, but it is very unforgiving.  Any mistake on the final battle and you will lose.
##(you use a mixture of the 1-3 keys and text inputs for what you want to do)
##
##It also has music and some(one)sound effects that is randomly determined when passing between rooms.  Final boss music and victory and defeat music are set though.
##
##It is basically a text based adventure, with some graphics.



##CREDITS
##
##Shapeless Demon Drawing by Bethesda Softworks(Hermaus Mora)
##
##Troll Drawing by Shredded-soul
##
##Music (and/or Sound Effects) by Eric Matyas
##
##www.soundimage.org
##
##Everything Else by Rusty Clayton



####The Castle Game

####################IMPORT SECTION#############################################################################
import turtle
import time
import random
import winsound

def main():
    ##############FUNCTION SECTION###################################################################################

    ########Hero animations############
    def input1():
        hero.clear()
        writer.clear()
        wn.onkey(investigate,"space")
        wn.onkeypress(left,"Left")
        wn.onkeypress(right,"Right")
        wn.onkeypress(up,"Up")
        wn.onkeypress(down,"Down")
        wn.onkey(leave,"Escape")
        wn.onkey(cheats,"~")
        wn.listen()
    ##########INPUT 2 WAS REMOVED Due to Ineffeciency#######
    def input3():######BLocks input momentarily when moving between rooms##########
        wn.onkeypress(None,"Left")
        wn.onkeypress(None,"Right")
        wn.onkeypress(None,"Up")
        wn.onkeypress(None,"Down")
    def input4():############BOSS FIGHT
        wn.onkeypress(None,"Left")
        wn.onkeypress(None,"Right")
        wn.onkeypress(None,"Up")
        wn.onkeypress(None,"Down")
        wn.onkey(attack,"1")
        wn.onkey(magic,"2")
        wn.onkey(defend,"3")
        wn.onkey(leave,"Escape")
    def input5():###FAILURE
        wn.onkeypress(None,"Left")
        wn.onkeypress(None,"Right")
        wn.onkeypress(None,"Up")
        wn.onkeypress(None,"Down")
        wn.onkey(None,"1")
        wn.onkey(None,"2")
        wn.onkey(None,"3")
        wn.onkey(leave,"a")
        wn.onkey(leave,"Escape")
        wn.listen()
    def up():
        input3()
        hero.setheading(90)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_up1)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_upsword1)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_upshield1)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_upswordshield1)
        hero.forward(movement)
        check()
        time.sleep(.1)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_up2)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_upsword2)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_upshield2)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_upswordshield2)
        hero.forward(movement)
        check()
        time.sleep(.1)
        input1()
    def down():
        input3()
        hero.setheading(270)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_down1)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_downsword1)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_downshield1)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_downswordshield1)  
        hero.forward(movement)
        check()
        time.sleep(.1)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_down2)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_downsword2)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_downshield2)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_downswordshield2)
        hero.forward(movement)
        check()
        time.sleep(.1)
        input1()
    def left():
        input3()
        hero.setheading(180)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_left1)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_leftsword1)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_leftshield1)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_leftswordshield1)
        hero.forward(movement)
        check()
        time.sleep(.1)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_left2)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_leftsword2)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_leftshield2)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_leftswordshield2)
        hero.forward(movement)
        check()
        time.sleep(.1)
        input1()
        
    def right():
        input3()
        hero.setheading(0)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_right1)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_rightsword1)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_rightshield1)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_rightswordshield1)
        hero.forward(movement)
        check()
        time.sleep(.1)
        if len(sword)==0 and len(shield)==0:
            hero.shape(hero_right2)
        if len(sword)>=1 and len(shield)==0:
            hero.shape(hero_rightsword2)
        if len(sword)==0 and len(shield)>=1:
            hero.shape(hero_rightshield2)
        if len(sword)>=1 and len(shield)>=1:
            hero.shape(hero_rightswordshield2)
        hero.forward(movement)
        check()
        time.sleep(.1)
        input1()


    ###########FINAL BOSS FIGHTS######################
        
    def attack():
        if len(final_boss_creature)==1:#####FIGHTING THE TROLL
            if len(troll_slayer_sword)>=1 and len(how_to_slay_trolls)>=1:
                wn.bgpic('images/boss_fights/troll/troll_encounter.png')####Where to attack?
                attack_neck=wn.textinput(" ","Where do you target your attack?\nArm,Leg,Eyes,Neck,Chest?")
                attack_neck=attack_neck.capitalize()
                if attack_neck=="Neck":
                    wn.bgpic('images/boss_fights/troll/troll_attack_success.png')####Slain the troll
                    victory_sound()
                    leave()
                else:
                    wn.bgpic('images/boss_fights/troll/troll_attack_fail.png')####Attack failed, you died
                    defeat_sound()
                    input5()
            elif len(troll_slayer_sword)==0 and len(sword)==0:
                wn.bgpic('images/boss_fights/troll/troll_attack_no_weapon.png')####Failure due to no weapon
                defeat_sound()
                input5()
            elif len(troll_slayer_sword)==0 and len(sword)>=1:
                wn.bgpic('images/boss_fights/troll/troll_attack_wrong_weapon.png')####Failure due to improper weapon
                defeat_sound()
                input5()
            elif len(troll_slayer_sword)>=1 and len(how_to_slay_trolls)==0:
                wn.bgpic('images/boss_fights/troll/troll_no_knowledge.png')###Failed attack due to no knowledge
                defeat_sound()
                input5()
        elif len(final_boss_creature)==2:
            wn.bgpic('images/boss_fights/dragon/dragon_attack.png')####Must defend against dragon fire, not attack
            defeat_sound()
            input5()
        else:
            wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_attack.png')####Attacking void creature, sucked into void.
            defeat_sound()
            input5()
        
    def magic():
        if len(final_boss_creature)==3:#######FIGHTING THE DEMON
            if len(words_of_power)>=1:
                wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_encounter.png')#######Speak the words
                first_word=wn.textinput(" ","Speak the first word!")
                first_word=first_word.capitalize()
                if first_word=="Vanqui":
                    wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_ensnared.png')#####The void shudders as your magic ensnares it
                    second_word=wn.textinput(" ","Speak the second word!")
                    second_word=second_word.capitalize()
                    if second_word=="Bestiari":
                        wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_trapped.png')#####The void screams as your magic continues to trap it    
                        third_word=wn.textinput(" ","Speak the final word!")
                        third_word=third_word.capitalize()
                        if third_word=="Noctis":
                            wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_sealed.png')#####The void is sealed, you have won.
                            victory_sound()
                            leave()
                        else:
                            wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_mispoke.png')######You mispoke the words, and were consumed.
                            defeat_sound()
                            input5()
                    else:
                        wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_mispoke.png')######You mispoke the words, and were consumed.
                        defeat_sound()
                        input5()
                else:
                    wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_mispoke.png')######You mispoke the words, and were consumed.
                    defeat_sound()
                    input5()
            elif len(words_of_power)==0:
                wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_no_magic.png')####You know no magic, you are sucked into the void
                defeat_sound()
                input5()
            
        elif len(final_boss_creature)==1:
            wn.bgpic('images/boss_fights/troll/troll_magic.png')###Magic is useless against trolls
            defeat_sound()
            input5()
        else:
            wn.bgpic('images/boss_fights/dragon/dragon_magic.png')##Magic is useless against dragons
            defeat_sound()
            input5()
            
    def defend():
        if len(final_boss_creature)==2:#######FIGHTING THE DRAGON
            if len(dragon_fire_shield)>=1 and len(how_to_slay_dragons)>=1 and len(sword)>=1:
                wn.bgpic('images/boss_fights/dragon/dragon_defend.png')####stopped the fire now attack dragon
                attack_weak_spot=wn.textinput(" ","Where do you target your attack?\nNeck,Eyes,Tail,Chest,Legs?")
                attack_weak_spot=attack_weak_spot.capitalize()
                if attack_weak_spot=="Chest":
                    wn.bgpic('images/boss_fights/dragon/dragon_attack_success.png')####Slain the dragon
                    victory_sound()
                    leave()
                else:
                    wn.bgpic('images/boss_fights/dragon/dragon_attack_fail.png')####Attack failed, you died
                    defeat_sound()
                    input5()
            elif len(dragon_fire_shield)==0 and len(shield)==0:
                wn.bgpic('images/boss_fights/dragon/dragon_no_shield.png')####Failure due to no shield
                defeat_sound()
                input5()
            elif len(dragon_fire_shield)==0 and len(shield)>=1:
                wn.bgpic('images/boss_fights/dragon/dragon_wrong_shield.png')####Failure due to improper shield
                defeat_sound()
                input5()
            elif len(dragon_fire_shield)>=1 and len(how_to_slay_dragons)>=0 and len(sword)>=1:
                wn.bgpic('images/boss_fights/dragon/dragon_no_knowledge.png')####did not know how to slay dragon
                defeat_sound()
                input5()
            elif len(dragon_fire_shield)>=1 and len(sword)==0:
                wn.bgpic('images/boss_fights/dragon/dragon_no_weapon.png')###Failed attack due to no weapon
                defeat_sound()
                input5()
            
                
        elif len(final_boss_creature)==1:
            wn.bgpic('images/boss_fights/troll/troll_defend.png')####Must attack trolls agressively, otherwise they will stomp you
            defeat_sound()
            input5()
        else:
            wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_defend.png')####Delaying sealing the demons seals your fate.
            defeat_sound()
            input5()


        
    ###########investigate function#########AKA STORY#########################
    def investigate():
        
        if len(current_room)==1:######ROOM 1#######DINING HALL    ########################################################################
            if hero.xcor()<=-110 and hero.xcor()>=-209 and hero.ycor()>=15:####UPPER LEFT SECTOR 1
                writer.write("Just an ordinary table.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=-110 and hero.xcor()>=-209 and hero.ycor()<=-35:####LOWER LEFT SECTOR 1
                writer.write("Just an ordinary table.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()>=15:####UPPER RIGHT SECTOR 1
                writer.write("Just an ordinary table.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()<=-35:####LOWER RIGHT SECTOR 1
                writer.write("Just an ordinary table.", move=False, align="left", font=("Arial", 8, "normal"))   
            elif hero.ycor()>125 and len(key)==0 and len(final_boss_creature)==2:###DRAGON
                writer.write("You feel an immense heat behind the door.\nIt sounds as if some great serpent is\nslithering around in the throne room.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.ycor()>125 and len(key)==0 and len(final_boss_creature)==1:###TROLL
                writer.write("You hear the labored breathing of \n some great creature and the slow footsteps\nthat sound as though a giant was making them.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.ycor()>125 and len(key)==0 and len(final_boss_creature)==3:###SHAPELESS DEMON
                writer.write("As you listen to the door it\nis silent, but not just\nthe silence of night, absolute\nsilence, nothingness.\nIt feels as though you are\nenveloped in darkness even in the torchlight.", move=False, align="left", font=("Arial", 8, "normal"))
            

            else:
                ##############NOT IN ANY SECTOR
                writer.write("Nothing of interest here.", move=False, align="left", font=("Arial", 8, "normal"))

        if len(current_room)==2:#####Room2###########HALL OF HEROES
                        
            
            if hero.xcor()<=-193 and hero.xcor()>=-220 and hero.ycor()<=-35:####George's Armor
                if len(knowledge_of_correct_shield)>=1:
                    aquire_item("dragon_fire_shield")
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()<=-35:####LOWER RIGHT SECTOR 1
                writer.write("The suits of heroes long dead.", move=False, align="left", font=("Arial", 8, "normal"))
                aquire_item("shield")
            elif hero.xcor()<=-120 and hero.xcor()>=-210 and hero.ycor()<=-35:####LOWER LEFT SECTOR 1
                writer.write("The suits of heroes long dead.", move=False, align="left", font=("Arial", 8, "normal"))
                aquire_item("shield")
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()>=15:####Upper RIGHT SECTOR 1
                writer.write("The suits of heroes long dead.", move=False, align="left", font=("Arial", 8, "normal"))
                aquire_item("shield")
            elif hero.xcor()<=-120 and hero.xcor()>=-210 and hero.ycor()>=15:####UPPER LEFT SECTOR 1
                writer.write("The suits of heroes long dead.", move=False, align="left", font=("Arial", 8, "normal"))
                aquire_item("shield")

            else:
                ##############NOT IN ANY SECTOR
                writer.write("Nothing of interest here.", move=False, align="left", font=("Arial", 8, "normal"))
                
        if len(current_room)==3:######ROOM 3#################THE BARRACKS
            if hero.xcor()<=-110 and hero.xcor()>=-209 and hero.ycor()>=15:####UPPER LEFT SECTOR 1
                writer.write("Bed's for the soldiers who once lived here.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=-110 and hero.xcor()>=-209 and hero.ycor()<=-35:####LOWER LEFT SECTOR 1
                aquire_item("location_of_key")
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()>=15:####UPPER RIGHT SECTOR 1
                writer.write("More beds.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()<=-35:####LOWER RIGHT SECTOR 1
                writer.write("Table where the soldiers ate.", move=False, align="left", font=("Arial", 8, "normal"))

            else:
                ##############NOT IN ANY SECTOR
                writer.write("Nothing of interest here.", move=False, align="left", font=("Arial", 8, "normal"))

        if len(current_room)==4:#####Room4#########THE STOREROOM

            if hero.xcor()<=-110 and hero.xcor()>=-209 and hero.ycor()>=15:####UPPER LEFT SECTOR 1
                if len(location_of_key)==0:
                    writer.write("Just bunch of crates.", move=False, align="left", font=("Arial", 8, "normal"))
                if len(location_of_key)>=0:
                    aquire_item("key")
            elif hero.xcor()<=-110 and hero.xcor()>=-209 and hero.ycor()<=-35:####LOWER LEFT SECTOR 1
                writer.write("More crates.", move=False, align="left", font=("Arial", 8, "normal"))   
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()>=15:####UPPER RIGHT SECTOR 1
                writer.write("Crates, crates, crates.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()<=-35:####LOWER RIGHT SECTOR 1
                writer.write("What's this? Oh it's a crate.", move=False, align="left", font=("Arial", 8, "normal"))

            else:
                ##############NOT IN ANY SECTOR
                writer.write("Nothing of interest here.", move=False, align="left", font=("Arial", 8, "normal"))
                
        if len(current_room)==5:######ROOM 5######THE LIBRARY
          
            if hero.xcor()<=-30 and hero.xcor()>=-280 and hero.ycor()>=15:####Top left bookcases
                if len(how_to_banish_void_creatures)==0:
                    writer.write("I get a strange feeling about these books.\nIt feels as if one of them is calling to me.", move=False, align="left", font=("Arial", 8, "normal"))
                elif len(how_to_banish_void_creatures)>=1:###Words of power.
                    aquire_item("words_of_power")
            elif hero.xcor()<=-57 and hero.xcor()>=-93 and hero.ycor()<=-35:####Story of George
                aquire_item("knowledge_of_correct_shield")
            elif hero.xcor()<=340 and hero.xcor()>=140 and hero.ycor()>=15:####Top right bookcases
                if len(knowledge_of_correct_sword)==0:
                    writer.write("A bunch of bookcases.", move=False, align="left", font=("Arial", 8, "normal"))
                elif len(knowledge_of_correct_sword)>=1:
                    aquire_item("how_to_slay_trolls")
            elif hero.xcor()<=-129 and hero.xcor()>=-174 and hero.ycor()<=-35:####How to banish void creatures
                aquire_item("how_to_banish_void_creatures")
            elif hero.xcor()<=312 and hero.xcor()>=276 and hero.ycor()<=-35:####Troll slayer knowledge
                aquire_item("knowledge_of_correct_sword")
            elif hero.xcor()<=205 and hero.xcor()>=165 and hero.ycor()<=-35:####Troll slayer knowledge
                aquire_item("how_to_slay_dragons")
                
            else:
                ##############NOT IN ANY SECTOR
                writer.write("Nothing of interest here.", move=False, align="left", font=("Arial", 8, "normal"))


        if len(current_room)==6:#####Room6#########THE ARMORY
            if hero.xcor()<=-174 and hero.xcor()>=-246 and hero.ycor()>=15:####Troll slayer
                writer.write("A table with weapons on it.", move=False, align="left", font=("Arial", 8, "normal"))
                aquire_item("troll_slayer_sword")
            elif hero.xcor()<=-57 and hero.xcor()>=-129 and hero.ycor()>=15:####Archery
                writer.write("The garrison's archery range.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=-120 and hero.xcor()>=-192 and hero.ycor()<=-35:####Generic Sword
                writer.write("A table with weapons on it.", move=False, align="left", font=("Arial", 8, "normal"))
                aquire_item("sword")
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()>=15:####Table
                writer.write("Just an ordinary table.", move=False, align="left", font=("Arial", 8, "normal"))
            elif hero.xcor()<=294 and hero.xcor()>=195 and hero.ycor()<=-35:####Generic Shields
                writer.write("A few suits of dented armor.", move=False, align="left", font=("Arial", 8, "normal"))
                aquire_item("shield")
                
            else:
                ##############NOT IN ANY SECTOR
                writer.write("Nothing of interest here.", move=False, align="left", font=("Arial", 8, "normal"))

    ###########CHECK FUNCTION#############
    def check():
    #################MOVEMENT BETWEEN ROOMS########################################
        if len(current_room)==1:
            if hero.xcor()>=340 :####go to level on right
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(-274,hero.ycor())
                wn.bgpic('images/room number2test.png')
                hero.showturtle()
                wn.title("The Hall of Heroes")
                current_room.append(1)
            if hero.xcor()<=-285:####go to level on left
                input3()
                new_room_sound()           
                hero.hideturtle()
                hero.goto(330,hero.ycor())
                wn.bgpic('images/room number6test.png')
                hero.showturtle()
                wn.title("The Armory")
                for i in range(5):
                    current_room.append(1)
            if hero.ycor()<=-162 :####go to level below
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(hero.xcor(),137)
                wn.bgpic('images/room number4test.png')
                hero.showturtle()
                wn.title("The Supply Room")
                for i in range(3):
                    current_room.append(1)
            if hero.ycor()>=144:####go to level above
                if len(key)==0:
                    hero.goto(hero.xcor(),hero.ycor()-(movement+1))
                elif len(key)>=1 and len(final_boss_creature)==1:##TROLL
                    input3()
                    for i in range(6):
                        current_room.append(1)
                    final_boss_sound()
                    hero.hideturtle()
                    wn.bgpic('images/boss_fights/troll/troll_encounter.png')
                    wn.title("The Final Showdown.")
                    input4()
                elif len(key)>=1 and len(final_boss_creature)==2:###DRAGON
                    input3()
                    for i in range(6):
                        current_room.append(1)
                    final_boss_sound()
                    hero.hideturtle()
                    wn.bgpic('images/boss_fights/dragon/dragon_encounter.png')
                    wn.title("The Final Showdown.")
                    input4()
                elif len(key)>=1 and len(final_boss_creature)==3:###DEMON
                    input3()
                    for i in range(6):
                        current_room.append(1)
                    final_boss_sound()
                    hero.hideturtle()
                    wn.bgpic('images/boss_fights/shapeless_demon/shapeless_demon_encounter.png')
                    wn.title("The Final Showdown.")
                    input4()
                
                
        if len(current_room)==2:
            if hero.xcor()>=340:####go to level on right
                hero.goto(hero.xcor()-(movement+1),hero.ycor())
            if hero.xcor()<=-285:####go to level on left
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(330,hero.ycor())
                wn.bgpic('images/room number1test.png')
                hero.showturtle()
                wn.title("The Dining Hall")
                current_room.pop()
            if hero.ycor()<=-162 :####go to level below
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(hero.xcor(),137)
                wn.bgpic('images/room number3test.png')
                hero.showturtle()
                wn.title("The Barracks")
                current_room.append(1)
            if hero.ycor()>=144 :####go to level above
                hero.goto(hero.xcor(),hero.ycor()-(movement+1))


                
        if len(current_room)==3:
            if hero.xcor()>=340 :####go to level on right
                hero.goto(hero.xcor()-(movement+1),hero.ycor())
            if hero.xcor()<=-285:####go to level on left
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(330,hero.ycor())
                wn.bgpic('images/room number4test.png')
                hero.showturtle()
                wn.title("The Supply Room")
                current_room.append(1)
            if hero.ycor()<=-162 :####go to level below
                hero.goto(hero.xcor(),hero.ycor()+(movement+1))
            if hero.ycor()>=144 :####go to level above
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(hero.xcor(),-155)
                wn.bgpic('images/room number2test.png')
                hero.showturtle()
                wn.title("The Hall of Heroes")
                current_room.pop()
        if len(current_room)==4:
            if hero.xcor()>=340 :####go to level on right
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(-274,hero.ycor())
                wn.bgpic('images/room number3test.png')
                hero.showturtle()
                wn.title("The Barracks")
                current_room.pop()
            if hero.xcor()<=-285:####go to level on left
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(330,hero.ycor())
                wn.bgpic('images/room number5test.png')
                hero.showturtle()
                wn.title("The Library")
                current_room.append(1)
            if hero.ycor()<=-162 :####go to level below
                hero.goto(hero.xcor(),hero.ycor()+(movement+1))
            if hero.ycor()>=144 :####go to level above
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(hero.xcor(),-155)
                wn.bgpic('images/room number1test.png')
                hero.showturtle()
                wn.title("The Dining Hall")
                for i in range(3):
                    current_room.pop()
                
            
        if len(current_room)==5:
            if hero.xcor()>=340:####go to level on right
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(-274,hero.ycor())
                wn.bgpic('images/room number4test.png')
                hero.showturtle()
                wn.title("The Supply Room")
                current_room.pop()
            if hero.xcor()<=-285:####go to level on left
                hero.goto(hero.xcor()+(movement+1),hero.ycor())
            if hero.ycor()<=-162 :####go to level below
                hero.goto(hero.xcor(),hero.ycor()+(movement+1))
            if hero.ycor()>=144 :####go to level above
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(hero.xcor(),-150)
                wn.bgpic('images/room number6test.png')
                hero.showturtle()
                wn.title("The Armory")
                current_room.append(1)

        if len(current_room)==6:
            if hero.xcor()>=340 :####go to level on right
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(-274,hero.ycor())
                wn.bgpic('images/room number1test.png')
                hero.showturtle()
                wn.title("The Dining Hall")
                for i in range(5):
                    current_room.pop()
            if hero.xcor()<=-285:####go to level on left
                hero.goto(hero.xcor()+(movement+1),hero.ycor())
            if hero.ycor()<=-162 :####go to level below
                input3()
                new_room_sound()
                hero.hideturtle()
                hero.goto(hero.xcor(),137)
                wn.bgpic('images/room number5test.png')
                hero.showturtle()
                wn.title("The Library")
                current_room.pop()
            if hero.ycor()>=144 :####go to level above
                hero.goto(hero.xcor(),hero.ycor()-(movement+1))
             
    ###############Generic Hero boundaries###################
        if hero.xcor()<=-48 and hero.ycor()>=35:###top left corner
            input3()
            hero.goto(hero.xcor(),hero.ycor()-(movement+1))
        if  hero.xcor()<=-30 and hero.ycor()>=35:
            input3()
            hero.goto(hero.xcor()+(movement+1),hero.ycor())
        if hero.xcor()>=105 and hero.ycor()>=35:###top right corner
            input3()
            hero.goto(hero.xcor(),hero.ycor()-(movement+1)) 
        if hero.xcor()>=100 and hero.ycor()>=35:
            input3()
            hero.goto(hero.xcor()-(movement+1),hero.ycor())  
        if hero.xcor()<=-48 and hero.ycor()<=-65 :###bottom left
            input3()
            hero.goto(hero.xcor(),hero.ycor()+(movement+1))  
        if hero.xcor()<=-30 and hero.ycor()<=-65 and hero.xcor()<=-30:
            input3()
            hero.goto(hero.xcor()+(movement+1),hero.ycor())  
        if hero.xcor()>=105 and hero.ycor()<=-65:###bottom right
            input3()
            hero.goto(hero.xcor(),hero.ycor()+(movement+1))
        if hero.xcor()>=100 and hero.ycor()<=-65:
            input3()
            hero.goto(hero.xcor()-(movement+1),hero.ycor())


    ###########AQUIRE ITEMS##########
    def aquire_item(type_item):
        item=type_item
        if item=="sword":
            if len(sword)>=1:
                pickup_sword=wn.textinput(" ","Put sword back? Y/N")
                if pickup_sword=="Y" or pickup_sword=="y":
                    sword.remove(1)
                input1()  
            else:
                pickup_sword=wn.textinput(" ","Found a sword!\nPick it up? Y/N")
                if pickup_sword=="Y" or pickup_sword=="y":
                    sword.append(1)
                input1()
                
        if item=="shield":
            if len(shield)>=1:
                pickup_shield=wn.textinput(" ","Put the shield back? Y/N")
                if pickup_shield=="Y" or pickup_shield=="y":
                    shield.remove(1)
                input1()  
            else:
                pickup_shield=wn.textinput(" ","Found a shield!\nEquip it? Y/N")
                if pickup_shield=="Y" or pickup_shield=="y":
                    shield.append(1)
                input1()
                  
        if item=="troll_slayer_sword" and len(knowledge_of_correct_sword)>=1:
            if len(troll_slayer_sword)>=1:
                pickup_item=wn.textinput(" ","Put trollslayer \nback? Y/N")
                if pickup_item=="Y" or pickup_item=="y":
                    troll_slayer_sword.remove(1)
                    sword.remove(1)
                input1()  
            else:
                pickup_item=wn.textinput(" ","Found troll slaying sword!\nPick it up? Y/N")
                if pickup_item=="Y" or pickup_item=="y":
                    troll_slayer_sword.append(1)
                    sword.append(1)
                input1()
            
        if item=="dragon_fire_shield" and len(knowledge_of_correct_shield)>=1:
            if len(dragon_fire_shield)>=1:
                pickup_shield=wn.textinput(" ","Put dragonfire shield \nback? Y/N")
                if pickup_shield=="Y" or pickup_shield=="y":
                    dragon_fire_shield.remove(1)
                    shield.remove(1)
                input1()  
            else:
                pickup_shield=wn.textinput(" ","Found dragonfire shield!\nEquip it? Y/N")
                if pickup_shield=="Y" or pickup_shield=="y":
                    dragon_fire_shield.append(1)
                    shield.append(1)
                input1()

        if item=="key" and len(location_of_key)>=1:
            if len(key)>=1:
                pickup_item=wn.textinput(" ","Put key back? Y/N")
                if pickup_item=="Y" or pickup_item=="y":
                    key.remove(1)
                input1()  
            else:
                pickup_item=wn.textinput(" ","Found key to throne room!\nPick it up? Y/N")
                if pickup_item=="Y" or pickup_item=="y":
                    key.append(1)
                input1()
            
        if item=="location_of_key":
            writer.write("There is a note from one of the garrison's soldiers.\nIt says that the key to the throne "
                         "room is located\nwithin the supply room in the northwest corner\nunder a crate.", move=False, align="left", font=("Arial", 10, "normal"))
            location_of_key.append(1)
                
        if item=="knowledge_of_correct_sword":
            writer.write("This book tells the story of Svengard the Trollslayer.\nHis sword is considered legendary"
                         " and \nis said to contain great magic.\nIt is currently on a table in the armory.\nHow disrespectful.", move=False, align="left", font=("Arial", 10, "normal"))
            knowledge_of_correct_sword.append(1)
            
        if item=="knowledge_of_correct_shield":
            writer.write("This book tells of a shield wielded by the\ndragon slayer George that could deflect "
                         "anything,\neven the fire of a dragon.\nHis suit of armor currently resides\nin the hall"
                         " of heroes.\nHe wore a blue plume and his heraldry\nwas yellow with a red X.", move=False, align="left", font=("Arial", 10, "normal"))
            knowledge_of_correct_shield.append(1)
            
        if item=="how_to_slay_dragons":
            writer.write("This book tells of a weak spot\non most dragons.\nOn their chest there is a hollow\n"
                         "of soft flesh behind which the heart\nof the dragon resides.", move=False, align="left", font=("Arial", 10, "normal"))
            how_to_slay_dragons.append(1)
            
        if item=="how_to_slay_trolls":
            writer.write("This book elaborates on how to slay trolls\nOne must decapitate one in order\n"
                         "to ensure that it will not regenerate.", move=False, align="left", font=("Arial", 10, "normal"))
            how_to_slay_trolls.append(1)
            
        if item=="how_to_banish_void_creatures":
            writer.write("This book speaks banishing shapeless demons to\nthe voids that they crawled from."
                         "\nIt says that only by knowing the correct \nwords of power can they be defeated "
                         "and banished.\nUnfortunately this book does not include those words.", move=False, align="left", font=("Arial", 10, "normal"))
            how_to_banish_void_creatures.append(1)
            
        if item=="words_of_power" and len(how_to_banish_void_creatures)>=1:
            
            writer.write("The is the book I sensed earlier.\nAll that is written are three words.\nVanqui,"
                         "Bestiari, Noctis.\nThis may be important to my quest.\nI should memorize these words.", move=False, align="left", font=("Arial", 10, "normal"))
            words_of_power.append(1)
            
    #####Determine boss        
    def final_boss():
        for i in range(random.randint(1,3)):
            final_boss_creature.append(1)
            

    #######Enter new room sound##########
    def new_room_sound():
        winsound.PlaySound('sounds\\door-1-open', winsound.SND_FILENAME)
        sound_roll=random.randint(1,3)
        if sound_roll==1:
            winsound.PlaySound('sounds\\Castle-of-Despair',winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        elif sound_roll==2:
            winsound.PlaySound('sounds\\Goblin-Loop',winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        elif sound_roll==3:
            winsound.PlaySound('sounds\\Chamber-of-Jewels',winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
            
    def final_boss_sound():
        winsound.PlaySound('sounds\\door-1-open', winsound.SND_FILENAME)
        winsound.PlaySound('sounds\\Into-Battle',winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
        
    def defeat_sound():
        winsound.PlaySound('sounds\\The-Darkness-Below_Looping',winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    def victory_sound():
        winsound.PlaySound('sounds\\Dont-Mess-with-the-8-Bit-Knight',winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)


    ###########EXIT GAME#########
    def leave():
        try:
            pickup_item=wn.textinput(" ","Restart? Y/N")
            if pickup_item=="Y" or pickup_item=="y":
                hero.clear()
                writer.clear()
                main()
            pickup_item=wn.textinput(" ","Exit game? Y/N")
            if pickup_item=="Y" or pickup_item=="y":
                wn.bgpic('images/Credits.png')
                hero.hideturtle()
                writer.hideturtle()
                time.sleep(9)
                turtle.bye()
                return False
        except ValueError:
            pass
        except TypeError:
            pass
        input1()
        
    def cheats():
        try:
            cheatNumber=int(wn.textinput("Cheat Menu","Enter number value for item\n1=sword,2=trollsword,3=shield\n4=drgnfrshield,5=key,6=kdrg7=ktrl,\n"\
                                         "8=kvoid,9=wordpower"))
            if cheatNumber==1:
                sword.append(1)
            if cheatNumber==2:
                troll_slayer_sword.append(1)
                sword.append(1)
            if cheatNumber==3:
                shield.append(1)
            if cheatNumber==4:
                dragon_fire_shield.append(1)
                shield.append(1)
            if cheatNumber==5:
                key.append(1)
            if cheatNumber==6:
                how_to_slay_dragons.append(1)
            if cheatNumber==7:
                how_to_slay_trolls.append(1)
            if cheatNumber==8:
                how_to_banish_void_creatures.append(1)
            if cheatNumber==9:
                words_of_power.append(1)
        except ValueError:
            pass
        except TypeError:
            pass
        input1()
        
        
    ##################END FUNCTION SECTION################################

        
    ########################VARIABLES AND STARTUP SECTION##############################################################################################
    #####STARTS THE MUSIC########
    winsound.PlaySound('sounds\\Castle-of-Despair',winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP )

    ###########Basic setup##########
    wn=turtle.Screen()
    wn.setup(width=1.0, height=1.0, startx=None, starty=None)

    ##ALL THE TURTLES######
    hero=turtle.Turtle()
    writer=turtle.Turtle()
    writer.penup()
    hero.penup()
    hero.hideturtle()
    writer.hideturtle()

    writer.goto(-600,0)


    #########IMPORT SPRITES############################################################
    ###NOTHING EQUIPED############
    hero_left1=("images/hero walk left1.gif")
    wn.addshape(hero_left1)
    hero_right1=("images/hero walk right1.gif")
    wn.addshape(hero_right1)
    hero_up1=("images/hero walk up1.gif")
    wn.addshape(hero_up1)
    hero_down1=("images/hero walk down1.gif")
    wn.addshape(hero_down1)
    hero_left2=("images/hero walk left2.gif")
    wn.addshape(hero_left2)
    hero_right2=("images/hero walk right2.gif")
    wn.addshape(hero_right2)
    hero_up2=("images/hero walk up2.gif")
    wn.addshape(hero_up2)
    hero_down2=("images/hero walk down2.gif")
    wn.addshape(hero_down2)
    ##############SWORD EQUIPED
    hero_leftsword1=("images/hero walk leftsword1.gif")
    wn.addshape(hero_leftsword1)
    hero_rightsword1=("images/hero walk rightsword1.gif")
    wn.addshape(hero_rightsword1)
    hero_upsword1=("images/hero walk upsword1.gif")
    wn.addshape(hero_upsword1)
    hero_downsword1=("images/hero walk downsword1.gif")
    wn.addshape(hero_downsword1)
    hero_leftsword2=("images/hero walk leftsword2.gif")
    wn.addshape(hero_leftsword2)
    hero_rightsword2=("images/hero walk rightsword2.gif")
    wn.addshape(hero_rightsword2)
    hero_upsword2=("images/hero walk upsword2.gif")
    wn.addshape(hero_upsword2)
    hero_downsword2=("images/hero walk downsword2.gif")
    wn.addshape(hero_downsword2)
    #########SHIELD EQUIPPED########shield
    hero_leftshield1=("images/hero walk leftshield1.gif")
    wn.addshape(hero_leftshield1)
    hero_rightshield1=("images/hero walk rightshield1.gif")
    wn.addshape(hero_rightshield1)
    hero_upshield1=("images/hero walk upshield1.gif")
    wn.addshape(hero_upshield1)
    hero_downshield1=("images/hero walk downshield1.gif")
    wn.addshape(hero_downshield1)
    hero_leftshield2=("images/hero walk leftshield2.gif")
    wn.addshape(hero_leftshield2)
    hero_rightshield2=("images/hero walk rightshield2.gif")
    wn.addshape(hero_rightshield2)
    hero_upshield2=("images/hero walk upshield2.gif")
    wn.addshape(hero_upshield2)
    hero_downshield2=("images/hero walk downshield2.gif")
    wn.addshape(hero_downshield2)
    ###########SWORD AND SHIELD EQUIPPED###########
    hero_leftswordshield1=("images/hero walk leftswordshield1.gif")
    wn.addshape(hero_leftswordshield1)
    hero_rightswordshield1=("images/hero walk rightswordshield1.gif")
    wn.addshape(hero_rightswordshield1)
    hero_upswordshield1=("images/hero walk upswordshield1.gif")
    wn.addshape(hero_upswordshield1)
    hero_downswordshield1=("images/hero walk downswordshield1.gif")
    wn.addshape(hero_downswordshield1)
    hero_leftswordshield2=("images/hero walk leftswordshield2.gif")
    wn.addshape(hero_leftswordshield2)
    hero_rightswordshield2=("images/hero walk rightswordshield2.gif")
    wn.addshape(hero_rightswordshield2)
    hero_upswordshield2=("images/hero walk upswordshield2.gif")
    wn.addshape(hero_upswordshield2)
    hero_downswordshield2=("images/hero walk downswordshield2.gif")
    wn.addshape(hero_downswordshield2)

    ########Movement Length#########
    movement=10

    #############Item lists##########

    sword=[]
    troll_slayer_sword=[]
    shield=[]
    dragon_fire_shield=[]
    key=[]
    knowledge_of_correct_sword=[]
    knowledge_of_correct_shield=[]
    how_to_slay_dragons=[]
    how_to_slay_trolls=[]
    how_to_banish_void_creatures=[]
    words_of_power=[]
    location_of_key=[]
    final_boss_creature=[]

    ############Start the game###########################
    final_boss()###ROLL for what monster will appear
    current_room=[1]
    wn.bgpic('images/room number1test.png')
    wn.title("The Dining Hall")
    hero.shape(hero_down1)
    hero.showturtle()
    input1()###starts hero input
    writer.color("white")##text color
    writer.write("You have found yourself in an abandoned dining hall.\nIt"
                 " appears everyone has left the castle due to fear.\nIt is"
                 " your quest to unlock the door to the throne room\nand fight"
                 " the evil locked within!\nPress arrow keys to move.\nPress"
                 " spacebar to investigate for clues.\nPress ESC at any time"
                 " to exit the game.", move=False, align="left", font=("Arial", 10, "normal"))
    wn.mainloop()
main()



