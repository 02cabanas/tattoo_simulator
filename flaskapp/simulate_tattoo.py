import bpy
import os
import sys

# Ensure the "Images as Planes" add-on is enabled
bpy.ops.preferences.addon_enable(module="io_import_images_as_planes")

# Get the command-line arguments
argv = sys.argv
argv = argv[argv.index("--") + 1:]  # Blender-specific handling to get script arguments

input_image_path = argv[0]
output_blend_file_path = argv[1]

# Define the file paths
blend_file_path = os.path.join(os.path.dirname(__file__), 'blend_files', 'model.blend')

def add_image_as_plane(image_path):
    print("Opening Blender file...")
    # Open the Blender file
    bpy.ops.wm.open_mainfile(filepath=blend_file_path)
    
    print("Adding image as plane...")
    # Add image as plane
    bpy.ops.import_image.to_plane(files=[{"name": os.path.basename(image_path)}], directory=os.path.dirname(image_path), relative=False)
    
    plane = bpy.context.object
    plane.name = "TattooPlane"
    
    print("Image added as plane.")
    
    # Save the updated Blender file
    print(f"Saving the updated Blender file to {output_blend_file_path}...")
    bpy.ops.wm.save_as_mainfile(filepath=output_blend_file_path)
    print(f"Blender file saved as '{output_blend_file_path}'")

# Run the function
print("Starting the add_image_as_plane function...")
add_image_as_plane(input_image_path)
print("Finished the add_image_as_plane function.")