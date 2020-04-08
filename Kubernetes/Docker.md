# Docker

### Docker란?
- 애플리케이션을 신속하게 구축, 테스트 및 배포할 수 있는 소프트웨어 플랫폼
- 소프트웨어를 컨테이너라는 표준화된 유닛으로 패키징 하며, 이 컨테이너에는 라이브러리, 시스템 도구, 코드, 런타임 등 소프트웨어를 실행하는 데 필요한 모든 것이 포함되어 있음
- Docker를 사용하면 환경에 구애 받지 않고 애플리케이션을 신속하게 배포 및 확장 할 수 있으며 코드가 문제없이 실행될 것임을 확신할 수 있음

### VM vs Container
![VMvsContainer](https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/vm-vs-docker.png)
- Hypervisor 기반 가상화
  - 기존의 가상화 방식은 주로 OS를 가상화 → overhead 발생
  - VMware나 VirtualBox 같은 가상머신은 호스트 OS 위에 게스트 OS 전체를 가상화 하여 사용하는 방식
- 컨테이너(Container) 기반 가상화
  - 단순 프로세스를 격리시키기 때문에 가볍고 빠르게 동작
  - CPU, Memory는 프로세스가 필요한만큼만 사용하므로 성능상의 이슈는 거의 없음

### Docker 구조
![Docker](https://docs.docker.com/engine/images/architecture.svg)
- Docker는 Client와 Server (Docker Host) 구조
  - Client : user가 'docker run' 등의 명령어를 입력하면 이를 Server쪽에 전송하고, 이를 Docker daemon이 수행
  - Docker daemon : docker api 요청을 수신하고 image, container, network, volume과 같은 docker object를 관리. 다른 docker daemon과의 통신을 통해 서비스 관리 가능
 - Docker Registry : Docker 이미지 저장소
 - Image : 컨테이너 실행에 필요한 파일과 설정 값 등을 포함하고 있는 것으로 상태 값을 가지지 않고 변하지 않음(Immutable). 공식 이미지의 경우 해당 이미지를 실행하기 위한 모든 것이 세팅 되어 있음.

### Docker 특징
![DockerContainerLayer](https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/image-layer.png)
- 레이어 저장방식
  - 도커 이미지는 컨테이너를 실행하기 위한 모든 정보를 가지고 있기 때문에 용량이 큼. 처음 이미지를 다운받을 때는 크게 부담이 되지 않지만, 기존 이미지에 파일 하나 추가했다고 다시 해당 용량이 큰 파일을 다시 받는 건 비효율적
  - 도커는 이런 문제를 해결하기 위해서 Layer라는 개념을 사용하고 유니온 파일 시스템을 이용하여 여러 개의 레이어를 하나의 파일시스템으로 사용할 수 있게 해 줌
  - 컨테이너를 생성할 때도 레이어 방식을 사용하여 기존의 이미지 레이어 위에 읽기/쓰기(read-write) 레이어 추가
![DockerImage](https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/docker-image.png)
- Dockerfile
  - 도커는 이미지를 만들기 위해 Dockerfile이라는 파일에 자체 DSL(Domain-specific language) 언어를 이용하여 이미지 생성 과정을 적음
  - Application 실행에 필요한 과정들을 Dockerfile로 작성하여 관리 가능
  - 해당 Dockerfile을 보면서 이미지 생성과정을 알 수 있으므로 수정 용이
- Docker hub : Docker hub를 통해 공개 이미지를 무료로 관리


#### 출처
Docker 공식문서 (https://docs.docker.com/engine/docker-overview/) <br/>
KT Cloud (https://cloud.kt.com/portal/user-guide/education-eduadvanced-edu_adv_2) <br/>
초보를 위한 도커 안내서 - 도커란 무엇인가? (https://subicura.com/2017/01/19/docker-guide-for-beginners-1.html)


