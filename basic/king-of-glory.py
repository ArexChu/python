#coding: utf-8

class Hero():
    name = ""
    category = ""
    output = ""
    skill = ""
    def __init__(self,name,category,output,skill):
        self.name = name
        self.category = category
        self.output = output
        self.skill = skill
    def steal_red_buff(self):
        self.output -= 300
    def solo(self):
        self.output -= 500
    def add_blood(self):
        self.output += 200

kai = Hero("凯","战士",1000,"极刃风暴")
wangzhaojun = Hero("王昭君","法师",1000,"凛冬将至")
ake = Hero("阿轲","刺客",1000,"瞬华")

kai.steal_red_buff()
kai.add_blood()

print(kai.output)
