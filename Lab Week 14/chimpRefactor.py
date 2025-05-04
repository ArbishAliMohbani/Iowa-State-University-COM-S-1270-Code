#!/usr/bin/env python
"""
chimpRefactor.py
Created: April 27, 2025
Lab: Week 14
Description: A refactored version of the chimp.py game that implements inheritance with
             an Entity parent class for the game objects.
"""

# Import Modules
import os
import pygame

# classes for our game objects
class Entity(pygame.sprite.Sprite):
    """Base class for game entities that handles image loading and initialization"""
    
    def __init__(self, data_dir, image_name, colorkey=None, scale=1):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        
        # Load the image (previously in load_image function)
        fullname = os.path.join(data_dir, image_name)
        self.image = pygame.image.load(fullname)
        self.image = self.image.convert()
        
        self.image = pygame.transform.scale_by(self.image, scale)
        
        if colorkey is not None:
            if colorkey == -1:
                colorkey = self.image.get_at((0, 0))
            self.image.set_colorkey(colorkey, pygame.RLEACCEL)
            
        self.rect = self.image.get_rect()


class Fist(Entity):
    """moves a clenched fist on the screen, following the mouse"""

    def __init__(self, data_dir):
        super().__init__(data_dir, "fist.png", -1)  # call Entity initializer
        self.fist_offset = (-235, -80)
        self.punching = False

    def update(self):
        """move the fist based on the mouse position"""
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos
        self.rect.move_ip(self.fist_offset)
        if self.punching:
            self.rect.move_ip(15, 25)

    def punch(self, target):
        """returns true if the fist collides with the target"""
        if not self.punching:
            self.punching = True
            hitbox = self.rect.inflate(-5, -5)
            return hitbox.colliderect(target.rect)

    def unpunch(self):
        """called to pull the fist back"""
        self.punching = False


class Chimp(Entity):
    """moves a monkey critter across the screen. it can spin the
    monkey when it is punched."""

    def __init__(self, data_dir):
        super().__init__(data_dir, "chimp.png", -1, 4)  # call Entity initializer
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 90
        self.move = 18
        self.dizzy = False

    def update(self):
        """walk or spin, depending on the monkeys state"""
        if self.dizzy:
            self._spin()
        else:
            self._walk()

    def _walk(self):
        """move the monkey across the screen, and turn at the ends"""
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, True, False)
        self.rect = newpos

    def _spin(self):
        """spin the monkey image"""
        center = self.rect.center
        self.dizzy = self.dizzy + 12
        if self.dizzy >= 360:
            self.dizzy = False
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        """this will cause the monkey to start spinning"""
        if not self.dizzy:
            self.dizzy = True
            self.original = self.image


def load_sound(data_dir, name):
    class NoneSound:
        def play(self):
            pass

    if not pygame.mixer.get_init():
        return NoneSound()

    fullname = os.path.join(data_dir, name)
    
    try:
        sound = pygame.mixer.Sound(fullname)
        return sound
    except pygame.error:
        print(f"Warning: Could not load sound file: {fullname}")
        return NoneSound()


def main():
    """this function is called when the program starts.
    it initializes everything it needs, then runs in
    a loop until the function returns."""
    # Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((1280, 480), pygame.SCALED)
    pygame.display.set_caption("Monkey Fever")
    pygame.mouse.set_visible(False)
    
    # Move global code into main()
    if not pygame.font:
        print("Warning, fonts disabled")
    if not pygame.mixer:
        print("Warning, sound disabled")

    main_dir = os.path.split(os.path.abspath(__file__))[0]
    data_dir = os.path.join(main_dir, "data")

    # Create The Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((170, 238, 187))

    # Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 64)
        text = font.render("Pummel The Chimp, And Win $$$", True, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width() / 2, y=10)
        background.blit(text, textpos)

    # Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Prepare Game Objects
    whiff_sound = load_sound(data_dir, "whiff.wav")
    punch_sound = load_sound(data_dir, "punch.wav")
    chimp = Chimp(data_dir)  # Pass data_dir to the constructor
    fist = Fist(data_dir)    # Pass data_dir to the constructor
    all_sprites = pygame.sprite.RenderPlain((chimp, fist))
    clock = pygame.time.Clock()

    # Main Loop
    going = True
    while going:
        clock.tick(60)

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if fist.punch(chimp):
                    punch_sound.play()  # punch
                    chimp.punched()
                else:
                    whiff_sound.play()  # miss
            elif event.type == pygame.MOUSEBUTTONUP:
                fist.unpunch()

        all_sprites.update()

        # Draw Everything
        screen.blit(background, (0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


# this calls the 'main' function when this script is executed
if __name__ == "__main__":
    main()
