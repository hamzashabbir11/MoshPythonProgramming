class Developer:
    def __init__(self,name,talk) -> None:
        self.name=name
        self.talk=talk

Speaker1=Developer('Sumama','LinkdIn')
print(Speaker1.name)
print(Speaker1.talk)
Speaker2=Developer('Adil','DevOps')
print(Speaker2.name)
print(Speaker2.talk)


class DataScience(Developer):
    pass

datastudent1=DataScience('Anis','Towards Data Science ')
print(datastudent1.name)
print(datastudent1.talk)