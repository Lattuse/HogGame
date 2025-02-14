import pygame, math, random

pygame.init()
dead = False
#Initialize variables:
count = 0
clock = pygame.time.Clock()
screen_width = 1280
screen_height = 720
surface = pygame.display.set_mode((screen_width,screen_height))
green = 0,255,0
red = 255,0,0
blue = 0,0,255
yellow = 255,255,0
white = 255,255,255
black = 0,0,0
background = pygame.image.load('all_sprites/background.png').convert_alpha()
background = pygame.transform.scale(background, (screen_width, screen_height))
# Background Music
pygame.mixer.init()
pygame.mixer.music.load("audio/sabaton.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.2)
# Texts and Fonts
font = pygame.font.SysFont('Arial', 36)
end = font.render('Game Over, press LMB to continue', True, 'black')
frame_index = 1

#pictures for animations

mage_left = []
mage_right = []
mage_forward = []
mage_back = []
mage_other = []

enemies_anim = pygame.transform.scale(pygame.image.load("all_sprites/hog.png").convert_alpha(), (100,100))


# adding animations loop
for i in range(1, 6):
    mage_left.append(pygame.transform.scale(pygame.image.load("all_sprites/player_left/" + str(i) + ".png").convert_alpha(), (100,100)))
for i in range(1, 6):
    mage_right.append(pygame.transform.scale(pygame.image.load("all_sprites/player_right/" + str(i) + ".png").convert_alpha(), (100,100)))
for i in range(1, 6):
    mage_forward.append(pygame.transform.scale(pygame.image.load("all_sprites/player_forward/" + str(i) + ".png").convert_alpha(), (100,100)))
for i in range(1, 6):
    mage_back.append(pygame.transform.scale(pygame.image.load("all_sprites/player_back/" + str(i) + ".png").convert_alpha(), (100,100)))

mage_other.append(pygame.image.load("all_sprites/player_forward/1.png"))


mage = mage_other[0].convert_alpha()
mage = pygame.transform.scale(mage, (100,100))


class Square:

    def __init__(self, pos, height, width, color, speed):
        self.image = pygame.Surface((width,height))
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = speed
        self.color = color
    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Player(Square):

    def __init__(self, pos, height, width, color, speed, img):
        super().__init__(pos, height, width, color, speed)
        self.image = img
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = speed

    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        self.pos += self.direction * self.speed * dt
        self.rect.center = self.pos

    def collided(self, other_rect):
        return self.rect.colliderect(other_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


#Inheritance
class Bullet(Square):
    def __init__(self, pos , speed, height, width, color, targetx,targety):
        super().__init__(pos, height, width, color, speed)
        self.height = 10
        self.width = 10
        x = pos[0]
        y = pos[1]
        angle = math.atan2(targety-y, targetx-x) #get angle to target in rads
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        self.x = x
        self.y = y

    def move(self, dt):

        self.x += self.dx * dt
        self.y += self.dy * dt
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)


#Build a square
sq = Player((640,360), 100, 100,'red', 500, mage)

bullets = []
enemies = []

#Main program loop
done = False
while not done:
    dt = clock.tick() / 1000
    if dead == False:
        #Get user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                #print(x,y)
                b = Bullet(sq.pos, 1500, 20, 20, 'white', x, y)
                bullets.append(b)

        #Handle held down keys
        keys = pygame.key.get_pressed()        

        if keys[pygame.K_UP]:
            if sq.pos[1] >= 0:
                sq.direction.y = -1
            else: sq.direction.y=0
            frame_index += 5 * dt
            if frame_index >= 5:
                frame_index = 0
            sq.image = mage_forward[int(frame_index)]
        elif keys[pygame.K_DOWN]:
            if sq.pos[1] <= 720:
                sq.direction.y = +1
            else: sq.direction.y=0
            frame_index += 5 * dt
            if frame_index >= 5:
                frame_index = 0
            sq.image = mage_back[int(frame_index)]
        else:
            sq.direction.y = 0
        
        if keys[pygame.K_RIGHT]:
            if sq.pos[0] <= 1280:
                sq.direction.x = +1
            else: sq.direction.x=0
            frame_index += 5 * dt
            if frame_index >= 5:
                frame_index = 0
            sq.image = mage_right[int(frame_index)]

        elif keys[pygame.K_LEFT]:
            if sq.pos[0] >= 0:
                sq.direction.x = -1
            else: sq.direction.x=0
            frame_index += 5 * dt
            if frame_index >= 5:
                frame_index = 0
            sq.image = mage_left[int(frame_index)]

        else:
            sq.direction.x = 0
            
        #Update game objects
        for b in bullets:
            b.move(dt)
        for e in enemies:
            e.move(dt)
        #spawn enemies on the top of the screen and tell them to move down
        if random.randint(1,50) == 15 and len(enemies)<5: #15 doesn't matter
            x = random.randint(0,screen_width-40)
            e = Player((x,0), 50, 50, 'yellow', 100, enemies_anim)
            e.direction.y = +1
            enemies.append(e)
        #collisions and death(
        for i in reversed(range(len(bullets))):
            for j in reversed(range(len(enemies))):
                if sq.collided(enemies[j].rect):
                    pass

                if bullets[i].collided(enemies[j].rect):
                    #e.color = white #TESTING
                    count+=1
                    del enemies[j]
                    del bullets[i]
                    break
        surface.blit(background, (0,0))
        for i in reversed(range(len(enemies))):
            if enemies[i].pos[1] > 700:
                    dead = True
                    
            surface.blit(enemies_anim, (enemies[i].pos[0]-50,enemies[i].pos[1]-50))
            if sq.collided(enemies[i].rect):
                dead = True
        #All the drawing
        #fill surface with black
        for b in bullets:
            b.draw(surface)

        sq.move(dt)
        surface.blit(sq.image, (sq.pos[0]-50,sq.pos[1]-50))

        score_surface = font.render('Your score: ' + str(count), True, 'black')
        text_rect = score_surface.get_rect()
        text_rect.center = (100, 50)
        pygame.draw.rect(surface, 'white', text_rect)
        surface.blit(score_surface, text_rect)
    if dead:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        surface.fill("white")
        surface.blit(end, (220, 200))
        surface.blit(score_surface, (250, 250))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                dead = False 
                enemies = []
                count = 0
    pygame.display.update() #no fps, only DELTA TIME BOYS

pygame.quit()
exit()
