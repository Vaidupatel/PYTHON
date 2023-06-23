class Dad:
    basketball = 1


class Son(Dad):
    dance = 1

    def isdance(self):
        return f"Yes i dance {self.dance} no of times"


class Grandson(Son):
    dance = 6

    def isdance(self):
        return f"Yes i dance very awesomely {self.dance} no of times "


darry = Dad()
laryy = Son()
harry = Grandson()


print(harry.isdance())
print(harry.basketball)
