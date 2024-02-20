import random

class BoxingBot:
    def __init__(self) -> None:
        self.punches = ['Jab',
                        'Cross', 
                        'Rear Hook',
                        'Lead Hook',
                        'Lead Uppercut',
                        'Rear Uppercut',
                        'Overhand',
                        'Double Jab',
                        'Cross Body Shot',
                        'Hook Body Shot',
                        'Liver Shot'
                        ]
        
        self.dodges = ['Slip Left',
                       'Slip Right',
                       'Bob and weave',
                       'Duck',
                       'Pull back',
                       'Parry',
                       'Block Left',
                       'Block right',
                       'Angle change'
                       ]
        pass


    def getPunchesCombination(self, count):
        if count > len(self.punches):
            raise ValueError("Count should not exceed the number of available punches.")
        
        return random.sample(self.punches, count)
    
    def getDodgesCombination(self, count):
        if count > len(self.dodges):
            raise ValueError("Count should not exceed the number of available dodges.")
        
        return random.sample(self.dodges, count)
    
    
