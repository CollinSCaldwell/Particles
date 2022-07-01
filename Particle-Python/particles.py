import pygame
import random
import operator
import numpy as np

pygame.init()


width = 800
height = 800

particles = []
particleCount = 100
particleTypes = 7
particleBases = []


minRadius = 10
maxRadius = 15

minRange = 30
maxRange = 40

repulsionMax = 200
repulsionDivider = 180.0

repulsionStrength = .85

maxSpeed = 1000

minDrag = .05
maxDrag = .1




class particletype :
    particleNum = 0
    numParticles = 0
    attractorMultiplier = []
    growthMultiplier = []
    particleRange = 0.0
    radius = 0.0
    particleColor = (0, 0, 0)
    drag = 0.0

    def __init__ (self, num, particleCount) :
        self.drag = random.randint(int(minDrag * 100), int(maxDrag * 100)) / 100
        self.particleNum = num
        self.numParticles = particleCount
        self.attractorMultiplier = []
        for i in range(0, particleCount) :
            self.attractorMultiplier.insert(i, float(random.randrange(-repulsionMax, repulsionMax, 1)/repulsionDivider))
            if(self.attractorMultiplier[i] == 0) :
                self.attractorMultiplier[i] = repulsionMax/repulsionDivider
        self.growthMultiplier = []
        for i in range(0, particleCount) :
            self.growthMultiplier.insert(i, float(random.randrange(100, 150, 1)/100.0))
            if(self.growthMultiplier[i] == 0) :
                self.growthMultiplier[i] = 5.0
        self.radius = random.randint(minRadius, maxRadius)
        self.particleRange = self.radius + random.randint(minRange, maxRange)
        self.particleColor = (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
        
class particle :
    attractorMultiplier = []
    growthMultiplier = []
    particleRange = 0.0
    radius = 0.0
    particleNum = 0
    particleColor = (0, 0, 0)
    drag = 0.0

    position = (0.0, 0.0)
    velocity = (0.0, 0.0)
    nextVelocity = (0.0, 0.0)
    collisionVelocity = (0.0, 0.0)

    def __init__ (self, particleType) :
        self.drag = particleType.drag
        self.attractorMultiplier = []
        self.attractorMultiplier = particleType.attractorMultiplier
        self.growthMultiplier = []
        self.growthMultiplier = particleType.growthMultiplier
        self.particleRange = particleType.particleRange
        self.radius = particleType.radius
        self.particleNum = particleType.particleNum
        self.particleColor = particleType.particleColor

    def calculateNewVelocity(self, particle) :
        newVelocity = tuple(map(operator.sub, particle.position, self.position))
        newVelocityMagnitude = (newVelocity[0]**2 + newVelocity[1]**2)**.5
        distance = ((particle.position[0] - self.position[0])**2 + (particle.position[1] - self.position[1])**2) ** (1/2) 
        if distance  - particle.radius - self.radius < self.particleRange :
            if distance  - particle.radius - self.radius < 0 :
                newVelocityMagnitude = newVelocityMagnitude + .01
                self.collisionVelocity = (self.collisionVelocity[0] + newVelocity[0]/newVelocityMagnitude * -repulsionStrength * (self.radius + particle.radius - distance) / 2, self.collisionVelocity[1] + newVelocity[1]/newVelocityMagnitude * -repulsionStrength * (self.radius + particle.radius - distance) / 2)
            else :
                b = .5
                if distance - particle.radius - self.radius > b :
                    m = (-1) / (self.particleRange - b)
                    result =   self.attractorMultiplier[particle.particleNum] * (m * (distance - self.radius - particle.radius - self.particleRange))
                    self.nextVelocity = (self.nextVelocity[0] + result * newVelocity[0] / newVelocityMagnitude , self.nextVelocity[1] + result * newVelocity[1] / newVelocityMagnitude)
                else :
                    zeroHeight = .5
                    m = (zeroHeight-1) / (-b)
                    result =  self.attractorMultiplier[particle.particleNum] * (m * (distance - self.radius - particle.radius) + zeroHeight)
                    self.nextVelocity = (self.nextVelocity[0] + result * newVelocity[0] / newVelocityMagnitude, self.nextVelocity[1] + result * newVelocity[1] / newVelocityMagnitude)


    def applyNewVelocity(self) :
        velocityToApply = (self.collisionVelocity[0] + self.nextVelocity[0], self.collisionVelocity[1] + self.nextVelocity[1])


        self.velocity = ((1-self.drag) * (self.velocity[0] + velocityToApply[0]) , (1-self.drag) * (self.velocity[1] + velocityToApply[1]))
        self.velocity = (self.velocity[0] * .95, self.velocity[1] * .95)
        
        magnitude = (self.velocity[0]**2 + self.velocity[1]**2) ** (1/2)
        if magnitude > maxSpeed :
            self.velocity = (self.velocity[0] / magnitude * maxSpeed, self.velocity[1] / magnitude * maxSpeed)
        
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])
        
        
        self.nextVelocity = (0.0, 0.0)
        self.collisionVelocity = (0.0, 0.0)



        # if self.position[0] + self.radius > width :
        #     self.position = (width - self.radius, self.position[1])
        # if self.position[0] - self.radius < 0 :
        #     self.position = (self.radius, self.position[1])
        # if self.position[1] + self.radius > height :
        #     self.position = (self.position[0], height - self.radius)
        # if self.position[1] - self.radius < 0 :
        #     self.position = (self.position[0], self.radius)

        if self.position[0] > width :
            self.position = (self.position[0] - width, self.position[1])
        if self.position[0] < 0 :
            self.position = (self.position[0] + width, self.position[1])
        if self.position[1] > height :
            self.position = (self.position[0], self.position[1] - height)
        if self.position[1] < 0 :
            self.position = (self.position[0], self.position[1] + height)















win = pygame.display.set_mode((width, height))

pygame.display.set_caption("Particles")



for i in range(0, particleTypes) :
    particleBases.insert(i, particletype(i, particleTypes))


for i in range(0, particleCount) :
    particles.insert(i, particle(particleBases[random.randint(0, particleTypes-1)]))
    particles[i].position = (random.randint(0, width), random.randint(0, height))


run = True

while run :
    pygame.time.delay(16)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
    win.fill((0,0,0))
    

    for i in range(0, particleCount) :
        for j in range(0, particleCount) :
            if(j != i) :
                particles[i].calculateNewVelocity(particles[j])

    for i in range(0, particleCount) :
        particles[i].applyNewVelocity()


    
    for i in range(0, particleCount) :
        pygame.draw.circle(win, particles[i].particleColor, particles[i].position, particles[i].radius - 1, particles[i].radius)
    
    pygame.display.update()
    


pygame.quit()






