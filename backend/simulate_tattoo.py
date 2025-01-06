import bpy
import os

def add_cube_to_scene():
    """Add a cube to the currently active scene."""
    print("Adding a cube to the current scene...")
    bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 0))
    cube = bpy.context.object
    cube.name = "AddedCube"
    print("Cube added to the scene.")

def main():
    # Define the path to the .blend file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    blend_file_path = os.path.join(current_dir, "../extra/blend_copy/model.blend")

    # Open the specified .blend file
    print(f"Opening .blend file: {blend_file_path}")
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)

    # Add the cube
    add_cube_to_scene()

    # Save the updated .blend file
    print(f"Saving changes to: {blend_file_path}")
    bpy.ops.wm.save_mainfile()

# Run the main function
if __name__ == "__main__":
    main()