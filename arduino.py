# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 15:21:17 2021

@author: joaoi
"""

from pyfirmata import Arduino

# Definindo parâmetros Arduino MEGA
board = Arduino("COM7") # Define a porta do Arduino no PC
pin_cold = board.get_pin('d:3:p') # define a porta de saída do Arduino (digital:3:pwm)
pin_hot = board.get_pin('d:11:p') # define a porta de saída do Arduino (digital:11:pwm)

pin_hot.write(0)
pin_cold.write(0)

board.exit()