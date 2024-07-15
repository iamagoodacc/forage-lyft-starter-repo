from tyres.tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear

    def needs_service(self):
        for value in self.tyre_wear:
            if value >= 0.9:
                return True
        return False