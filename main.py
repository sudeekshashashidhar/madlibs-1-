import random

when = ["Yesterday", "A few weeks ago", "Today morning"]
where = ["Pet Store"]
pet = ["Dog", "Bird", "Fish"]
emotion_of_pet = ["Scared", "Excited", "Nervous", "Protective"]
with_who = ["Mom", "Dad", "Sister", "Brother", "Grandma", "Grandpa", "Friends"]
cost = ["too expensive", "good price", "sale price"]
at_home = ["settled", "scared", "shy", "protective", "home sick", "energetic", "curious"]
name = ["Bella", "Ruby", "Boomer", "Viper", "Kane"]

print(random.choice(when) + ", we went to the " + random.choice(where) + " to find my dream pet, a " + random.choice(pet) + ", with my " + random.choice(with_who) + ". When we got to the store, the owner showed us my choice of pet and we followed him. There was this particular pet that I felt a special bond with it. It was " + random.choice(emotion_of_pet) + ". After a tough decision I told the owner that I will take it. It was ", random.choice(cost) + " to buy it. I named it " + random.choice(name) + ". After a few days, it was " + random.choice(at_home) + ". I am very happy with my pet." )
