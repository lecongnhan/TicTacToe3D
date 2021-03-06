from GameState import *
from PlayGround import *
import pygame
from OpenGL.GL import *
import configuration as cfg
import enum
import PlayState
from Controller import HumanController, MinMaxController

class MenuState(BaseState):
    def __init__(self):
        BaseState.__init__(self)
        self.font = None
        self.text = None
        self.buttons = None

        self.playState = None
        self.selfDestroy = False

    def constructor(self):
        BaseState.constructor(self)
        self.screen = pygame.display.set_mode(cfg.displaySize)

        self.constructButtons()

    def constructButtons(self):
        posX = cfg.displaySize[0] / 2
        posY = cfg.displaySize[1] / 2
        pvp = Button(self.screen, "Person VS Person", (posX, posY - 150), 60)
        pvm = Button(self.screen, "Person VS Machine", (posX, posY - 50), 60)
        mvp = Button(self.screen, "Machine VS Person", (posX, posY + 50), 60)
        mvm = Button(self.screen, "Machine VS Machine", (posX, posY + 150), 60)

        pvp.playState = PlayState.PlayState(HumanController(), HumanController())
        pvm.playState = PlayState.PlayState(HumanController(), MinMaxController())
        mvp.playState = PlayState.PlayState(MinMaxController(), HumanController())
        mvm.playState = PlayState.PlayState(MinMaxController(), MinMaxController())

        self.buttons = [pvp, pvm, mvp, mvm]

    def requestPushState(self):
        return self.playState

    def requestPopState(self):
        return self.selfDestroy

    def eventHandling(self, events) -> bool:
        BaseState.eventHandling(self, events)

        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.selfDestroy = True

        for button in self.buttons:
            button.eventHandling(events)

        return False

    def update(self, deltaTime: float) -> bool:
        BaseState.update(self, deltaTime)

        for button in self.buttons:
            button.update(deltaTime)
            if button.isClicked:
                self.playState = button.playState

        if self.playState is not None:
            return False

        return True

    def render(self) -> bool:
        BaseState.render(self)

        self.screen.fill(cfg.backgroundColor)

        for button in self.buttons:
            button.draw()

        pygame.display.update()
        return False

class Button:
    def __init__(self, screen, text, pos, fontSize,
                 color=cfg.mainmenuTextColor,
                 hoveredColor=cfg.mainmenuTextColorHovered,
                 clickedColor=cfg.mainmenuTextColorClicked):
        self.screen = screen
        self.font = pygame.font.SysFont('Corbel', fontSize)
        self.textNormal = self.font.render(text, True, color)
        self.textHovered = self.font.render(text, True, hoveredColor)
        self.textClicked = self.font.render(text, True, clickedColor)
        self.text = self.textNormal
        self.rect = self.text.get_rect()
        self.pos = [pos[0] - self.rect[2] / 2, pos[1] - self.rect[3] / 2]

        self.isClicked = False
        self.isHovered = False

        self.playState = None

    def eventHandling(self, events):
        self.isClicked = False

        for event in events:
            if event.type == pygame.MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self.isHovered = self.pos[0] <= pos[0] <= self.pos[0] + self.rect[2] and self.pos[1] <= pos[1] <= self.pos[1] + self.rect[3]
                if self.isHovered:
                    self.text = self.textHovered
                else:
                    self.text = self.textNormal
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.isHovered:
                    self.text = self.textClicked
            if event.type == pygame.MOUSEBUTTONUP:
                self.isClicked = self.isHovered

    def update(self, deltaTime: float):
        pass

    def draw(self):
        self.screen.blit(self.text, self.pos)