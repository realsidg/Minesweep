import numpy as np
FUNCTION calculateNeighbours(grid, row, column):
    unrev, flags, revealed <- ({'count':0, 'positions':[]},{'count':0, 'positions':[]},{'count':0, 'positions':[]})
    for i in range(-1,2):
        for j in range(-1,2):
            r= row+i
            c=column+j
            IF (i,j)!=(0,0) AND r in range(0,len(grid)) AND c in range(0, len(grid)):
                IF grid[r][c]==' ':
                    unrev['count']+=1
                    unrev['positions'].append(parsePos(r, c))
                ELSEIF grid[r][c]=='F':
                    flags['count']+=1
                    flags['positions'].append(parsePos(r, c))
                ELSE:
                    revealed['count']+=1
                    revealed['positions'].append(parsePos(r, c))
            ENDIF
                ENDIF
    ENDFOR
        ENDFOR
    RETURN {"unrevealed":unrev, "flags":flags, "rev":revealed}    
ENDFUNCTION

FUNCTION parsePos(row, column):
    r <- str(row+1)
    c= chr(ord('a')+column)
    RETURN c+r
ENDFUNCTION

FUNCTION hint(currgrid, mines):
    grid <- np.array(currgrid)
    min_ratio=1
    mincell=(8,8)
    IF np.array_equal(grid, np.full([len(currgrid),len(currgrid)],' ')):
        RETURN 'a1'
    ELSE:
        for r in range(len(currgrid)):
            for c in range(len(currgrid)):
                IF grid[r][c] not in [' ','0','F']:
                    neighbours= calculateNeighbours(grid, r, c)
                    IF(neighbours['unrevealed']['count']>0) AND (neighbours['unrevealed']['count']+neighbours['flags']['count'] = int(grid[r][c])):
                        RETURN neighbours['unrevealed']['positions'][0]+'f'
                    ELSEIF(neighbours['unrevealed']['count'] > 0) AND  (neighbours['flags']['count'] = int(grid[r][c])):
                        OUTPUT (neighbours['unrevealed']['positions'][0])
                        RETURN neighbours['unrevealed']['positions'][0]
                    ENDIF
                    IF neighbours['unrevealed']['count']!=0:
                        ratio=( int(grid[r][c]) - neighbours['flags']['count'] )/neighbours['unrevealed']['count']
                        IF ratio<min_ratio: 
                            min_ratio <- ratio
                            mincell= (r,c)
    ENDIF
                ENDIF
                    ENDIF
                        ENDIF
        ENDFOR
            ENDFOR
    min_neighbours=calculateNeighbours(grid, mincell[0], mincell[1])
    OUTPUT (min_neighbours['unrevealed']['positions'][0])
    RETURN min_neighbours['unrevealed']['positions'][0]
