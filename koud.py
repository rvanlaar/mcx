#!/usr/bin/env python2.7

from mcpi.minecraft import Minecraft


def is_het_koud(mc):
    pos = mc.player.getTilePos()
    blok_id = mc.getBlock(pos.x, pos.y - 1, pos.z)
    if blok_id in (78, 79, 80):
        mc.postToChat('Brrrr, het is koud.')

if __name__ == '__main__':
    mc = Minecraft.create()
    is_het_koud(mc)
