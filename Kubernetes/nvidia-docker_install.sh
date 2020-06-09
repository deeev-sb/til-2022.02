### nvidia 드라이버가 설치되어 있는지 확인한다.
nvidia-smi

### nvidia 드라이버가 설치되어 있다면 아래 내용을 진행한다.
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update

sudo apt-get install -y nvidia-docker2

sudo vi /etc/docker/daemon.json

#daemon.json에 아래 내용을 추가한다.
{"default-runtime": "nvidia",
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}
#----------------------------------------------

sudo systemctl restart docker

sudo docker run --runtime=nvidia --rm nvidia/cuda nvidia-smi