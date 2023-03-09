import pyxel


class Background:
    def __init__(self):
        self.start = pyxel.frame_count
        self.images = []  # active images
        self.kind = ([0, -127, 0, 24, 0, 141, 127, 8], [50, -80, 0, 0, 128, 180, 80, 8],
                     [147, -96, 0, 147, 0, 109, 96, 8])

    def update(self):
        if (pyxel.frame_count - self.start) % 256 == 1:
            self.create_image()

        for i in range(len(self.images) - 1, -1, -1):
            self.images[i][1] += 1
            if self.images[i][1] > pyxel.height:
                del(self.images[i])

    def draw(self):
        pyxel.cls(5)
        pyxel.pal(5, 3)
        for image in self.images:
            pyxel.blt(*tuple(image))
        pyxel.pal()

    def create_image(self):
        i = pyxel.rndi(0, len(self.kind) - 1)
        self.images.append(self.kind[i].copy())
