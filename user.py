class User:
    is_rewards_member = False
    gold_card_points = 0
    def __init__(self,first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

    def display_info(self):
        print(F"{self.first_name }\n {self.last_name} \n {self.email} \n {self.age} \n {self.gold_card_points} \n {self.is_rewards_member}")

    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        print(self.gold_card_points,self.is_rewards_member)
    
    def spend_points(self,spent):
        self.gold_card_points -= spent

Josh = User("Josh", "Remulla", "yahoo@yehaw.com", 31)

Ashley = User("Ashley", "Remulla", "google@gmail.com", 28)

Kai =User("Kai", "Rin", "retriever@shiba.com", 13)

Josh.enroll()

Josh.spend_points(50)

Ashley.enroll()

Ashley.spend_points(80)

Josh.display_info()
Ashley.display_info()
Kai.display_info()