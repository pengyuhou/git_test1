import pygame
from .. import tools,set_up
from  .. import  constants as C
import json
import  os


class Player(pygame.sprite.Sprite):
    def __init__(self,name):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.load_data()
        self.setup_states()
        self.setup_velocities()
        self.setup_timers()
        self.load_images()

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()


    def load_data(self):
        file_name = self.name+'.json'
        file_path = os.path.join('source/data/player',file_name)
        with open(file_path) as f:
            self.player_data = json.load(f)

    def setup_states(self):
        self.face_right = True
        self.dead = False
        self.big = False

    def setup_velocities(self):
        self.x_vel = 0
        self.y_vel = 0

    def setup_timers(self):
        self.walking_timer = 0
        self.transition_timer = 0

    def load_images(self):
        sheet = set_up.GRAPHICS['mario_bros']
        frame_rects = self.player_data['image_frames']

        self.right_frames = []
        self.left_frames = []
        self.up_frames = []
        self.down_frames = []

        frame_rects = [
            (178,32,12,16),
            (80,32,15,16),
            (96,32,16,16),
            (112,32,16,16)
        ]

        for frame_rect in frame_rects:
            right_image = tools.get_img(sheet,*frame_rect,(0,0,0),C.PLAYER_MULTI)
            left_image = pygame.transform.flip(right_image,True,False)
            up_image = pygame.transform.rotate(right_image,90)
            down_image = pygame.transform.rotate(right_image, -90)
            self.right_frames.append(right_image)
            self.left_frames.append(left_image)
            self.up_frames.append(up_image)
            self.down_frames.append(down_image)

        self.frame_index = 0
        self.frames = self.right_frames
        self.image = self.frames[self.frame_index]
        self.rect =self.image.get_rect()

    def update(self,keys):

        self.current_time = pygame.time.get_ticks()
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
            self.y_vel = 0
            self.frames = self.right_frames
        if keys[pygame.K_LEFT]:
            self.x_vel = -5
            self.y_vel = 0
            self.frames = self.left_frames
        if keys[pygame.K_UP]:
            self.x_vel = 0
            self.y_vel = -5
            self.frames = self.up_frames
        if keys[pygame.K_DOWN]:
            self.x_vel = 0
            self.y_vel = 5
            self.frames = self.down_frames

        if self.current_time - self.walking_timer>100:
            self.walking_timer = self.current_time
            self.frame_index += 1
            self.frame_index %= 4
        self.image = self.frames[self.frame_index]
















    def update(self,keys):
        if keys[pygame.K_RIGHT]:
            self.x_vel = 5
        elif keys[pygame.K_LEFT]:
            self.x_vel = -5
