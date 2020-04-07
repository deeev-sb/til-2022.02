# Kubernetes

### Kubernetes란?
- 컨테이너 오케스트레이션 플랫폼 중 하나
- 컨테이너를 쉽고 빠르게 배포/확장하고 관리를 자동화해주는 오픈소스 플랫폼
- 여러 클러스터의 호스트 간에 애플리케이션 컨테이너의 배치, 스케일링, 운영을 자동화하기 위한 플랫폼을 제공하는 것이 목적
- kubernetes가 너무 길어서 k8s(케이에이츠) or kube(큐브) 로 줄여서 부름

### Kubernetes의 기본 기능
- 상태관리 : 상태를 선언하고 선언한 상태를 유지. 노드가 죽거나 컨테이너 응답이 없을 경우 자동으로 복구
- Scheduling : 클러스터의 여러 노드 중 조건에 맞는 노드를 찾아 컨테이너를 배치
- Cluster : 가상 네트워크를 통해 하나의 서버에 있는 것처럼 통신
- Service Discovery : 서로 다른 서비스를 쉽게 찾고 통신할 수 있음
- Resource Monitoring : cAdvisor라는 리소스 메트릭(지표) 수집도구를 통한 리소스 모니터링
- Auto-scaling : 리소스에 따라 자동으로 서비스를 조정함
- RollOut/RollBack : 배포/롤백 및 버전 관리

### Kubernetes 기본 개념
![DesiredState](https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/desired-state.png)
- Current state : 현재 상태
- Desired state : 관리자가 원하는 상태
- 관리자가 서버를 배포할 때 직접적인 동작을 명령하지 않고 상태를 선언하는 방식 사용
  - 명령 $ docker run
  - 상태 $ kubectl create (물론 kubectl run도 있지만 잘 사용하지 않음)

### kubernetes Controller
![KubernetesController](https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/workload.png)
- Daemon Set : 로그나 모니터링 등 모든 노드에 설치가 필요한 경우에 사용
- Deployment : 새로운 버전의 애플리케이션을 다양한 전략으로 배포 가능 
- Stateful Sets : 실행 순서를 보장하여 순서나 데이터가 중요한 경우 사용
- CronJob / Job : 배치성 작업에 사용
- Replication Controller (RC) : 지정된 숫자로 Pod를 기동 및 관리

### Kubernetes 배포
- 롤링 업데이트
  - 일반적으로 많이 사용하는 배포 패턴
  - 새 버전을 배포하면서, 새 인스턴스를 하나씩 늘려가고, 기존 버전은 하나씩 줄여가는 방식
  - 기존 버전과 새 버전이 동시에 존재 가능
  - 시스템을 무장애로 업데이트 가능
  - 새 버전용 컨트롤러와 기존 버전용 컨트롤러 필요
- Deployment
  - kubernetes에서 일반적으로 사용하는 배포 패턴
  - 롤링 업데이트를 좀 더 자동화한 객체 (컨트롤러 개념에 포함됨)
  - 컨트롤러를 따로 정의하지 않고, Deployment 객체만 만듦
  - Deployment 객체가 자동으로 롤링 업데이트를 해 줌

### Kubernetes Object
- Pod
![Pod](https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/pod.png)
  - kubernetes에서 배포할 수 있는 가장 작은 단위
- ReplicaSet
![ReplicaSet](https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/replicaset.png)
  - Pod를 한 개 이상 복제하여 관리하는 오브젝트
  - Pod 생성 및 개수 유지를 위해서는 반드시 ReplicaSet을 사용해야함 
- Service
  - 네트워크와 관련된 오브젝트
  - Pod를 외부 네트워크와 연결해주고 여러 개의 Pod를 바라보는 내부 로드 밸런서 생성 시 사용
  - 내부 DNS에 서비스 이름을 도메인으로 등록하기 때문에 서비스 디스커버리 역할도 함
- Volume
  - 저장소와 관련된 오브젝트

