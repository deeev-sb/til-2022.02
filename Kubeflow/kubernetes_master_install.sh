# kubeadm init
sudo kubeadm init --pod-network-cidr=10.217.0.0/16

# 설치가 완료되면, kubectl을 사용하기 위해서 관리자 설정 파일을 유저 디렉토리로 복사한다.
mkdir -p $HOME/.kube

sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown $(id -u):$(id -g) $HOME/.kube/config

# Kubernetes 접속을 테스트하기 위해, 다음 명령어를 실행한다.
kubectl cluster-info

# cilium을 쿠버네티스에 설치한다.
kubectl create -f https://raw.githubusercontent.com/cilium/cilium/v1.6/install/kubernetes/quick-install.yaml

# cilim 포드의 READY가 1/1dl ehlaus, Kubernetes Cluster를 사용할 수 있다.
kubectl get pods -n kube-system --selector=k8s-app=cilium