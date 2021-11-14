# godot-images
creates docker images with linux godot engines with specific versioning. prefers headless over x11 and will not bother with anything that is not one of those types of godot engine.

versioning looks like main_version_sub_version_mono if mono and main_version_sub_version if not mono. if using the stable non-mono release, version will just be main_version. sub versions may be chained like in the case of 2.1.7_rc_20200815

images can be found at godotimages/godot:main_version_sub_version_mono
  
do not use godotimages/godot:latest
  
example images:
* you're using godot 3.0 mono --> pull godotimages/godot:3.0_mono
* you're using godot 3.1.2 rc2 --> pull godotimages/godot:3.1.2_rc2
* you're using godot 3.2.3 beta11 mono --> pull godotimages/godot:3.2.3_beta11_mono
* you're using godot 3.4 not mono --> pull godotimages/godot:3.4

full list of tags can be found [here](https://hub.docker.com/repository/registry-1.docker.io/godotimages/godot/tags)
 
godot will be added to the path in any given image and entry point should be overriden when used.
