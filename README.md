# godot-images
creates docker images with linux godot engines with specific versioning. prefers headless over x11 and will not bother with anything that is not one of those types of godot engine.

versioning looks like <main_version>___<sub_version>___mono if mono and <main_version>___<sub_version> if not mono. sub versions may be chained like in the case of 2.1.7___rc___20200815

images can be found at godotimages/godot:<main_version>___<sub_version>___<mono>
  
do not use godotimages/godot:latest
  
example images:
* you're using godot 3.0 mono --> pull godotimages/godot:3.0___mono
* you're using godot 3.1.2 rc2 --> pull godotimages/godot:3.1.2___rc2
  
godot will be added to the path in any given image and entry point should be overriden when used.
