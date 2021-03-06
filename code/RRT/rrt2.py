from collections import deque
from queue import PriorityQueue
import heapq
import numpy as np
import math
import random as rd
import pygame
import time


class Node:
    def __init__(self, state=None, parent=None):
        self.state = state
        self.parent = parent


######################################
#          Workspace
######################################
def isValidWorkspace(pt, r, radiusClearance):
    x, y = pt

    # ------------------------------------------------------------------------------
    #                              Circle 1 pts
    # ------------------------------------------------------------------------------
    ptInCircle1 = (x - 5.5 / r) ** 2 + (y - 5.5 / r) ** 2 - (
                (3.2 + radiusClearance) / r) ** 2 <= 0

    # --------------------------------------------------------------------------------
    #                             square 1 pts
    # --------------------------------------------------------------------------------
    X = np.float32([0.5, 2.5, 2.5, 0.5]) / r
    Y = np.float32([4.5, 4.5, 6.5, 6.5]) / r
    ptInSquare1 = Y[0] - radiusClearance / r <= y <= Y[2] + radiusClearance / r and \
                  0 >= (Y[2] - Y[1]) * (x - X[1]) - radiusClearance / r and \
                  0 >= (Y[0] - Y[3]) * (x - X[3]) - radiusClearance / r

    # --------------------------------------------------------------------------------
    #                             Square 2 pts
    # --------------------------------------------------------------------------------
    X = np.float32([8.5, 10.5, 10.5, 8.5]) / r
    Y = np.float32([4.5, 4.5, 6.5, 6.5]) / r
    ptInSquare2 = Y[0] - radiusClearance / r <= y <= Y[2] + radiusClearance / r and \
                  0 >= (Y[2] - Y[1]) * (x - X[1]) - radiusClearance / r and \
                  0 >= (Y[0] - Y[3]) * (x - X[3]) - radiusClearance / r

    # --------------------------------------------------------------------------------
    #                             Square 3 pts
    # --------------------------------------------------------------------------------
    X = np.float32([4.5, 6.5, 6.5, 4.5]) / r
    Y = np.float32([0.5, 0.5, 2.5, 2.5]) / r
    ptInSquare3 = Y[0] - radiusClearance / r <= y <= Y[2] + radiusClearance / r and \
                  0 >= (Y[2] - Y[1]) * (x - X[1]) - radiusClearance / r and \
                  0 >= (Y[0] - Y[3]) * (x - X[3]) - radiusClearance / r

    # --------------------------------------------------------------------------------
    #                             Square 4 pts
    # --------------------------------------------------------------------------------
    X = np.float32([4.5, 6.5, 6.5, 4.5]) / r
    Y = np.float32([8.5, 8.5, 10.5, 10.5]) / r
    ptInSquare4 = Y[0] - radiusClearance / r <= y <= Y[2] + radiusClearance / r and \
                  0 >= (Y[2] - Y[1]) * (x - X[1]) - radiusClearance / r and \
                  0 >= (Y[0] - Y[3]) * (x - X[3]) - radiusClearance / r

    if ptInCircle1 or ptInSquare1 or ptInSquare2 or ptInSquare3 or ptInSquare4:
        return False
    return True


# checks whether next action is near an obstacle or ill defined
def isSafe(newState, r, radiusClearance):
    col = float(11 / r)
    row = float(11 / r)

    if newState[0] < 0.0 or newState[0] > col or newState[1] < 0.0 or newState[1] > row:
        return False
    return isValidWorkspace(newState, r, radiusClearance)


def steer(xNearest, xRand):
    stepsize = 0.5
    dist = distance(xNearest, xRand)
    if (dist < stepsize):
        return xRand
    else:
        t = stepsize / dist
        v = xRand - xNearest
        r = t * v + xNearest
        return r


def isObstacleFree(pt1, pt2, radiusClearance):
    stepsize = 0.1
    t = np.arange(stepsize, 1.0 + stepsize, stepsize)
    v = pt2 - pt1
    for i in range(len(t)):
        r = t[i] * v + pt1
        if not isSafe(r, 1, radiusClearance):
            return False
    return True


def printPath(node):
    solution = []
    current = node
    while current:
        solution.append(current.state)
        current = current.parent
    return solution


def samplePoint():
    x = rd.uniform(0.0, 11.0)
    y = rd.uniform(0.0, 11.0)
    return [x, y]


def distance(startPosition, goalPosition):
    sx, sy = startPosition
    gx, gy = goalPosition
    return math.sqrt((gx - sx) ** 2 + (gy - sy) ** 2)


def nearest(nodesExplored, newState):
    minDist = np.inf
    for key, node in nodesExplored.items():
        dist = distance(node.state, newState)
        if dist < minDist:
            minDist = dist
            minKey = key
    return minKey, minDist


