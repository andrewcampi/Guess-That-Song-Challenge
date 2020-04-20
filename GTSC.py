import os, vlc, glob, time
from random import randint

print("If error 'vlc mod does not exist':")
print("   - IPython Console: !pip install vlc")

#AllMyLoving = vlc.MediaPlayer("All My Loving (The Beatles) 60s.mp3")
#AllMyLoving.play()

#song1 = vlc.MediaPlayer(song[0])
#song1.play()
#Song1.stop()


class Song:
  def __init__(self, title, artist, year):
    self.title = title
    self.artist = artist
    self.year = year
  def __repr__(self):
    return_string = self.title + "," + self.artist + "," + self.year
    return return_string



def gather_songs():
  song = glob.glob("/Users/andrewcampi/Desktop/GTS_Challenge/*.mp3")

  for x in range(len(song)):
      song[x] = song[x][41:]

  song_50s = []
  song_60s = []
  song_70s = []
  song_80s = []
  song_90s = []
  song_2000 = []

  for x in range(len(song)):
      if song[x][-5:-8:-1] == "s05":
          song_50s.append(song[x])
      elif song[x][-5:-8:-1] == "s06":
          song_60s.append(song[x])
      elif song[x][-5:-8:-1] == "s07":
          song_70s.append(song[x])
      elif song[x][-5:-8:-1] == "s08":
          song_80s.append(song[x])
      elif song[x][-5:-8:-1] == "s09":
          song_90s.append(song[x])
      elif song[x][-5:-10:-1] == "+0002":
          song_2000.append(song[x])

  return song, song_50s, song_60s, song_70s, song_80s, song_90s, song_2000



def play_challenge_moderator(song):
  os.system('clear') 
  current_round = 0
  p1_name = input("Enter Player 1 Name: ")
  p2_name = input("Enter Player 2 Name: ")
  game_to = int(input("Enter points to play to: "))
  print("\nOverview: ")
  print("    - Player 1 and 2 will compete to guess the title and artist of the song first.")
  print("    - Correctly guessing the title:    +1 point")
  print("    - Correctly guessing the title:    +1 point")
  print("    - Incorrect guess:                 -1 point")
  print("    - The first player to", game_to, "points wins!")
  print("\nControls:")
  print("    -", p1_name +"'s buzzer:  z")
  print("    -", p2_name +"'s buzzer:  m")
  p1_points = 0
  p2_points = 0
  while p1_points<game_to and p2_points<game_to:
    current_round+=1
    print("\n\nRound",current_round,"starts in:")
    countdown = 10
    for x in range(countdown):
        time.sleep(1)
        print(countdown-x-1, "seconds...")
    
    song_select = randint(1,len(song))
    song_to_play = vlc.MediaPlayer(song[song_select])
    
    again = True
    while again == True:
        song_to_play.play()
        buzzer = input("Buzzer:")
        song_to_play.stop()
        if buzzer[0] == "z":
            print(p1_name, "can guess.")
        elif buzzer[0] == "m":
            print(p2_name, "can guess.")
        countdown = 10
        for x in range(countdown):
            time.sleep(1)
            print(countdown-x-1, "seconds...")
        choice = int(input("Buzz again? Yes[1], No[2]:"))
        if choice == 1:
            again = True
        elif  choice == 2:
            again = False
    
    #Get song name and artist
    song_name = song[song_select]
    for x in range(len(song[song_select])):
        if song[song_select][x] == "(":
            song_name = song_name[0:x]
    song_artist = song[song_select]
    index_start = 0
    index_end = 0
    for x in range(len(song[song_select])):
        if song[song_select][x] == "(":
            index_start = x
            index_start+=1
        if song[song_select][x] == ")":
            index_end = x
    song_artist = song[song_select][index_start:index_end]
    
    print("\n\nSong Name:", song_name)
    print("Song Artist:", song_artist)
            
            
    p1_round_points = int(input(p1_name+" round points:"))
    p2_round_points = int(input(p2_name+" round points:"))
    p1_points += p1_round_points
    p2_points += p2_round_points
    os.system('clear')
    print("\nRound complete. The Score is:")
    print("    -",p1_name,":",p1_points, "points")
    print("    -",p2_name,":",p2_points, "points")
    song.remove(song[song_select])
  if p1_points>p2_points:
    print("\n\n",p1_name,"wins!")
  elif p2_points>p1_points:
    print("\n\n",p2_name,"wins!")
  elif p1_points==p2_points:
    print("\n\nTie!")



