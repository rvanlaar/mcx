from time import sleep
from mcpi.minecraft import Minecraft
from .blocks import get_block_name


def staan_op_blok():
    pos = mc.player.getTilePos()
    blok_id = mc.getBlock(pos.x, pos.y - 1, pos.z)
    blok_naam = get_block_name(blok_id)
    mc.postToChat("Ik sta op %s" % (blok_naam, ))

if __name__ == '__main__':
    mc = Minecraft.create()
    while True:
        staan_op_blok(mc)
        sleep(1)
