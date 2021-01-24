# The final version of this code is not yet available

from random import randint
import random

status = "user" # Choice between user or admin statues

if status == "admin":
    transform = input("Your topics : ")
else:
    transform = "Animal Bricolage Décoration Education Informatique Loisir"
    
topics = transform.split(" ")

class Favorite:
    def __init__(self, topics):
        self.topics = topics
        self.nblike = dict.fromkeys(topics,0)
        self.nbDislike = dict.fromkeys(topics, 0)
        
    def __repr__(self):
        return f"{self.topics}"
    
    def trier(self):
        n = 5
        while True:
            doit_continuer = False
            i = random.choice(self.topics)
            for search in topics:
                if self.nblike[search] + self.nbDislike[search] < 5:
                    doit_continuer = True
            answer = input(f"{i} | Like or no like : ")
            if answer == "like":
                self.nblike[i] += 1
            elif answer == "no":
                self.nbDislike[i] += 1
            if doit_continuer == False:
                break
            
            

        print(f"Like : {self.nblike}")
        print(f"Dislike : {self.nbDislike}")
        
    
user = Favorite(topics)
