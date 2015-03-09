import bpy
import math
def numline(r=1.0,zerogap=0,origin=[0,0,3],sizedec=1.5,nit=9):
	y=zerogap+r
	for it in range(nit):
		bpy.ops.mesh.primitive_uv_sphere_add(location=(origin[0],origin[1]+y,origin[2]),size=r)
		bpy.ops.object.shade_smooth()
		bpy.ops.mesh.primitive_uv_sphere_add(location=(origin[0],origin[1]-y,origin[2]),size=r)
		bpy.ops.object.shade_smooth()	
		y+=r
		r=r/sizedec
		y+=r


def numlineup(r=1.0,zerogap=0,origin=[0,0,3],sizedec=1.5,nit=9):
	y=zerogap+r
	x=0.0
	origr=r
	for it in range(nit):
		bpy.ops.mesh.primitive_uv_sphere_add(location=(origin[0]+x,origin[1]+y,origin[2]))
		bpy.ops.object.shade_smooth()
		bpy.ops.mesh.primitive_uv_sphere_add(location=(origin[0]+x,origin[1]-y,origin[2]))
		bpy.ops.object.shade_smooth()	
		y+=r
		v=math.acos(( (2.0/3)**it+(2.0/3)**(it+1) )/(2*origr))
		h=2*origr*math.sin(v)
		x+=h
		r=r/sizedec
		y+=r