def player_1_random(song, high_score):
  os.system('clear') 
  total_rounds = 10
  current_round = 0
  print("\nOverview: ")
  print("    - Correctly guessing the title:    +1 point")
  print("    - Correctly guessing the artist:   +1 point")
  print("    - Incorrect guess:                 -1 point")
  print("    - Play 10 Rounds!")
  print("    - Score = points/rounds")
  points = 0
  while current_round < total_rounds:
    current_round+=1
    print("\n\nRound",current_round,"starts in:")
    countdown = 10
    for x in range(countdown):
        time.sleep(1)
        print(countdown-x-1, "seconds...")
    
    song_select = randint(1,len(song))
    song_to_play = vlc.MediaPlayer(song[song_select])
    song_to_play.play()
    
    name_guess = input("Guess Song Name: ")
    artist_guess = input("Guess Aritst Name: ")
    
    song_to_play.stop()
    
    #Get song name and artist
    song_name = song[song_select]
    for x in range(len(song[song_select])):
        if song[song_select][x] == "(":
            song_name = song_name[0:x-1]
    song_artist = song[song_select]
    index_start = 0
    index_end = 0
    for x in range(len(song[song_select])):
        if song[song_select][x] == "(":
            index_start = x
            index_start+=1
        if song[song_select][x] == ")":
            index_end = x
    song_artist = song[song_select][index_start:index_end]
    print("\n\nSong Name:", song_name)
    print("Song Artist:", song_artist)
           
    name_correct = False
    artist_correct = False
    if name_guess.upper() == song_name.upper():
        points+=1
        name_correct = True
        print("Song Name: Correct (+1 point)")
    else:
        points-=1
        name_correct = False
        print("Song Name: Incorrect (-1 point)")
    if artist_guess.upper() == song_artist.upper():
        points+=1
        artist_correct = True
        print("Song Artist: Correct (+1 point)")
    else:
        points-=1
        arist_correct = False
        print("Song Name: Incorrect (-1 point)")
    
    
    print("\nRound complete:")
    print("    - Points:", points)
    score = points/10
    print("    - Current Score:", score)
    song.remove(song[song_select])
    

  return score


def jeopardy_board(list100,list200,list300,list400,list500):
  big_dash = 50
  print("-"*big_dash)
  print("|           Guess That Song Challenge           |")
  print("-"*big_dash)
  print("|  50s  |  60s  |  70s  |  80s  |  90s  | 2000+ |")
  print("-"*big_dash)
  list_of_list = [list100,list200,list300,list400,list500]
  for y in range(5):
    print("|", " ", end="")
    for x in range(6):
      print(list_of_list[y][x], end="")
      print( " ", "|",  " ", end="")
    print("")
  print("-"*big_dash)
  print("\n")



