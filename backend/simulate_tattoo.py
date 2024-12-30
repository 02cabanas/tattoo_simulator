import bpy

# Add a cube to the current scene
def add_cube_to_scene():
    print("Adding a cube to the current scene...")
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
    cube = bpy.context.object
    cube.name = "AddedCube"
    print("Cube added to the scene.")

# Run the function
print("Starting the add_cube_to_scene function...")
add_cube_to_scene()
print("Finished the add_cube_to_scene function.")