def generatePath(q, startEndCoor, nodesExplored, radiusClearance, numIterations=3000):
    # get start and goal locations
    sx, sy = startEndCoor[0]
    gx, gy = startEndCoor[1]

    # Initializing root node
    key = str(sx) + str(sy)
    root = Node(np.float32([sx, sy]), None)
    nodesExplored[key] = root

    for i in range(numIterations):
        # sample random point
        newPosX, newPosY = samplePoint()
        xRand = np.array([newPosX, newPosY])

        # Get Nearest Node
        xNearestKey, _ = nearest(nodesExplored, xRand)
        xNearest = nodesExplored[xNearestKey].state

        # steer in direction of path
        xNew = steer(xNearest, xRand)

        # check if edge is not in obstacle
        if (xNew == xNearest).all() or not isObstacleFree(xNearest, xNew, radiusClearance):
            continue

        # add node to nodesExplored(add vertex and edge)
        newNode = Node(xNew, nodesExplored[xNearestKey])
        s = str(newNode.state[0]) + str(newNode.state[1])
        nodesExplored[s] = newNode

        # print path if goal is reached
        if distance(newNode.state, [gx, gy]) <= 0.3:
            sol = printPath(newNode)
            return [True, sol]

    return [False, None]


def triangleCoordinates(start, end, triangleSize=5):
    rotation = (math.atan2(start[1] - end[1], end[0] - start[0])) + math.pi / 2
    # print(math.atan2(start[1] - end[1], end[0] - start[0]))
    rad = math.pi / 180

    coordinateList = np.array([[end[0], end[1]],
                               [end[0] + triangleSize * math.sin(rotation - 165 * rad),
                                end[1] + triangleSize * math.cos(rotation - 165 * rad)],
                               [end[0] + triangleSize * math.sin(rotation + 165 * rad),
                                end[1] + triangleSize * math.cos(rotation + 165 * rad)]])

    return coordinateList


# if __name__ == '__main__':
# newState = np.array([3,9])
# print(isSafe(newState,1,0.3))

