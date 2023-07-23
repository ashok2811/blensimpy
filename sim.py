import bpy

def create_pitch():
    # Clear existing mesh objects
    bpy.ops.object.select_all(action='DESELECT')
    bpy.ops.object.select_by_type(type='MESH')
    bpy.ops.object.delete()

    # Pitch dimensions
    pitch_length = 22
    pitch_width = 10

    # Create the pitch plane
    bpy.ops.mesh.primitive_plane_add(size=pitch_length, enter_editmode=False, location=(0, 0, 0))
    pitch_plane = bpy.context.active_object
    pitch_plane.name = "Pitch"
    #pitch_plane.rotation_euler[0] = 1.5708  # Rotate 90 degrees on X-axis
    pitch_plane.scale[1] = pitch_width / pitch_length

    # Create stumps
    stump_radius = 0.1
    stump_height = 0.71

    for x in [-1, 1]:
        bpy.ops.mesh.primitive_cylinder_add(radius=stump_radius, depth=stump_height, location=(x * 0.5, 0, stump_height / 2))
        stump = bpy.context.active_object
        stump.name = "Stump_" + str(x)

    # Set the camera
    bpy.ops.object.camera_add(location=(0, -8, 4), rotation=(1.2, 0, 0))
    camera = bpy.context.active_object
    camera.name = "Camera"
    bpy.context.scene.camera = camera

    # Set the light
    bpy.ops.object.light_add(type='SUN', location=(8, -8, 10))
    light = bpy.context.active_object
    light.name = "Light"

def create_ball():
    # Create the ball
    bpy.ops.mesh.primitive_uv_sphere_add(radius=0.1, location=(-10, 0, 0))
    ball = bpy.context.active_object
    ball.name = "Ball"

    # Set initial velocity (in Blender units per frame)
    velocity_x = 0.1
    velocity_y = 0.0

    # Set animation for the ball
    frames = 250  # Number of frames the ball will move
    gravity = -0.003  # Acceleration due to gravity
    for i in range(frames):
        ball.location.x += velocity_x
        velocity_y += gravity  # Apply gravity to the vertical velocity
        ball.location.z += velocity_y
        ball.keyframe_insert(data_path='location', frame=i + 2)

if __name__ == "__main__":
    create_pitch()
    create_ball()
