#!/usr/bin/env python2.7

from time import sleep
from mcpi.minecraft import Minecraft
import blocks as mcx_blocks


def staan_op_blok():
    pos = mc.player.getTilePos()
    blok_id = mc.getBlock(pos.x, pos.y - 1, pos.z)
    blok_naam = mcx_blocks.get_block_name(blok_id)
    mc.postToChat("Ik sta op %s" % (blok_naam, ))

if __name__ == '__main__':
    mc = Minecraft.create()
    i = 0
    while 1 < 60:
        staan_op_blok(mc)
        sleep(2)
