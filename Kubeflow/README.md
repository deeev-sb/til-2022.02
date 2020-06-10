# Kubeflow

## Kubeflow install
Ubuntu 18.04 LTS, Nvidia Driver Gefore RTX 2070인 컴퓨터에 Kubeflow를 설치하는 내용이다.
<br>
<br>

### Nvidia Driver 설치하기

Ubuntu 18.04 환경에서 RTX 2070을 사용할 경우 nouveau로 자동 설정 되기 때문에 nouveau를 제거하는 작업 필요하며, 컨테이너에서 GPU를 사용할 예정이기 때문에 Nvidia Driver 설치 필요하다.

[Nvidia Driver 설치하기](./nvidia_driver_install.sh)

Nvidia Driver가 설치되면 다음과 같이 확인 가능하다.

![Nvidia-Driver](../img/Kubeflow_install(1).PNG)

<br>

### Docker 설치하기

[Docker 설치하기](./docker_install.sh)

Docker 설치 후 hello-world 이미지가 실행되면 Docker가 정상적으로 깔린 것이다.

![Docker_install](../img/kubeflow_install(2).PNG)

컨테이너에서 GPU를 사용하기 위해서 nvidia-docker2를 설치해야한다.

[nvidia-docker2 설치하기](./nvidia-docker2_install.sh)

nvidia-docker2가 정상적으로 설치되면 다음과 같이 확인 가능하다.

![nvidia-docker2_install](../img/kubeflow_install(3).PNG)

<br>

### Kubernetes 설치하기

Kubernetes를 설치하기 위해서 swap을 비활성화한다.

[swapoff](./swapoff.sh)

Kubelet, Kubeadm, Kubectl은 Master와 Worker 모두 필요하므로 공통으로 설치해준다.  
Kubeflow 문서에 따르면 현재 권장하는 Kubernetes 버전은 1.14이지만, 1.15버전도 호환이 되므로 1.15.10-00 버전으로 설치한다.

[kubernetes 기본 요소 설치하기](./kubernetes_basic_install.sh)

Kubernetes Master Node의 경우 kubeadm init 명령어를 통해 초기화시켜준다.

[Kubernetes Master Node 설치하기](./kubernetes_master_install.sh)

Kubernetes 접속이 되면 다음과 같다.

![Kubernetes_Connect](../img/kubeflow_install(4).PNG)

cilim 포드의 READY가 1/1dl ehlaus, Kubernetes Cluster를 사용할 수 있다.

![Master_install_finish](../img/kubeflow_install(5).PNG)

Kubernetes Worker Node의 경우 kubeadm join 명령어를 통해 Master Node와 연결해준다.

~~~
kubeadm join 192.168.0.3:6443 --token fyjmjm.buuiz9xb9skq85lm \
    --discovery-token-ca-cert-hash sha256:f20c8957e66c1423647f9a9ca301c1c63f76400cfc98671702153aaea3ef0df6 
~~~

Kubernetes는 기본적으로 cluster의 control plane node는 보안상의 이유로 노드가 격리되어 있어서, 포드가 스케줄링되지 않는다. 1대의 머신만을 사용한다면 노드 격리를 해제하여 확인한다.

~~~
kubectl taint nodes --all node-role.kubernetes.io/master-node/mortar untainted
~~~

<br>

### Nvidia Plugin 설치하기

Kubernetes에서 GPU를 사용하기 위해서, nvidia k8s-device-plugin을 설치한다.

~~~
kubectl apply -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v1.12/nvidia-device-plugin.yml
~~~

device-plugin 포드가 정상적으로 작동했는지 확인한다.  
(control plane node를 격리하지 않은 경우 `No resources found.`를 출력한다.)

~~~
kubectl -n kube-system get pod -l name=nvidia-device-plugin-ds
~~~

![device-plugin_확인](../img/kubeflow_install(6).PNG)

<br>

### Kubeflow 설치하기

Kubeflow에서는 인증/권한 기능을 위해서 istio를 사용한다. 그래서 istio-system이라는 namespace에 istio 관련 component가 설치된다. Kubernetes 1.15버전에서는 `Service Account Token Volume Projection` 기능이 비활성화되어 있으므로 활성화시켜 줘야한다.
기능을 활성화 하기 위해서는, kube-apiserver manifest에 몇 가지 플래그를 추가해야한다.

