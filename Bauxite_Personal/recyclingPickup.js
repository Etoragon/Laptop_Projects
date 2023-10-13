const pygame = require('pygame')
const os = require('os')
const time = require('time')
const random = require('random')
const mixer = require('pygame')

pygame.init()
pygame.font.init()

// Display window with set width and height
let s_width = 1000
let s_height = 700
let screen = pygame.display.set_mode([s_width, s_height])

pygame.display.set_caption('Stop The Asteroids!')

// Road Object images
let grandma = pygame.transform.scale(pygame.image.load('walkerPix.png').convert_alpha(), [75, 75])
let cardboard_box = pygame.transform.scale(pygame.image.load('cardBBoxPixel.png').convert_alpha(), [75, 75])
let dog = pygame.transform.scale(pygame.image.load('dogPix.png').convert_alpha(), [75, 75])
let bottle = pygame.transform.scale(pygame.image.load('pixelBottle.png').convert_alpha(), [75, 75])

// User Character
let trash_truck = pygame.transform.scale(pygame.image.load('TrashTruckPix.png'), [180, 180]).convert_alpha()

// Background
let backg_img = pygame.transform.scale(pygame.image.load('backgroundTest.png'), [s_width, s_height])

class RoadObject {
constructor(x, y, img) {
this.x = x
this.y = y
this.img = img
this.mask = pygame.mask.from_surface(this.img)
}

draw(window) {
window.blit(this.img, [this.x, this.y])
}

move(vel) {
this.x -= vel
}

off_screen(width) {
return !(this.x <= width && this.x >= 0)
}

collision(obj) {
return collide(obj, this)
}

get_height() {
return this.img.get_height()
}
}

class Truck {
constructor(x, y, health = 100) {
this.x = x
this.y = y
this.health = health
this.tuck_img = trash_truck
}

draw(window) {
window.blit(this.tuck_img, [this.x, this.y])
}

get_width() {
return this.tuck_img.get_width()
}

get_height() {
return this.tuck_img.get_height()
}
}

class Player extends Truck {
constructor(x, y, health = 100) {
super(x, y, health)
this.truck_img = trash_truck
this.mask = pygame.mask.from_surface(this.truck_img)
this.max_health = health
}

draw(screen) {
super.draw(screen)
this.healthbar(screen)
}

healthbar(screen) {
pygame.draw.rect(screen, [255, 0, 0], [this.x, this.y + this.truck_img.get_height() + 10, this.truck_img.get_width(), 10])
pygame.draw.rect(screen, [0, 255, 0], [this.x, this.y + this.truck_img.get_height() + 10, this.truck_img.get_width() * (this.health / this.max_health), 10])
}
}

// Sound
// mixer.music.load('Arcane_Battle.ogg.mp3')
// mixer.music.play(-1)

function collide(obj1, obj2) {
let offset_x = obj2.x - obj1.x
let offset_y = obj2.y - obj1.y
return obj1.mask.overlap(obj2.mask, [offset_x, offset_y]) !== null
}

function main() {
// game loop
let running = true
}