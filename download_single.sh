#!/bin/bash -e

FINAL_NAME="godot_${1}"
DL_URL=$2
ZIP_NAME=$3
EXTRACTED_FILE_NAME=$4

mkdir -p /tmp/dl_tmp

cd /tmp/dl_tmp
yes | wget -q ${DL_URL}
yes | unzip -q ${ZIP_NAME} -d ./

rm -rf ${ZIP_NAME}

mv $EXTRACTED_FILE_NAME /usr/local/bin/${FINAL_NAME}
chmod u+x /usr/local/bin/${FINAL_NAME}

echo "installed ${FINAL_NAME} to /usr/local/bin/"

silent=$(cd -)
