sudo apt-get update

### docker-ce install, 18.09
### https://docs.docker.com/install/linux/docker-ce/ubuntu/

sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

sudo apt-get update

###리포지토리에서 사용 가능한 버전 확인
apt-cache madison docker-ce

sudo apt-get install -y docker-ce=5:18.09.9~3-0~ubuntu-xenial docker-ce-cli=5:18.09.9~3-0~ubuntu-xenial containerd.io

sudo su

mkdir -p /etc/systemd/docker.service.d

systemctl daemon-reload

systemctl restart docker

exit

### docker가 정상적으로 설치되었는지 확인한다.
sudo docker run hello-world