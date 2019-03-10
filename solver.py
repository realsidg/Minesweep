import numpy as np



def calculateNeighbours(grid, row, column):
    unrev, flags, revealed = ({'count':0, 'positions':[]},{'count':0, 'positions':[]},{'count':0, 'positions':[]})
    for i in range(-1,2):
        for j in range(-1,2):
            r= row+i
            c=column+j
            if (i,j)!=(0,0) and r in range(0,len(grid)) and c in range(0, len(grid)):
                if grid[r][c]==' ':
                    unrev['count']+=1
                    unrev['positions'].append(parsePos(r, c))

                elif grid[r][c]=='F':
                    flags['count']+=1
                    flags['positions'].append(parsePos(r, c))

                else:
                    revealed['count']+=1
                    revealed['positions'].append(parsePos(r, c))
    return {"unrevealed":unrev, "flags":flags, "rev":revealed}    



def parsePos(row, column):
    r = str(row+1)
    c= chr(ord('a')+column)
    return c+r

def hint(currgrid, mines):
    grid = np.array(currgrid)
    min_ratio=1
    mincell=(8,8)
    if np.array_equal(grid, np.full([len(currgrid),len(currgrid)],' ')):
        return 'a1'
    
    else:
        for r in range(len(currgrid)):
            for c in range(len(currgrid)):
                if grid[r][c] not in [' ','0','F']:

                    neighbours= calculateNeighbours(grid, r, c)
                    if(neighbours['unrevealed']['count']>0) and (neighbours['unrevealed']['count']+neighbours['flags']['count'] == int(grid[r][c])):
                        return neighbours['unrevealed']['positions'][0]+'f'

                    elif(neighbours['unrevealed']['count'] > 0) and  (neighbours['flags']['count'] == int(grid[r][c])):
                        print (neighbours['unrevealed']['positions'][0])
                        return neighbours['unrevealed']['positions'][0]

                    if neighbours['unrevealed']['count']!=0:
                        ratio=( int(grid[r][c]) - neighbours['flags']['count'] )/neighbours['unrevealed']['count']
                        if ratio<min_ratio: 
                            min_ratio = ratio
                            mincell= (r,c)

    min_neighbours=calculateNeighbours(grid, mincell[0], mincell[1])
    print (min_neighbours['unrevealed']['positions'][0])
    return min_neighbours['unrevealed']['positions'][0]
