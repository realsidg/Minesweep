class cell:

    def __init__(self, row , column, value):
        self.row= row
        self.column= column
        self.revealed= False if value==' ' else True
        self.flag= True if value=='F' else False

        if self.flag or not self.revealed:
            self.value=None
        else:
            self.value= int(value)         
    

    def parsePos(self):
        r = str(self.row+1)
        c= chr(ord('a')+self.column)
        return c+r

    def calcNeighbours(self, grid):
        
        unrev, flags, revealed = ([],[],[])
        for i in range(-1,2):
            for j in range(-1,2):

                r= self.row+i
                c= self.column+j

                if (i,j)!=(0,0) and r in range(0,len(grid)) and c in range(0, len(grid)):
                    if grid[r][c].revealed==False:
                        unrev.append(grid[r][c])

                    elif grid[r][c].flag:
                        flags.append(grid[r][c])
                    else:
                        revealed.append(grid[r][c])

        return {"unrevealed":unrev, "flags":flags, "rev":revealed}  


def hint(currgrid, mines):
    min_ratio=1
    mincell=None
    if currgrid == [ [' ' for j in range(len(currgrid))] for i in range(len(currgrid))]:
        return 'a1'
    

    else:
        grid=[[cell(i,j,currgrid[i][j]) for j in range(len(currgrid))] for i in range(len(currgrid))]

        for row in grid:
            for ccell in row:
                if ccell.value != None:

                    neighbours= ccell.calcNeighbours(grid)
                    if(len(neighbours['unrevealed'])>0) and (len(neighbours['unrevealed'])+len(neighbours['flags'])== ccell.value):
                        print (neighbours['unrevealed'][0].parsePos() + 'f')                       
                        return neighbours['unrevealed'][0].parsePos() + 'f'

                    elif(len(neighbours['unrevealed']) > 0) and  (len(neighbours['flags']) == ccell.value):
                        print (neighbours['unrevealed'][0].parsePos())
                        return neighbours['unrevealed'][0].parsePos()

                    if len(neighbours['unrevealed'])!=0:
                        ratio=( ccell.value - len(neighbours['flags']) )/ len(neighbours['unrevealed'])
                        if ratio<min_ratio: 
                            min_ratio = ratio
                            mincell= ccell

    min_neighbours=mincell.calcNeighbours(grid)
    print (min_neighbours['unrevealed'][0].parsePos())
    return min_neighbours['unrevealed'][0].parsePos()
