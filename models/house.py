from typing import Type

class House:
    
    def __init__(self) -> None:
        self.__address = "Street of Lemon Trees"
        self.__owner = None
    
    def turn_the_lights(self) -> None:
        print('I am turning on the lights')
    
    def get_address(self) -> str:
        return self.__address

    def set_owner(self, owner: any) -> None:
        self.__owner = owner
    
    def get_owner(self) -> any:
        return self.__owner
