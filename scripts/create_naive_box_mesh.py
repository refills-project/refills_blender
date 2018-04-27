#
# Copyright 2018, Georg Bartels (georg.bartels@cs.uni-bremen.de).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import bpy
from math import *
from mathutils import *
import os.path
import sys


def clear_scene():
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.select_all(action='TOGGLE')
    bpy.ops.object.delete(use_global=False)


def make_plane(dims, mat, loc=(0, 0, 0), rot=(0, 0, 0)):
    bpy.ops.mesh.primitive_plane_add(location=loc, rotation=rot)
    bpy.ops.transform.resize(value=dims)
    bpy.context.active_object.data.materials.append(mat)


def make_image_plane(infile, loc, rot, height):
    (dir, file) = os.path.split(infile)
    bpy.ops.import_image.to_plane(files=[{"name": file, "name": file}], directory=dir, relative=False)
    act_obj = bpy.context.active_object
    act_obj.location = loc
    act_obj.rotation_mode = 'QUATERNION'
    act_obj.rotation_quaternion = rot
    act_obj.dimensions = height * act_obj.dimensions


def make_object(infile, width, depth, height, mat):
    make_plane((0.5 * width, 0.5 * depth, 0), mat)  # bottom
    make_plane((0.5 * width, 0.5 * depth, 0), mat, (0, 0, height))  # top
    make_plane((0.5 * width, 0, 0.5 * height), mat, loc=(0, -depth / 2, height / 2), rot=(pi / 2.0, 0, 0))  # back
    make_image_plane(infile, (0, depth / 2.0, height / 2.0),
                     Quaternion((1, 0, 0), -pi / 2.0) * Quaternion((0, 0, 1), pi), height)  # front
    make_plane((0, depth / 2, height / 2), mat, loc=(width / 2, 0, height / 2), rot=(0, pi / 2, 0))  # left
    make_plane((0, depth / 2, height / 2), mat, loc=(-width / 2, 0, height / 2), rot=(0, pi / 2, 0))  # right
    # NO LONGER NEEDED?
    # bpy.context.scene.objects.active = bpy.data.objects["Plane"]
    # bpy.ops.object.select_all()
    # bpy.ops.object.join()


def make_default_material():
    mat = bpy.data.materials.new("MAT_NAME")
    mat.diffuse_color = (0.2, 0.2, 0.2)
    mat.use_transparency = True
    mat.transparency_method = 'Z_TRANSPARENCY'
    mat.alpha = 0.1
    return mat


def make_and_create_mesh(infile, outfile, width, depth, height):
    clear_scene()
    make_object(infile, width, depth, height, make_default_material())
    bpy.ops.wm.collada_export(filepath=outfile)


argv = sys.argv
argv = argv[argv.index("--") + 1:]  # get all args after "--"

if not len(argv) == 5:
    raise RuntimeError("Did not find all expected arguments: INFILE OUTFILE WIDTH HEIGHT DEPTH")

make_and_create_mesh(argv[0], argv[1], float(argv[2]), float(argv[3]), float(argv[4]))