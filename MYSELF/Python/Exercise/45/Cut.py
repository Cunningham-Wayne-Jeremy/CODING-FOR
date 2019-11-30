class Scenes(object)

    def description(self):
        print("Describe what happens in the scene!")

    def timedresponse(self, reason, count):
        self.count = count
        self.reason = reason
        userinput = input("What do you do? ")
        t = Timer(count, Death.enter())
        t.start()


# description
# if input == grab rope * 3:
# return self.t.cancel
# if statements
#
