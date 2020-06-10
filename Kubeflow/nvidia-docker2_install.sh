# 패키지 저장소를 추가한다.
distribution=$(. /etc/os-release;echo VERSION_ID)

curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
### 만약 위의 명령어가 실행되지 않는다면 아래 명령어를 입력해준다.---
distribution="ubuntu18.04"
### ------------------------------------------------------------

sudo apt-get update

sudo apt-get install nvidia-docker2

sudo systemctl restart docker

# nvidia-docker2가 정상적으로 설치되었는지 확인하기 위해, 다음 명령어를 실행한다. (이미지는 README.md에서 확인)
sudo docker run --runtime nvidia nvidia/cuda:10.0-base nvidia-smi

# Docker의 기본 런타임을 변경해준다
sudo vi /etc/docker/daemon.json
# 아래의 내용을 추가해준다.
{
    "default-runtime": "nvidia", 
    "runtimes": {
        "nvidia": {
            "path": "nvidia-container-runtime",
            "runtimeArgs": []
        }
    }
}


# Docker 재시작
sudo systemctl restart docker