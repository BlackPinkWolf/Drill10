from pico2d import load_image


class Grass:
    image = None
    def __init__(self):
        if Grass.image == None:
            Grass.image =  load_image('grass.png')

    def draw(self):
        self.image.draw(400, 60)
        self.image.draw(400, 50)


    def update(self):
        pass
