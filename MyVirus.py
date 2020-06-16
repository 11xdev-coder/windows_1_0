import time
import pygame
from tkinter import *
from tkinter import messagebox

Tk().wm_withdraw()

pygame.init()

pygame.display.set_icon(pygame.image.load('images.png'))

screen = pygame.display.set_mode((850,150))
pygame.display.set_caption('ВАЖНОЕ СООБЩЕНИЕ!!')
font = pygame.font.SysFont('Lucida Concole',50)
label = font.render('Твоей оперативке КОНЕЦ!!', 1,(12,10,0,1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            pygame.display.set_icon(pygame.image.load('images.png'))
            screen = pygame.display.set_mode((850, 150))
            pygame.display.set_caption('ВАЖНОЕ СООБЩЕНИЕ!!')
            root = Tk()
            cnv = Canvas(root,bg='red')
            cnv.pack()
            cnv.create_text(150,50,text='Все данные удалены!')
            messagebox.showerror('Хахахахахахаха','Хахахахахахахахаххахахахахахахахахахахахахахахахахахаха')

    screen.fill((0,0,0))
    screen.blit(label,(50,50))

    pygame.display.update()

