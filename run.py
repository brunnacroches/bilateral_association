from models import House, Person

house_maria = House()
maria = Person('Maria')

maria.set_local(house_maria)
house_maria.set_owner(maria)

owner = house_maria.get_owner()
owner.introduce_yourself()

maria.show_local()
