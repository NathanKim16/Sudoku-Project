import pygame.font

class Button():
    def __init__(self, screen, msg, color, xPos, yPos, width, height):
        #Initialize button attributes.
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg = msg
        
        #Set the dimensions and properties of the button.
        self.width, self.height = width, height
        self.button_color = color
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)
        
        #Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        # self.rect.center = self.screen_rect.center
        self.rect.centerx = xPos
        self.rect.centery = yPos
        
        #The button essage needs to be prepped only once.
        self.prep_msg(self.msg)
        # self.draw_button()
    
    def prep_msg(self, msg):
        #Turn msg into a rendered image and center text on the button.
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        #Draw a blank button and then draw the message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class boardButton(Button):
    def __init__(self, screen, msg, color, xPos, yPos, width, height, state):
        super().__init__(screen, msg, color, xPos, yPos, width, height)
        self.state = state