import os

IMAGE_SIZE = 150
SCREEN_SIZE = 900
NUM_TILES_SIDE = 6
NUM_TILES_TOTAL = 30
MARGIN = 15

ASSET_DIR = 'images'
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']
assert len(ASSET_FILES) == 15