if __name__ == "__main__":

    # iul = 20
    # iur = 20
    is1 = -4  # -4  #-4
    is2 = -4  # -4  #-3
    ig1 = 4  # 4   #0
    ig2 = 4  # 2.5  #-3
    # istartOrientation = 0
    # idt = -1#0.6 #0.8
    # ismoothCoef = -1# 0.2 #0.1

    # ---------------------------------
    # Inputs From World Coordinates
    # To Pygame Coordinates
    # ---------------------------------
    # startOrientation = 360 - istartOrientation
    # ul = iul
    # ur = iur
    s1 = 5.5 + (is1)
    s2 = 5.5 - (is2)
    g1 = 5.5 + (ig1)
    g2 = 5.5 - (ig2)
    # dt = idt if (idt >= 0.0) else 0.3
    # smoothCoef = ismoothCoef if (ismoothCoef >= 0) else 0.5

    # ---------------------------
    #  Precision Parameters
    # ---------------------------
    threshDistance = 0.5
    clearance = 0.1
    # threshAngle = 5

    # ---------------------------
    #  Robot parameters
    # ---------------------------
    # smoothCoef = ismoothCoef if (ismoothCoef>= 0) else 0.5
    # wheelDist = 0.2116  # 0.3175/6 * 4
    # wheelRadius = 0.038
    # robotParams = [ul, ur, wheelRadius, wheelDist, smoothCoef]
    robotRadius = 0  # 0.177

    # -------------------------------
    #  Parameters needed by gazebo
    # -------------------------------
    # dt - affects publishing rate
    #   - dt must be of resolution 0.1
    #   - restricting frequency to 10Hz in gazebo
    #   - 1/frequency*dt must be a whole number

    # is1,is2,iorientation- initial pose for robot
    # writeParametersForGazebo(dt, is1, is2, istartOrientation)

    # ----------------------------
    #  Display parameters
    # ----------------------------
    pygame.init()

    res = 1.0  # resolution of grid
    scale = 80  # scale of grid

    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    yellow = (255, 255, 0)

    size_x = 11
    size_y = 11
    gameDisplay = pygame.display.set_mode((size_x * scale, size_y * scale))

    # ----------------------------
    # Start and goal coordinates
    # ----------------------------
    startCoor = np.float32((np.float32([s1, s2])) / res)
    goalCoor = np.float32((np.float32([g1, g2])) / res)

    startEndCoor = [startCoor, goalCoor]

    ############################################################
    #                 Display Obstacles
    ############################################################
    circlePts1 = [5.5, 5.5, 3]

    pygame.draw.circle(gameDisplay, red, (int(circlePts1[0] * scale), int(circlePts1[1] * scale)),
                       int(circlePts1[2] * scale))
    pygame.draw.rect(gameDisplay, red, [int(scale * 0.5), int(scale * 4.5), int(scale * 2), int(scale * 2)])
    pygame.draw.rect(gameDisplay, red, [int(scale * 8.5), int(scale * 4.5), int(scale * 2), int(scale * 2)])
    pygame.draw.rect(gameDisplay, red, [int(scale * 4.5), int(scale * 0.5), int(scale * 2), int(scale * 2)])
    pygame.draw.rect(gameDisplay, red, [int(scale * 4.5), int(scale * 8.5), int(scale * 2), int(scale * 2)])

    ############################################################
    #          Draw Explored Nodes and solution path
    ############################################################
    nodesExplored = {}
    q = []

    if not isSafe(startCoor, res, clearance + robotRadius) or not isSafe(goalCoor, res, clearance + robotRadius):
        pygame.draw.rect(gameDisplay, blue, (startCoor[0] * res * scale, startCoor[1] * res * scale,
                                             res * 2, res * 2))

        pygame.draw.circle(gameDisplay, blue, (int(goalCoor[0] * res * scale), int(goalCoor[1] * res * scale)),
                           math.floor(0.3 * res * scale))

        pygame.draw.rect(gameDisplay, white, (goalCoor[0] * res * scale, goalCoor[1] * res * scale,
                                              res * 2, res * 2))
        basicfont = pygame.font.SysFont(None, 48)
        text = basicfont.render('Start or goal position must be in a valid workspace', True, (255, 0, 0),
                                (255, 255, 255))
        textrect = text.get_rect()
        textrect.centerx = gameDisplay.get_rect().centerx
        textrect.centery = gameDisplay.get_rect().centery

        gameDisplay.blit(text, textrect)
        pygame.display.update()
        pygame.time.delay(2000)

    else:
        startTime = time.time()  # Start time of simulation
        print('Exploring nodes...')
        success, solution = generatePath(q, startEndCoor, nodesExplored, clearance + robotRadius)
        endTime = time.time()

        #############################################
        #      Drawing
        #############################################
        if success:
            print('Optimal path found')
            print("Total time taken for exploring nodes " + str(endTime - startTime) + " seconds.")
            # writeSolutionToFile(solution)

            draw = True
            while draw:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

                # draw nodesExplored
                for s in nodesExplored:
                    if nodesExplored[s].parent:
                        pt = nodesExplored[s].state[0:2]
                        ptParent = nodesExplored[s].parent.state[0:2]
                        x, y = pt * scale * res
                        x2, y2 = ptParent * scale * res

                        # draw explored nodes
                        pygame.draw.line(gameDisplay, white, (x2, y2), (x, y), 1)
                        # pygame.draw.circle(gameDisplay,green,(int(x),int(y)),4)
                        triangle = triangleCoordinates([x2, y2], [x, y], 5)
                        pygame.draw.polygon(gameDisplay, green,
                                            [tuple(triangle[0]), tuple(triangle[1]), tuple(triangle[2])])

                    # draw start and goal locations
                    pygame.draw.rect(gameDisplay, blue, (startCoor[0] * res * scale, startCoor[1] * res * scale,
                                                         res * 2, res * 2))

                    pygame.draw.circle(gameDisplay, blue,
                                       (int(goalCoor[0] * res * scale), int(goalCoor[1] * res * scale)),
                                       math.floor(0.3 * res * scale))

                    pygame.draw.rect(gameDisplay, white, (goalCoor[0] * res * scale, goalCoor[1] * res * scale, \
                                                          res * 2, res * 2))
                    pygame.display.update()

                # draw solution path
                for i in range(len(solution) - 2, -1, -1):
                    pt = solution[i][0:2]
                    pt1 = solution[i + 1][0:2]
                    xt, yt = pt[0] * scale * res, pt[1] * scale * res
                    x, y = pt1[0] * scale * res, pt1[1] * scale * res
                    pygame.draw.line(gameDisplay, yellow, (xt, yt), (x, y), 3)
                    pygame.draw.circle(gameDisplay, red, (int(x), int(y)), 4)
                    pygame.display.update()
                pygame.time.delay(4000)
                draw = False

        else:
            print('Path not possible')
            basicfont = pygame.font.SysFont(None, 48)
            text = basicfont.render('Path can\'t be generated', True, (255, 0, 0), (255, 255, 255))
            textrect = text.get_rect()
            textrect.centerx = gameDisplay.get_rect().centerx
            textrect.centery = gameDisplay.get_rect().centery

            gameDisplay.blit(text, textrect)
            pygame.display.update()
            pygame.time.delay(200000)
    pygame.quit()
