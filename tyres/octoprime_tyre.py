from tyres.tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, tyre_wear):
        self.tyre_wear = tyre_wear

    def needs_service(self):
        total = 0
        for value in self.tyre_wear:
            total += value
        if total >= 3:
            return True
        return False