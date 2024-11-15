import pygame.font

class Button():
    def __init__(self, screen, msg, color, xPos, yPos, width, height, curve):
        #Initialize button attributes.
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.msg = msg
        
        #Set the dimensions and properties of the button.
        self.width, self.height = width, height
        self.button_color = color
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)
        self.curve = curve
        
        #Build the button's rect object and center it.
        self.xPos = (xPos-(width/2))#Translates given center pos to top left corner
        self.yPos = (yPos-(height/2))#Translates given center pos to top left corner
        self.rect = pygame.Rect(self.xPos, self.yPos, self.width+0.5, self.height+0.5)#Accounts for any rounding errors
        
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
        pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=self.curve)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class boardButton(Button):
    def __init__(self, screen, msg, color, xPos, yPos, width, height, state, curve):
        super().__init__(screen, msg, color, xPos, yPos, width, height, curve)
        self.state = state
        self.curve = 0
    def prep_msg(self, msg):
        #Turn msg into a rendered image and center text on the button.
        self.font = pygame.font.SysFont(None, 65)#Larger font for the board
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    # def draw_button(self):
    #     #Draw a blank button and then draw the message.
    #     pygame.draw.rect(self.screen, self.button_color, self.rect, border_radius=curve)
    #     self.screen.blit(self.msg_image, self.msg_image_rect)