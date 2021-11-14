# godot-images
creates docker image with library of linux godot engines with specific versioning. Prefers headless over x11 and will not bother with anything that is not one of those types of godot engine.

versioning looks like godot_<main_version>_<sub_version>_mono if mono and godot_<main_version>_<sub_version> if not mono. sub versions may be chained like in the case of godot_2.1.7_rc_20200815

image can be found at godotimages/godot:latest and is updated daily.

examples are: 
* godot_3.0.0_mono
* godot_3.0.0
* godot_3.2.3_rc2
* godot_3.2.3_beta1
* godot_3.0.3_rc1_mono
