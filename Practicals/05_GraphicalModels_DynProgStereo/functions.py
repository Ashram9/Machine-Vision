import numpy as np
# the goal of this routine is to return the minimum cost dynamic programming solution 
# given a set of unary and pairwise costs
def dynamicProgram(unaryCosts, pairwiseCosts):

    # count number of positions (i.e. pixels in the scanline), and nodes at each
    # position (i.e. the number of distinct possible disparities at each position)
    nNodesPerPosition = len(unaryCosts)
    nPosition = len(unaryCosts[0])

    # define minimum cost matrix - each element will eventually contain
    # the minimum cost to reach this node from the left hand side.
    # We will update it as we move from left to right
    minimumCost = np.zeros([nNodesPerPosition, nPosition])

    # define parent matrix - each element will contain the (vertical) index of
    # the node that preceded it on the path.  Since the first column has no
    # parents, we will leave it set to zeros.
    parents = np.zeros([nNodesPerPosition, nPosition])

    # FORWARD PASS

    # TODO:  fill in first column of minimum cost matrix
    minimumCost[:, 0] = unaryCosts[:, 0]

    # Now run through each position (column)
    for cPosition in range(1,nPosition):
        # run through each node (element of column)
        for cNode in range(nNodesPerPosition):
            # now we find the costs of all paths from the previous column to this node
            possPathCosts = np.zeros([nNodesPerPosition,1])
            for cPrevNode in range(nNodesPerPosition):
                # TODO  - fill in elements of possPathCosts
                possPathCosts[cPrevNode,0] = minimumCost[cPrevNode, cPosition-1] + pairwiseCosts[cPrevNode, cNode] + unaryCosts[cNode, cPosition]

            # TODO - find the minimum of the possible paths 
            minCost = np.min(possPathCosts)
            ind = np.argmin(possPathCosts)
            
            # Assertion to check that there is only one minimum cost.
            # assert(len(np.where(possPathCosts == minCost)[0]) == 1)

            # TODO - store the minimum cost in the minimumCost matrix
            minimumCost[cNode, cPosition] = minCost
            
            # TODO - store the parent index in the parents matrix
            parents[cNode, cPosition] = ind

    #BACKWARD PASS
    #we will now fill in the bestPath vector
    bestPath = np.zeros([nPosition,1])
    
    #TODO  - find the index of the overall minimum cost from the last column and put this
    #into the last entry of best path
    minCost = np.min(minimumCost[:, nPosition-1])
    minInd = np.argmin(minimumCost[:, nPosition-1]) 
    bestPath[-1] = minInd

    # TODO - find the parent of the node you just found
    bestParent = parents[minInd, nPosition-1]

    # run backwards through the cost matrix tracing the best patch
    for cPosition in range(nPosition-2,-1,-1):
        # TODO - work through matrix backwards, updating bestPath by tracing parents
        bestPath[cPosition] = bestParent
        bestParent = parents[int(bestParent), cPosition] 

    # TODO: REMOVE THIS WHEN YOU ARE DONE
    # bestPath = np.floor(np.random.random(nPosition)*nNodesPerPosition)
    return bestPath


def dynamicProgramVec(unaryCosts, pairwiseCosts):
    
    # same preprocessing code
    
    # count number of positions (i.e. pixels in the scanline), and nodes at each
    # position (i.e. the number of distinct possible disparities at each position)
    nNodesPerPosition = len(unaryCosts)
    nPosition = len(unaryCosts[0])

    # define minimum cost matrix - each element will eventually contain
    # the minimum cost to reach this node from the left hand side.
    # We will update it as we move from left to right
    minimumCost = np.zeros([nNodesPerPosition, nPosition])

    # TODO: fill this function in. (hint use tiling and perform calculations columnwise with matricies)

    # define parent matrix - each element will contain the (vertical) index of
    # the node that preceded it on the path.  Since the first column has no
    # parents, we will leave it set to zeros.
    parents = np.zeros([nNodesPerPosition, nPosition])

    # forward pass
    minimumCost[:, 0] = unaryCosts[:, 0]

    for cPosition in range(1, nPosition):
        # calculate possible path costs using vectorized operations
        possPathCosts = minimumCost[:, cPosition-1, np.newaxis] + pairwiseCosts + unaryCosts[:, cPosition, np.newaxis].T
        
        # find the minimum of the possible paths
        minimumCost[:, cPosition] = np.min(possPathCosts, axis=0)

        # update parents matrix with the index of the minimum path
        parents[:, cPosition] = np.argmin(possPathCosts, axis=0)

    # backward pass
    bestPath = np.zeros([nPosition,1])
    
    # find the index of the overall minimum cost from the last column

    #into the last entry of best path
    minCost = np.min(minimumCost[:, nPosition-1])
    minInd = np.argmin(minimumCost[:, nPosition-1]) 
    bestPath[-1] = minInd

    # find the parent of the node you just found
    bestParent = parents[minInd, nPosition-1]

    # run backwards through the cost matrix tracing the best patch
    for cPosition in range(nPosition-2,-1,-1):
        # work through matrix backwards, updating bestPath by tracing parents
        bestPath[cPosition] = bestParent
        bestParent = parents[int(bestParent), cPosition] 


    # TODO: REMOVE THIS WHEN YOU ARE DONE
    # bestPath = np.floor(np.random.random(nPosition)*nNodesPerPosition)

    return bestPath