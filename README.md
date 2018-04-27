# refills_blender
A collection of Blender scripts used in the REFILLS project.

## Creation of Naive Product Meshes
### Installation
You need at least ```Blender v2.79```. For ```Ubuntu 14.04``` and ```Ubuntu 16.04```, go to [the Blender website](https://www.blender.org/) and download the newest pre-compiled binaries.

You also need to enable the plugin ```import_image_to_plane```. That is a standard plugin that is disabled by default. Open Blender, and then go to File > User Preferences > Import-Export and activate the tick on "Import-Export: Import Images as Planes". Then, hit "Save User Settings". You should only need to do this once.

![import_images_as_planes](https://github.com/refills-project/refills_blender/blob/master/doc/import_images_as_planes.png)

### Running the script
Go to the directory in which you have installed blender and run:
```shell
$ blender --background -P <script-name>
```
