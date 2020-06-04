### swapoff
sudo swapoff -a

sudo sed s/\\/dev\\/mapper\\/centos-swap/#\ \\/dev\\/mapper\\/centos-swap/g -i /etc/fstab

### kubeadm init
sudo kubeadm init --pod-network-cidr=192.168.0.0/16

### ---------------------------------
### I0603 22:10:52.986556   28880 version.go:248] remote version is much newer: v1.18.3; falling back to: stable-1.15
### [init] Using Kubernetes version: v1.15.12
###
### ...
###
### Your Kubernetes control-plane has initialized successfully!
### 
### To start using your cluster, you need to run the following as a regular user:
### 
###   mkdir -p $HOME/.kube
###   sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
###   sudo chown $(id -u):$(id -g) $HOME/.kube/config
### 
### You should now deploy a pod network to the cluster.
### Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
###   https://kubernetes.io/docs/concepts/cluster-administration/addons/
### 
### Then you can join any number of worker nodes by running the following on each as root:
### 
### kubeadm join 192.168.0.3:6443 --token sybtdq.cv4oi3vp001zx27t \
###     --discovery-token-ca-cert-hash sha256:0e95f085bb80b7f0c8423a9754cda8b2fcbd4bb3d3e194b8a8c354b57f32a7b4 
### ---------------------------------

mkdir -p $HOME/.kube

sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config

sudo chown $(id -u):$(id -g) $HOME/.kube/config

### enable master node sheduling
kubectl taint nodes --all node-role.kubernetes.io/master-

kubectl apply -f https://docs.projectcalico.org/v3.11/manifests/calico.yaml