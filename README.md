# refills_blender
A collection of Blender scripts used in the REFILLS project.

## Creation of Naive Product Meshes
We created a script that generates naive product meshes from a (hopefully high-res) front picture and bounding box information. 

![image](https://github.com/refills-project/refills_blender/blob/master/doc/somat_mesh.png)

### Installation
You need at least ```Blender v2.79```. For ```Ubuntu 14.04``` and ```Ubuntu 16.04```, go to [the Blender website](https://www.blender.org/) and download the newest pre-compiled binaries.

You also need to enable the plugin ```import_image_to_plane```. That is a standard plugin that is disabled by default. Open Blender, and then go to File > User Preferences > Import-Export and activate the tick on "Import-Export: Import Images as Planes". Then, hit "Save User Settings". You should only need to do this once.

![import_images_as_planes](https://github.com/refills-project/refills_blender/blob/master/doc/import_images_as_planes.png)

### Running the script
Example call for creating the Somat mesh from the included example data (width=14cm, depth=10cm, height=15cm):
```shell
$ ~/blender-2.79b-linux-glibc219-x86_64/blender -P scripts/create_naive_box_mesh.py --background -- images/somat_classic_pulver.png meshes/somat_classic_pulver.dae 0.14 0.1 0.15
```
