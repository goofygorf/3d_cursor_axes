# 3d_cursor_axes.py - David Spencer - 6/5/22
# Creates a supplementary 3d axes to enhance the Blender 3d Cursor.
# Uses an Empty object connected to the 3d Cursor with Drivers.
 
# Usage == import or copy/paste the script into the Script Editor, and Run Script
# Empty Axes can be changed to a different object or size in the Object Data Properties
# or Right Click in the 3d Viewport to interactively change size.
# Change the Empty Axes color in  Preferences - Themes - 3d Viewport - Empty.
# Change the 3d Cursor color in Preferences - Themes - 3d Viewport - View Overlay
# Always maintain matching Rotation Orders between the Empty and the 3d Cursor

import bpy
  # set default name and rotation order
cursor_name = "3D Cursor Axes"
default_rot_mode = "ZXY"
scene = bpy.context.scene.name_full
  # create a new Empty Axis type
crsr = bpy.data.objects.new(name=cursor_name, object_data=None)
crsr.empty_display_type ='ARROWS'
crsr.rotation_mode = default_rot_mode
  # add the empty to the current active view layer
view_layer = bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(crsr)

  # change the Scene cursor to default rotation order
bpy.context.scene.cursor.rotation_mode = default_rot_mode

# ------ Axes Driver Setup -------
def create_drivers(transform):
    index = 0
    while index < 3:
        driver = bpy.data.objects[cursor_name].driver_add(transform, index).driver
        driver.type = 'AVERAGE'
        var = driver.variables.new() 
        var.type = 'SINGLE_PROP'
        var.targets[0].id_type = 'SCENE'
        var.targets[0].id = bpy.data.scenes[scene]
        var.targets[0].data_path = "cursor."+transform+"["+str(index)+"]"
        index +=1
        
create_drivers('location')
create_drivers('rotation_euler')