#!/bin/bash -e

FINAL_NAME=${1}
DL_URL=$2
ZIP_NAME=$3
EXTRACTED_FILE_NAME=$4

mkdir -p /tmp/dl_tmp

cd /tmp/dl_tmp
yes | wget -q ${DL_URL}
yes | unzip -q ${ZIP_NAME} -d ./
ls ${EXTRACTED_FILE_NAME}
rm -rf ${ZIP_NAME}

[ -d ${EXTRACTED_FILE_NAME} ] && MONO_FILE_NAME=$(echo `ls ./${EXTRACTED_FILE_NAME} | grep -v ".dll" | head -1`) && mv ./${EXTRACTED_FILE_NAME}/${MONO_FILE_NAME} ./${EXTRACTED_FILE_NAME}/${FINAL_NAME} && mv ./${EXTRACTED_FILE_NAME}/* /usr/local/bin/
[ -f ${EXTRACTED_FILE_NAME} ] && mv ./${EXTRACTED_FILE_NAME} /usr/local/bin/${FINAL_NAME}

rm -rf ${EXTRACTED_FILE_NAME}

chmod u+x /usr/local/bin/${FINAL_NAME}

silent=$(cd -)
