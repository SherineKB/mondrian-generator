import bpy
import random

# DELETE MESHES
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False) 

# COLORS
black = (0, 0, 0, 1)
color1 = bpy.data.materials.new("MondrianBlack")
color1.diffuse_color = black

white = (1, 1, 1, 1)
color2 = bpy.data.materials.new("MondrianWhite")
color2.diffuse_color = white

blue = (0, 0, 1, 0)
color3 = bpy.data.materials.new("MondrianBlue")
color3.diffuse_color = blue

red = (1, 0, 0, 1)
color4 = bpy.data.materials.new("MondrianRed")
color4.diffuse_color = red

yellow = (1, 1, 0, 1)
color5 = bpy.data.materials.new("MondrianYellow")
color5.diffuse_color = yellow

# WHITE PLANE
bpy.ops.mesh.primitive_plane_add()
bpy.ops.transform.translate(value=(0, -3, 0))
bpy.ops.transform.resize(value=(16, 22, 14))
monPlane1 = bpy.context.active_object
monPlane1.data.materials.append(color2)

# NUMBER 3
bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-10, -1, 0))
myCube1 = bpy.context.active_object
myCube1.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-6, 1, 0))
bpy.ops.transform.resize(value=(3, 1, 1))
myCube2 = bpy.context.active_object
myCube2.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-2, -1, 0))
bpy.ops.transform.resize(value=(1, 2, 1))
myCube3 = bpy.context.active_object
myCube3.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-5, -4, 0))
bpy.ops.transform.resize(value=(3, 1, 1))
myCube4 = bpy.context.active_object
myCube4.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-6, 1, 0))
bpy.ops.transform.resize(value=(3, 1, 1))
myCube5 = bpy.context.active_object
myCube5.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-2, -7, 0))
bpy.ops.transform.resize(value=(1, 2, 1))
myCube6 = bpy.context.active_object
myCube6.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-6, -9, 0))
bpy.ops.transform.resize(value=(3, 1, 1))
myCube7 = bpy.context.active_object
myCube7.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-10, -7, 0))
myCube8 = bpy.context.active_object
myCube8.data.materials.append(color1)

# LETTER D
bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(3, -4, 0))
bpy.ops.transform.resize(value=(1, 6, 1))
myCube8 = bpy.context.active_object
myCube8.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(7, 1, 0))
bpy.ops.transform.resize(value=(3, 1, 1))
myCube9 = bpy.context.active_object
myCube9.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(10, -4, 0))
bpy.ops.transform.resize(value=(1, 4, 1))
myCube10 = bpy.context.active_object
myCube10.data.materials.append(color1)

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(7, -9, 0))
bpy.ops.transform.resize(value=(3, 1, 1))
myCube11 = bpy.context.active_object
myCube11.data.materials.append(color1)

# COLOR LIST

colorList = [color3, color4, color5]

# COLORED CUBES

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-10, 12.5, 0))
bpy.ops.transform.resize(value=(1.8, 4, 1))
myCubeColored1 = bpy.context.active_object
myCubeColored1.data.materials.append(random.choice(colorList))

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-5, 8.5, 0))
bpy.ops.transform.resize(value=(5, 1, 1))
myCubeColored2 = bpy.context.active_object
myCubeColored2.data.materials.append(random.choice(colorList))

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(6, 5, 0))
bpy.ops.transform.resize(value=(2, 2, 2))
myCubeColored3 = bpy.context.active_object
myCubeColored3.data.materials.append(random.choice(colorList))

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(12, 13, 0))
bpy.ops.transform.resize(value=(1.8, 4, 1))
myCubeColored4 = bpy.context.active_object
myCubeColored4.data.materials.append(random.choice(colorList))

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-12, -15, 0))
bpy.ops.transform.resize(value=(2, 2, 2))
myCubeColored5 = bpy.context.active_object
myCubeColored5.data.materials.append(random.choice(colorList))

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(-3.5, -17, 0))
bpy.ops.transform.resize(value=(1.8, 4, 1))
myCubeColored6 = bpy.context.active_object
myCubeColored6.data.materials.append(random.choice(colorList))

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(3.5, -23, 0))
bpy.ops.transform.resize(value=(5, 1, 1))
myCubeColored7 = bpy.context.active_object
myCubeColored7.data.materials.append(random.choice(colorList))

bpy.ops.mesh.primitive_cube_add()
bpy.ops.transform.translate(value=(8, -19, 0))
bpy.ops.transform.resize(value=(2, 2, 1))
myCubeColored8 = bpy.context.active_object
myCubeColored8.data.materials.append(random.choice(colorList))
