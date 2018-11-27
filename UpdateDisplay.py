
class UpdateDisplay:
    def __init__(self):
        self.targets = []

    def add(self, target):
        self.targets.append(target)

    def update(self):
        for target in self.targets:
            target()
