import os,random
import time, sys

xp = 0
#colors

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"






os.system('clear')
def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.9)
		else:
			time.sleep(0.9)

typewriter(red + 'THE END')
time.sleep(2)
os.system('clear')
os.system('clear')
def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.08)
		else:
			time.sleep(0.2)


			
typewriter(red + 'VROOM, you here the sound of the bus. Your just playing video games on your phone. PEW, PEW, PEW. Then you hear a sudden thud. But that was normal for this crummy bus. You find a place to hide in your game and you look up to see what happend. You see that the new bus driver has side - swiped the curb. You think that it\'s normal for new people to fail once at their job. So you just move on. ')
time.sleep(2)
os.system('clear')
typewriter('You go back to playing your game.')
time.sleep(1)
os.system('clear')
ePaper = input('Would you like to try a game on your phone that your younger couson made you? You will get 200 more xp! \n[Y/N]\n').upper()
ePaper = ePaper.upper()
if ePaper == "Y":
 typewriter('You tap on the app')
 time.sleep(2)
 os.system('clear')
 game = ('█▀█ ▄▀█ █▄░█ █▄▀')
 game2 = ('\n█▀▄ █▀█ █░▀█ █░█')          
 time.sleep(1.5)
 os.system('clear')
 print()
 print()
 xr = ('\n██╗░░██╗')
 xs = ('\n╚██╗██╔╝')
 xd = ('\n░╚███╔╝░')
 xa = ('\n░██╔██╗░')
 xz = ('\n██╔╝╚██╗')
 xh = ('\n╚═╝░░╚═╝')
 typewriter(red + game)
 typewriter(red + game2)
 typewriter(red + xr)
 typewriter(red + xs)
 typewriter(red + xd)
 typewriter(red + xa)
 typewriter(red + xz)
 typewriter(red + xh)
 print()
 time.sleep(2)
 os.system('clear')
 print(yellow + """             
 						PAPER: THE GAME""")
  
 print(blue + "              PRESS ENTER")
 
 blank = ''
 inpt = input('')
 if inpt == blank:
 	os.system("clear")
 elif input != blank:
  	print(red + 'Please press Enter')
 else:
  print(red + 'An Error occured.\nPress Enter')
  time.sleep(5)
  os.system('clear')

## Now, the game
 enemies = [
     'Paper Demon',
     'Paper Throwing AI',
     'Oragami King',
     'Oragami Queen',
     'Oragami Prince',
     'Oragami Princess',
     'Paper God',
 ]
 enemy_name = random.choice(enemies)
 enemy_health = 120
 enemy_accuracy = 0.4
 enemy_damage = 15

 player_health = 80
 player_accuracy = 0.8
 player_damage = 20
 heals_left = 3
 heal_amount = 10  


 def heal_player(amount):
    global player_health

    player_health += amount
    player_health = player_health + amount


 def attack_enemy(amount):
     global enemy_health
     enemy_health -= amount
     print('You hit the enemy with your piece of your sharp paper!')


 def attack_player(amount):
     global player_health
     player_health -= amount
     print('You were hit by the enemies paper! ')


 print('A ' + enemy_name + ' has challenged you to a paper war!')
 print()
 while player_health > 0:
     print(enemy_name + ' HP: ' + str(enemy_health))
     print('Your HP: ' + str(player_health))
     print('Heals papers left: ' + str(heals_left))
     print()
     action = input('Attack or heal? ')
     print()

     if action == "attack":
         player_roll = random.randint(1, 10)

         if player_roll < player_accuracy * 10:
             attack_enemy(player_damage)

             if enemy_health <= 0:
                 print('You win, you beat (a) (the) ' + enemy_name +
                      '. You are now a paper master!!')
                 break
         else:
             print('You missed your paper shot!')

     elif action == 'heal':
         if player_health == 350:
            print('You have full health, you cannot use a heal paper.')
         else:
             if heals_left:
                 heal_player(heal_amount)
                 heals_left -= 1
             else:
                 print('You are out of heal paper!')

     time.sleep(1)
     enemy_roll = random.randint(1, 10)
     if enemy_roll < enemy_accuracy * 10:
        attack_player(enemy_damage)

        if player_health <= 0:
             print(
                'You got pummeled by the enemies papers, better luck next time!'
            )
        else:
         print(enemy_name + ' missed! ')

     print()
     print('******************')
     print()

 if player_health <= 0:
   looser = ( red + 'Your pretty mad that you lost, but whatever. You still played!!')
   typewriter(looser)
   time.sleep(1)
   os.system('clear')
   print('+ 200 XP')
   xp += 200
   time.sleep(2)
 
 elif enemy_health <= 0:
   wiiner = (red + 'You are pretty happy that you won! You played and won! ')
   typewriter(wiiner)
   time.sleep(1)
   os.system('clear')
   print('+ 200 XP')
   xp += 200
   time.sleep(2)
 os.system('clear')
elif ePaper == "N":
  typewriter('Your loss, lets move on. ')

#*********************************************************


print('______________________________* 1 HOUR LATER *_________________________________')
time.sleep(2)
os.system('clear')
typewriter('Your arrive at your house. Your moms greets you. "How was school bud? ". "Fine I guess, the newbie bus driver side-swiped the curb today."."Well, that\'s what you get when a school hires someone with no experince.". "Ok... well I\'m going up to my room to play some video games and Justin.". "K hon!"')
time.sleep(2)
os.system('clear')
typewriter(yellow + 'You run up to your room and get on your computer and call your closest friend, Justin. ')
time.sleep(2)
os.system('clear')
print('wat up dude?')
time.sleep(2)
print('not much, you?')
time.sleep(2)
print('welp, im gr8')
time.sleep(2)
print('wanna get on cod?')
time.sleep(2)
print('sure, No0b')
time.sleep(2)
print('OH, your on!!')
time.sleep(2)
os.system('clear')
typewriter(bcyan + 'You play a couple COD matches with Justin until you have to go to dinner. When you sre putting everything away, you see a box that looks like an old gameboy. You put it in your school backpack for the bus in case your phone died. The you ran downstairs for dinner. ')
