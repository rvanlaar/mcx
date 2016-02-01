#!/usr/bin/env python2.7

from mcpi.minecraft import Minecraft


def naar_huis(mc):
    hoogte = mc.getHeight(0, 0)
    mc.player.setPos(0, hoogte, 0)


if __name__ == '__main__':
    mc = Minecraft.create()
    naar_huis(mc)
