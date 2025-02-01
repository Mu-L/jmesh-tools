import bpy

class SHAPE_OT_Select(bpy.types.Operator):
    bl_idname = "shape.select"
    bl_label = "Select Shape"

    shape_name: bpy.props.StringProperty()

    def execute(self, context):
        self.report({'INFO'}, f"Select object '{self.shape_name}'.")
        return {'FINISHED'}
    
class SHAPE_OT_Delete(bpy.types.Operator):
    bl_idname = "shape.delete"
    bl_label = "Select Shape"

    shape_name: bpy.props.StringProperty()

    def execute(self, context):
        self.report({'INFO'}, f"Delete object '{self.shape_name}'.")
        return {'FINISHED'}