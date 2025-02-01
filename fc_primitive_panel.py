import bpy
from bpy.types import Panel

class FC_PT_Primitive_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Shapes"
    bl_category = "JMesh"
   
    def draw(self, context):
        
        layout = self.layout

        row = layout.row()
        col = row.column()
        col.prop(context.scene, "snap_to_target", text="Snap to mesh")

        # col = row.column()
        # col.prop(context.scene, "snap_offset", text="Offset")

        row = layout.row()
        col = row.column()
        col.prop(context.scene, "use_snapping", text="Snap to grid")

        if context.scene.primitive_type != "Curve":   

            row = layout.row()
            row.prop(context.scene, "extrude_immediate", text="Extrude immediately")

        row = layout.row()
        row.operator("object.fc_primitve_mode_op", text="Shape Mode")        
        
        for shape in context.scene.shape_list:
            box = layout.box()
            
            row = box.row(align=True)

            row.scale_y = 0.6 

            row.label(text=shape.name)

            select_op = row.operator("shape.select", text="", icon="RESTRICT_SELECT_OFF")
            select_op.shape_name = shape.name

            delete_op = row.operator("shape.delete", text="", icon="TRASH")
            delete_op.shape_name = shape.name
