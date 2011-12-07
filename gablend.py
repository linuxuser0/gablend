import bpy
import random

def create_random_object(name, dist, accuracy):
    bpy.ops.mesh.primitive_uv_sphere_add()
    random_object = bpy.context.active_object
    randomize_object(random_object, dist, accuracy)
    random_object.name = name
    return random_object

def randomize_object(shape, dist, accuracy):
    for vert in shape.data.vertices:
        randomize_vertex(vert, dist, accuracy)
    
def randomize_vertex(vert, dist, accuracy):
    vert.co.x += random.randrange(-dist, dist, accuracy)
    vert.co.y += random.randrange(-dist, dist, accuracy)
    vert.co.z += random.randrange(-dist, dist, accuracy)
    

def mutate(obj, dist, accuracy):
    verts = count_vertices(obj)
    for vert in obj.data.vertices:
        chance = random.randint(1, verts)
        if chance == verts:
            randomize_vertex(vert, dist, accuracy)
            
