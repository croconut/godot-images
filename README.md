# godot-images
creates docker images with linux godot engines with specific versioning. will only create images for headless linux versions so versions before 3.0.6 are not supported.

versioning looks like main_version_sub_version_mono if mono and main_version_sub_version if not mono. if using the stable non-mono release, version will just be main_version. sub versions may be chained like in the case of 2.1.7_rc_20200815

images can be found at godotimages/godot:main_version_sub_version_mono
  
do not use godotimages/godot:latest
  
example images:
* you're using godot 3.0.6 mono --> pull godotimages/godot:3.0.6_mono
* you're using godot 3.1.2 rc2 --> pull godotimages/godot:3.1.2_rc2
* you're using godot 3.2.3 beta11 mono --> pull godotimages/godot:3.2.3_beta11_mono
* you're using godot 3.4 --> pull godotimages/godot:3.4

full list of tags can be found [here](https://hub.docker.com/repository/registry-1.docker.io/godotimages/godot/tags)
 
godot will be added to the path in any given image and entry point should be overriden when used.
