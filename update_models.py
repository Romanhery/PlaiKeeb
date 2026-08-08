import pcbnew

# Update this path to whatever .STEP or .WRL file you want to apply to ALL footprints
MODEL_PATH = "/Users/romans/PlaiKeyboard/cherry-mx-red-switch-1.snapshot.3 (1)/Cherry MX.STEP"

board = pcbnew.GetBoard()
updated_count = 0

for footprint in board.GetFootprints():
    # Clear any existing 3D models from the footprint
    footprint.Models().clear()
    
    # Create the new 3D model object
    model = pcbnew.FP_3DMODEL()
    model.m_Filename = MODEL_PATH
    
    # Set your scale, rotation, and offsets here
    model.m_Scale.x, model.m_Scale.y, model.m_Scale.z = (1.0, 1.0, 1.0)
    model.m_Rotation.x, model.m_Rotation.y, model.m_Rotation.z = (-270.0, 0.0, 0.0)
    model.m_Offset.x, model.m_Offset.y, model.m_Offset.z = (0.0, 1.0, 1.5)
    
    # Append model to the footprint
    footprint.Models().append(model)
    updated_count += 1

pcbnew.Refresh()
print(f"DONE: Applied 3D model to all {updated_count} footprint(s) on the board!")
