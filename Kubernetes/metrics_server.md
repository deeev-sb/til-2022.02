# Metrics Server 설치하기

Metrics Server는 Kubernetes에서 리소스 메트릭 파이프라인을 구성하는 가장 기본적인 방법이다. 그러나 Kubernetes를 설치한다고 해서 Metrics Server가 자동으로 설치되지는 않으므로 직접 설치하는 과정이 필요하다.

![not_install_Metrics-Server](../img/metrics-server(1).PNG)

[kubernetes-sigs/metrics-server](https://github.com/kubernetes-sigs/metrics-server)를 참고하여 Metrics Server를 설치한다.

~~~ shell
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/download/v0.3.6/components.yaml
~~~

설치가 잘 진행되었다면, apiserver와 deployment, service를 확인 할 수 있다

~~~ shell
kubectl get apiservices | grep metrics

kubectl -n kube-system get deploy,svc | grep metrics-server
~~~

![Check_apiserver&deployment&service](../img/metrics-server(2).PNG)

여기까지 실행하면 metrics server는 돌지만 kubelet에 접근해 포드와 노드의 정보를 얻어오지 못하는 현상이 일어난다.

![metrics_not_available](../img/metrics-server(3).PNG)

이 현상은 tls 통신이 제대로 이뤄지지 않기 때문에 발생하는 것이므로, metrics server의 내용을 수정하여 서버와 통신이 원활하게 이루어지도록 옵션을 바꾼다.

~~~ shell
kubectl edit deployments.apps -n kube-system metrics-server
~~~

yaml 파일 내부에서 args를 찾아가 다음 설정 두 개를 추가한다.

| argument | 설명 |
|----------|------|
|- --kubelet-insecure-tls|인증서가 공인 기관에 승인 받지 않은 안전하지 않기 때문에 보안적으로 취약하지만 무시하겠다는 의미|
|- --kubelet-preferred-address-types=InternalIP|kubelet 연결에 사용할 때 사용하는 주소 타입을 지정|

![Option_change](../img/metrics-server(4).PNG)

`get pod`를 통해 kube-system에 metrics-server가 존재하는지 확인한다.

~~~ shell
kubectl get pod -n kube-system
~~~

![get_pod_kube-system](../img/metrics-server(5).PNG)

이제 pod에 대한 정보를 얻어 올 수 있다.

![get_pod](../img/metrics-server(6).PNG)

node에 대한 정보도 얻어 올 수 있다.

![get_nodes](../img/metrics-server(7).PNG)

이렇게 kubernetes 내부에 Metrics Server를 설치하여 관찰 할 수 있다.

<br>

---
🔗 **Reference**  
- https://github.com/kubernetes-sigs/metrics-server
- https://blog.naver.com/isc0304/221860790762
- https://www.inflearn.com/course/%EB%8D%B0%EB%B8%8C%EC%98%B5%EC%8A%A4-%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EB%A7%88%EC%8A%A4%ED%84%B0
- https://github.com/kubernetes-sigs/metrics-server/issues/300