class TempRoom:
    roomName = "none"
    depth = 0
    xloc = 0
    yloc = 0
    connectedRooms = []

    def __init__(self, roomName, depth, xloc, yloc):
        self.roomName = roomName
        self.depth = depth
        self.xloc = xloc
        self.yloc = yloc