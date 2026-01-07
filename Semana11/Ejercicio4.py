class Head:
    def __init__(self):
        pass

class Torso:
    def __init__(self,head,right_arm,left_arm,right_leg,left_leg,feet):
        self.head = head
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.right_leg = right_leg
        self.left_leg = left_leg
        self.feet = feet

class Arm:
    def __init__(self,hand):
        self.hand = hand

class Hand:
    def __init__(self):
        pass

class Leg:
    def __init__(self):
        pass

class Feet:
    def __init__(self):
        pass

class Human:
    def __init__(self,torso):
        self.torso = torso

head = Head()
right_hand = Hand() 
left_hand = Hand()
right_arm = Arm(right_hand)
left_arm = Arm(left_hand)
right_leg = Leg()
left_leg = Leg()
feet = Feet()
torso = Torso(head,right_arm,left_arm,right_leg,left_leg,feet)
human = Human(torso)
