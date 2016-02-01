from time import sleep
from mcpi.minecraft import Minecraft
from .blocks import get_block_name


def standing_on_block():
    pos = mc.player.getTilePos()
    block_id = mc.getBlock(pos.x, pos.y - 1, pos.z)
    block_name = get_block_name(block_id)
    mc.postToChat("Standing on Block: %s" % (block_name, ))

if __name__ == '__main__':
    mc = Minecraft.create()
    while True:
        standing_on_block(mc)
        sleep(1)