### Kubernetes 클러스터 아키텍처
![KubernetesClusterArchitecture](https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/master-node.png)
- 마스터 (Master)
  - 노드를 제어하고 전체 클러스터를 관리해주는 컨트롤러
  - 전체적인 제어/관리를 하기 위한 관리 서버
  - 다양한 모듈이 확장성을 고려하여 기능별로 쪼개져 있음 
  - 관리자만 접근할 수 있게 보안 설정을 해야 하고 마스터 서버가 죽으면 클러스터를 관리할 수 없기 때문에 보통 3중화로 구성
- 노드 (Node)
  - 마스터에 의해 명령을 받고 실제 서비스를 하는 컴포넌트
  - 노드 서버는 마스터 서버와 통신하면서 필요한 Pod를 생성 및 네트워크와 볼륨 설정
  - 컨테이너가 배포될 물리 서버 또는 가상 머신 이며, 워커 노드(Worker Node)라고도 부름
- Kubelet
  - 명령 도구

### Master 구성요소
![MasterComponent](https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/kubernetes-master.png)
- API 서버 kube-apiserver
  - API 서버는 모든 요청을 처리하는 마스터 핵심 모듈
  - kubetcl의 요청 뿐 아니라 내부 모듈의 요청도 처리하며, 권한을 체크하여 요청 거부도 가능
  - 원하는 상태(desired state)를 key-value 저장소에 저장하고 저장된 상태를 조회하는 역할
  - 노드에서 실행 중인 컨테이너의 로그를 보여주고 명령을 보내는 등 디버거 역할도 수행
- 분산 데이터 저장소 etcd
  - RAFT 알고리즘을 이용한 key-value 저장소
  - 여러 개로 분산하여 복제할 수 있기 때문에 안정성이 높고 속도가 빠른 편
  - 단순히 값을 저장하고 읽는 기능 뿐만 아니라 watch 기능이 있어 어떤 상태가 변경되면 바로 체크하여 로직 실행
  - 클러스터의 모든 설정, 상태 데이터는 여기 저장되므로 etcd만 잘 백업해두면 언제든지 클러스터 복구 가능
  - etcd는 API 서버만 통신
- 스케줄러 kube-scheduler
  - 스케줄러는 할당되지 않은 Pod를 필요한 자원, 라벨에 따라 적절한 노드 서버에 할당해주는 모듈
- 큐브 컨트롤러 kube-controller-manager
  - 큐브 컨트롤러는 kubernetes에 있는 거의 모든 오브젝트의 상태 관리
  - 오브젝트별로 철저하게 분업화되어 Deployment는 ReplicaSet을 생성하고 ReplicaSet은 Pod를 생성하고 Pod는 스케줄러가 관리하는 형식
- 클라우드 컨트롤러 cloud-controller-manager
  - 클라우드 컨트롤러는 AWS, GCE, Azure 등 클라우드에 특화된 모듈
  - 노드 추가/삭제 및 로드 밸런서 연결 또는 볼륨을 붙일 수 있음

### Node 구성요소
![NodeComponent](https://subicura.com/assets/article_images/2019-05-19-kubernetes-basic-1/kubernetes-node.png)
- 큐블릿 kubelet
  - 노드에 할당된 Pod의 생명주기 관리
  - Pod 생성 및 pod 안의 컨테이너에 이상이 없는지 확인하면서 주기적으로 마스터에 상태 전달
  - API 서버의 요청을 받아 컨테이너 로그를 전달하거나 특정 명령을 대신 수행하기도 함
- 프록시 kube-proxy
  - Pod로 연결되는 네트워크 관리


#### 출처
Kubernetes 공식문서 (https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/) <br/>
KT Cloud (https://cloud.kt.com/portal/user-guide/education-eduadvanced-edu_adv_3) <br/>
쿠버네티스 시작하기 - Kubernetes란 무엇인가?  (https://subicura.com/2019/05/19/kubernetes-basic-1.html) <br/>
쿠버네티스 기본 개념 정리 (https://dailyheumsi.tistory.com/208)