def player_2_jeopardy(song_50s, song_60s, song_70s, song_80s, song_90s, song_2000):
  list100 = [100,100,100,100,100,100]
  list200 = [200,200,200,200,200,200]
  list300 = [300,300,300,300,300,300]
  list400 = [400,400,400,400,400,400]
  list500 = [500,500,500,500,500,500]
  show_lists = [list100,list200,list300,list400,list500]
  os.system('clear') 
  
  board_50s = []
  board_60s = []
  board_70s = []
  board_80s = []
  board_90s = []
  board_2000 = []
  for x in range(5):
      num = randint(1,len(song_50s)-1)
      board_50s.append(song_50s[num])
      song_50s.remove(song_50s[num])
  for x in range(5):
      num = randint(1,len(song_60s)-1)
      board_60s.append(song_60s[num])
      song_60s.remove(song_60s[num])
  for x in range(5):
      num = randint(1,len(song_70s)-1)
      board_70s.append(song_70s[num])
      song_70s.remove(song_70s[num])
  for x in range(5):
      num = randint(1,len(song_80s)-1)
      board_80s.append(song_80s[num])
      song_80s.remove(song_80s[num])
  for x in range(5):
      num = randint(1,len(song_90s)-1)
      board_90s.append(song_90s[num])
      song_90s.remove(song_90s[num])
  for x in range(5):
      num = randint(1,len(song_2000)-1)
      board_2000.append(song_2000[num])
      song_2000.remove(song_2000[num])
  big_board = [board_50s, board_60s, board_70s, board_80s, board_90s, board_2000]

  p1_name = input("Enter Player 1 Name: ")
  p2_name = input("Enter Player 2 Name: ")
  p1_points = 0
  p2_points = 0
  
  current_round = 0
  while current_round<30:
      current_round +=1
      jeopardy_board(list100,list200,list300,list400,list500)
      category_select = input("(Winner of last round) Pick a category: ")
      calliber_select = int(input("(Winner of last round) Pick a point value: "))
      if calliber_select == 100:
          calliber_select = 0
      elif calliber_select == 200:
          calliber_select = 1
      elif calliber_select == 300:
           calliber_select = 2
      elif calliber_select == 400:
           calliber_select = 3
      elif calliber_select == 500:
           calliber_select = 4
      if category_select == "50s":
          category_select = 0
      elif category_select == "60s":
          category_select = 1
      elif category_select == "70s":
          category_select = 2
      elif category_select == "80s":
          category_select = 3
      elif category_select == "90s":
          category_select = 4
      elif category_select == "2000+":
          category_select = 5
      
      song_to_play = vlc.MediaPlayer(big_board[category_select][calliber_select])
      song_to_play.play()
      
      again = True
      while again == True:
          song_to_play.play()
          buzzer = input("Buzzer:")
          song_to_play.stop()
          if buzzer[0] == "z":
              print(p1_name, "can guess.")
          elif buzzer[0] == "m":
              print(p2_name, "can guess.")
          countdown = 10
          for x in range(countdown):
              time.sleep(1)
              print(countdown-x-1, "seconds...")
          choice = int(input("Buzz again? Yes[1], No[2]:"))
          if choice == 1:
              again = True
          elif  choice == 2:
              again = False
    
      #Get song name and artist
      song_name = big_board[category_select][calliber_select]
      for x in range(len(big_board[category_select][calliber_select])):
          if big_board[category_select][calliber_select][x] == "(":
              song_name = song_name[0:x]
      song_artist = big_board[category_select][calliber_select]
      index_start = 0
      index_end = 0
      for x in range(len(big_board[category_select][calliber_select])):
          if big_board[category_select][calliber_select][x] == "(":
              index_start = x
              index_start+=1
          if big_board[category_select][calliber_select][x] == ")":
              index_end = x
      song_artist = big_board[category_select][calliber_select][index_start:index_end]
    
      print("\n\nSong Name:", song_name)
      print("Song Artist:", song_artist)
      
      p1_round_points = int(input(p1_name+" round points (Full[1], Half[2], None[3], -Half[4], -Full[5]): "))
      p2_round_points = int(input(p2_name+" round points (Full[1], Half[2], None[3], -Half[4], -Full[5]): "))
      
      if calliber_select == 0:
          calliber_select = 100
      elif calliber_select == 1:
          calliber_select = 200
      elif calliber_select == 2:
           calliber_select = 300
      elif calliber_select == 3:
           calliber_select = 400
      elif calliber_select == 4:
           calliber_select = 500
      
      if p1_round_points == 1:
          p1_points += calliber_select
      elif p1_round_points == 2:
          p1_points += calliber_select/2
      elif p1_round_points == 3:
          p1_points += 0
      elif p1_round_points == 4:
          p1_points -= calliber_select
      elif p1_round_points == 5:
          p1_points -= calliber_select/2
      
      if p2_round_points == 1:
          p2_points += calliber_select
      elif p2_round_points == 2:
          p2_points += calliber_select/2
      elif p2_round_points == 3:
          p2_points += 0
      elif p2_round_points == 4:
          p2_points -= calliber_select
      elif p2_round_points == 5:
          p2_points -= calliber_select/2
      
      os.system('clear')
      print("\nRound complete. The Score is:")
      print("    -",p1_name,":",p1_points, "points")
      print("    -",p2_name,":",p2_points, "points")
      
      if calliber_select == 100:
          calliber_select = 0
      elif calliber_select == 200:
          calliber_select = 1
      elif calliber_select == 300:
           calliber_select = 2
      elif calliber_select == 400:
           calliber_select = 3
      elif calliber_select == 500:
           calliber_select = 4
      
      show_lists[calliber_select][category_select] = "---"
  
  if p1_points > p2_points:
      print(p1_name, "wins!")
  elif p2_points > p1_points:
      print(p2_name, "wins!")
  elif p1_points == p2_points:
      print("Tie!")
 


def player_1_jeopardy():  
  pass



def main():
  song, song_50s, song_60s, song_70s, song_80s, song_90s, song_2000 = gather_songs()
  
  play_again = True
  os.system('clear') 
  print("Welcome to 'Guess That Song Challenge 2019'.")
  print("\nGame Modes:")
  print(" - [1] '2 player random song' with moderator")
  print(" - [2] '1 player random song' (self-type)")
  print(" - [3] '2 player Jeopardy' with moderator")
  mode = int(input("\nSelect game mode [1][2][3]:"))
  
  if mode == 1:
    while play_again == True:
      play_challenge_moderator(song)
      question = input("Play again? ([1]Yes or [2]No):")
      if question == "1":
        play_again = True
      else:
        play_again = False
        
  if mode == 2:
    high_score = 0
    while play_again == True:
      score = player_1_random(song, high_score)
      if score > high_score:
          high_score = score
      print("\n\nScore:", score)
      print("High Score:", high_score)
      question = input("Play again? ([1]Yes or [2]No):")
      if question == "1":
        play_again = True
      else:
        play_again = False
        
  if mode == 3:
    player_2_jeopardy(song_50s, song_60s, song_70s, song_80s, song_90s, song_2000)
    

main()
