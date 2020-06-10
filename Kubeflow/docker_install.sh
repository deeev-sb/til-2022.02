# apt가 https 저장소를 사용할 수 있도록 패키지 추가
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

# Docker GPG Key 추가
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# 저장소 추가
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"


sudo apt-get update


# k8s-device-plugin을 사용하려면 Docker 18.03 버전 필요하므로 18.03버전 설치
sudo apt-get install docker-ce=5:18.09.9~3-0~ubuntu-bionic docker-ce-cli=5:18.09.9~3-0~ubuntu-bionic containerd.io

sudo apt-mark hold docker-ce docker-ce-cli

# 설치 가능한 Docker 버전 보는 법
apt-cache madison docker-ce

# Docker가 정상적으로 설치되었는지 확인하기 위해 hello-world 이미지 실행
sudo docker run hello-world