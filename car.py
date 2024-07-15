from abc import ABC, abstractmethod
from datetime import date

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class Serviceable:
    def needs_service():
        pass

class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
        self.engine = Engine()
        self.battery = Battery()    

    @abstractmethod
    def needs_service(self):
        pass

class Engine:
    def needs_service():
        pass 

class Battery:
    def needs_service():
        pass   

class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Calliope:
        return Calliope(CapuletEngine(last_service_date, current_mileage, last_service_mileage))

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Glissade:
        return Glissade(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage))

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Palindrome:
        return Palindrome(SternmanEngine(last_service_date, warning_light_on))

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Rorschach:
        return Rorschach(WilloughbyEngine(last_service_date, current_mileage, last_service_mileage))

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Thovex:
        return Thovex(CapuletEngine(last_service_date, current_mileage, last_service_mileage))
