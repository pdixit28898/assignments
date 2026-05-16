# print(""" INSTRUCTIONS
# 1. Game consist of total 5 questions. Each question carrys points
# to different question respectively. If you answered correct, 
# you'll get points, if you don't, no points would be given.
# You can also skip the question if you want; to skip question-
# just type "s" at any point """)
# strt=input("Do you want to start the game? yes/no=")
# score=0
# crct=0
# wrng=0
# skpd=0

# if strt=="yes":
#    print("""    WELCOME
#                   to
#                   the  
#                   KBC
#    its time to win some points.
#    All the best👍👍👍👍👍👍👍👍👍
#    """)
#    q1=input("""
   
#    Q1. What is the capital of India?
   
#    type o for the options or s to skip :-  """)
#    if q1=="o":
#       ans1=input("""
#       a.Lucknow               b.Mumbai
#       c.Delhi                 d.Chennai 
#                      your answer =  """)
#       if ans1=="c":
#          print("Right answer")
#          score=score+1000
#          crct=crct=1
#       elif ans1== "a" or ans1== "b" and ans1=="d":
#          print("Wrong answer")
#          wrng=wrng+1
#       else:
#          print("invalid input")  
#    else:
#       print("skipped") 
#       skpd=skpd+1
                   
#    q2=input("""

#    Q2. In which city Taj Mahal is situated? 
   
#    type o for the options or s to skip :-  """)
#    if q2=="o":
#       ans2=input("""
#    a.Delhi                  b.Kolkata
#    c.kanpur                 d.Agra           
#                         your answer =   """)
#       if ans2=="d":
#          print("Right answer")
#          score=score+2000
#       elif ans2== "a" or ans2== "b" and ans1=="c" :
#          print("Wrong answer")
#          wrng=wrng+1
#       else:
#          print("invalid input") 
       
#    else:
#       print("skipped")
#       skpd=skpd+1
        
#    q3=input("""
#    Who is the PM of India?
   
#    type o for the options or s to skip :-  """)
#    if q3=="o":
#       ans3=input("""
#    a.Rahul Gandhi           b.Amitabh Bachchan
#    c.Narendra Modi          d.Donald trump
#                            your answer =  """)
#       if ans3=="c":
#          print("Right answer")
#          score=score+3000
#          crct=crct+1
         
#       elif ans3== "a" or ans3== "b" and ans3=="d" :
#          print("Wrong answer")
#          wrng=wrng+1 
        
#       else:
#          print("invalid input")

#    else:
#       print("skipped")
#       skpd=skpd+1
      
     
#    q4=input("""
#    What is the national flower of india? 
      
#     type o for the options or s to skip :-  """)
#    if q4=="o":
#       ans4=input(""" 
#    a.Lotus                  b.Rose
#    c.Lily                   d.Sunflower 
#                               your answer=   """)
#       if ans4=="a":
#          print("Right answer")
#          score=score+4000
#          crct=crct+1
      
#       elif ans4== "c" or ans4== "b" and ans4=="d" :

#          print("Wrong answer")
#          wrng=wrng+1
         
#       else:
#          print("invalid input") 
#    else:
#       print("skipped")
#       wrng=wrng+1
      
      
#    q5=input("""
#    Wnat is the Currency of India? 
   
#    type o for the options or s to skip :-  """)
#    if q5=="o":
#       ans5=input("""
#    a.Rupee                  b.Taka
#    c.Yen                    d.Dollar 
#                         your answer=   """)
#       if ans5=="a":

#          print("Right answer")
#          score=score+5000
#          crct=crct+1
         
#       elif ans5== "c" or ans5== "b" and ans5=="d" :

#          print("Wrong answer")
#          wrng=wrng+1 
         
#       else:
#          print("invalid input") 

#    else:
#       print("skipped")
#       skpd=skpd+1
      
# else:
#     print("Thank you. But you should play the game. Atleast try one time")

# print(f"Correct answer= {crct}")
# print(f"Wrong answer = {wrng} ")
# print(f"Skipped Questions= {skpd} ")
# print(f"Total score = {score} ")