~~~
sudo vi /etc/kubernetes/manifests/kube-apiserver.yaml
# 다음 내용을 추가한다. ------------------------
    - --service-account-signing-key-file=/etc/kubernetes/pki/sa.key
    - --service-account-issuer=api
    - --service-account-api-audiences=api,vault
~~~

Kubeflow를 쉽게 설치하기 위해서는 동적 볼륨 프로비저너가(dynamic volume provisioner)가 필요하다. 여기서는 local directory를 이용하는 Local Path Provisioner를 사용하겠다.

[Dynamic Volume Provisioner 설치하기](./provisioner_install.sh)

local path를 기본으로 설정하기 전
![local path를 기본으로 설정하기 전](../img/Kubeflow_install(7).PNG)

local path를 기본으로 설정하기 후
![local path를 기본으로 설정하기 후](../img/Kubeflow_install(8).PNG)

Kubeflow를 설치하기 위해서, kftctl을 릴리즈 페이지에서 다운로드 합니다. 현재 v1.0 버전이 최신이므로, v1.0 버전을 기준으로 설치했습니다.

[Kubeflow 설치하기](./kubeflow_install.sh)

Kubeflow namespace와 istio-system namespace의 포드를 명령어를 통해 조회해보면 아래와 같다.

~~~
# Kubeflow namespace 조회
kubectl -n kubeflow get pod
~~~
![Kubeflow namespace 조회](../img/Kubeflow_install(9).PNG)
~~~
# istio-system namespace 조회
kubectl -n istio-system get pod
~~~
![istio-system namespace 조회](../img/Kubeflow_install(10).PNG)

### Kubeflow 접속하기

istio-ingressgateway를 통해서 Kubeflow GUI 접속한다. 여기서는 편의를 위해 NodePort를 사용했다.

~~~
kubectl -n istio-system get service istio-ingressgateway
~~~

![istio-ingressgateway를 통한 포트 확인](../img/Kubeflow_install(11).PNG)

서비스 타입이 NodePort이고, 80번 포트가 31380 노드포트로 열려있다. 브라우저를 실행하고 해당 포트로 접속한다. 입력은 CLUSTER-IP:PORT 순으로 한다. (10.110.216.2:80)

![Kubeflow 포트 입력하여 접속하기](../img/Kubeflow_install(12).PNG)

기본 설정을 바꾸지 않았다면, 사용자 이름은 admin@kubeflow.org 이고, 비밀번호는 12341234 이다.

![Kubeflow 이메일 및 비밀번호 입력](../img/Kubeflow_install(13).PNG)

기본값은 admin이고 원하는 namespace로 변경 가능하다.

![Kubeflow Namespace](../img/Kubeflow_install(14).PNG)

Namespace가 생성되면, Kubeflow Dashborad 화면을 볼 수 있다.

![Kubeflow Dashboard](../img/Kubeflow_install(15).PNG)


<br>
<br>
---
🔗 **Reference**  
- https://docs.docker.com/install/linux/docker-ce/ubuntu/
- https://github.com/NVIDIA/nvidia-docker  
- https://www.kangwoo.kr/2020/02/17/pc%ec%97%90-kubeflow-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0-1%eb%b6%80-nvidia-%eb%93%9c%eb%9d%bc%ec%9d%b4%eb%b2%84-docker-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0/
- https://github.com/NVIDIA/nvidia-docker/issues/963
- https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/install-kubeadm/
- https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/
- https://github.com/NVIDIA/k8s-device-plugin
- https://www.kangwoo.kr/2020/02/17/pc%ec%97%90-kubeflow-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0-2%eb%b6%80-kubernetes-nvidia-device-plugin-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0/
- https://github.com/rancher/local-path-provisioner#deployment
- https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/#changing-the-default-storageclass
- https://www.kubeflow.org/docs/started/k8s/kfctl-k8s-istio/
- https://www.kubeflow.org/docs/started/k8s/kfctl-existing-arrikto/
- https://www.kangwoo.kr/2020/02/18/pc%ec%97%90-kubeflow-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0-3%eb%b6%80-kubeflow-%ec%84%a4%ec%b9%98%ed%95%98%ea%b8%b0/