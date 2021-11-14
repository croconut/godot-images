#!/bin/bash -e

FINAL_NAME="godot_${1}"
DL_URL=$2
ZIP_NAME=$3
EXTRACTED_FILE_NAME=$4

echo $FINAL_NAME $DL_URL $ZIP_NAME $EXTRACTED_FILE_NAME

mkdir -p /tmp/dl_tmp

cd /tmp/dl_tmp

echo "downloading godot from ${DL_URL} ..."
yes | wget -q ${DL_URL}
mkdir -p ~/.cache
mkdir -p ~/.config/godot
echo "unzipping ${ZIP_NAME} ..."
yes | unzip -q ${ZIP_NAME} -d ./

mv $EXTRACTED_FILE_NAME /usr/local/bin/${FINAL_NAME}
chmod u+x /usr/local/bin/${FINAL_NAME}

echo "installed ${FINAL_NAME} to /usr/local/bin/"

silent=$(cd -)
