class Person:
    def __init__(self, name: str) -> None:
        self.__local = None
        self.__name = name
    
    def into_local(self) -> None:
        self.__local.turn_the_lights()
    
    def show_local(self) -> None:
        address = self.__local.get_address()
        print(address)

    def introduce_yourself(self) -> None:
        print('Hello, I am {}'.format(self.__name))

    def set_local(self, local: any) -> None:
        self.__local = local

    def get_local(self) -> any:
        return self.__local


