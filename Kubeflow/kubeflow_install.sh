# Kubeflow 설치
mkdir ~/kubeflow

cd ~/kubeflow

curl -L -O https://github.com/kubeflow/kfctl/releases/download/v1.0/kfctl_v1.0-0-g94c35cf_linux.tar.gz

tar -xvf kfctl_v1.0-0-g94c35cf_linux.tar.gz

# Kubeflow 배포를 쉽게 하기 위해, 환경 변수 생성
# path 설정은 본인의 컴퓨터에 맞게!!
export PATH=$PATH:"/home/ese-ksb/kubeflow"

export CONFIG_URI="https://raw.githubusercontent.com/kubeflow/manifests/v1.0-branch/kfdef/kfctl_istio_dex.v1.0.1.yaml"

export KF_NAME=kf-test

export BASE_DIR=/home/ese-ksb/kubeflow

export KF_DIR=${BASE_DIR}/${KF_NAME}

# kfcl_existing_arrikto.yaml 설정 파일로, kubeflow 배포
mkdir -p ${KF_DIR}

cd ${KF_DIR}

wget -O kfctl_istio_dex.yaml $CONFIG_URI

export CONFIG_FILE=${KF_DIR}/kfctl_istio_dex.yaml

kfctl apply -V -f ${CONFIG_FILE}
