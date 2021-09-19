# Antartica beta test
# No sounds, only 1 block to place
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
def main():

    texture1 = "assets/block.jpg"
    texture2 = "assets/block2.png"
    texture3 = "assets/block3.png"
    block_id = 1

    app = Ursina()


    def uptade():
        global block_id
        if held_keys['1']:
            block_id = 1
        if held_keys['2']:
            block_id = 2
        if held_keys['3']:
            block_id = 3


    class Voxel(Button):
        def __init__(self, position=(0, 0, 0), texture=texture3):
            super().__init__(
                parent=scene,
                position=position,
                model="cube",
                color=color.white,
                origin_y=0.5,
                texture=texture,
                highlight_color=color.gray
            )

        def input(self, key):
            if self.hovered:
                if key == 'p':
                    if block_id == 1:
                        voxel = Voxel(position=self.position +
                                      mouse.normal, texture=texture2)
                    elif block_id == 2:
                        voxel = Voxel(position=self.position +
                                      mouse.normal, texture=texture2)
                    elif block_id == 3:
                        voxel = Voxel(position=self.position +
                                      mouse.normal, texture=texture3)
                if key == 'o':
                    destroy(self)


    class Sky(Entity):
        def __init__(self):
            super().__init__(
                parent=scene,
                model="sphere",
                texture="assets/sky.jfif",
                scale=300,
                double_sided=True
            )


    for z in range(32):
        for x in range(32):
            voxel = Voxel(position=(x, 0, z))

    sky = Sky()

    player = FirstPersonController()

    app.run()

if __name__ == "__main__":
    main()