import pygame
import random

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
        mole_position = [0, 0]
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    position = list(event.pos)
                    position[0] = (position[0] // 32)
                    position[1] = (position[1] // 32)
                    if (mole_position[0] == position[0]) and (mole_position[1] == position[1]):
                        mole_position[0] = random.randrange(0, 19)
                        mole_position[1] = random.randrange(0, 15)

            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=((mole_position[0] * 32), (mole_position[1] * 32))))
            i = 1
            while i < 20:
                pygame.draw.line(screen, "dark blue", (32 * i, 0), (32 * i, 512))
                i += 1
            i = 1
            while i < 16:
                pygame.draw.line(screen, "dark blue", (0, 32 * i), (640, 32 * i))
                i += 1
            #screen.blit(mole_image, mole_image.get_rect(topleft=(0, 0)))
            #mole_position = [0, 0]

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
