# Dashboard 사용하기

다음 명령어를 통해 dashboard를 만들 수 있다.

~~~ shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.1/aio/deploy/recommended.yaml
~~~

![create_dashboard](../img/k8s_dashboard(1).PNG)

다음 명령어를 통해 dashboard를 확인 할 수 있다.

~~~ shell
kubectl get all -n kubernetes-dashboard
~~~

![check_dashboard](../img/k8s_dashboard(2).PNG)

현재 `service/kubernetes-dashboard`의 type이 ClusterIp 이므로, 접속 할 수 있게 type을 NodePort로 변경해준다. 다음 명령어를 통해 yaml 파일을 열어 type 부분을 변경하면 된다.

~~~ shell 
kubectl edit service/kubernetes-dashboard -n kubernetes-dashboard
~~~

![chang_port_type](../img/k8s_dashboard(3).PNG)

지정된 port 번호를 입력하여 접속하면

![page_https](../img/k8s_dashboard(4).PNG)

HTTPS server라고 하므로, https://127.0.0.1:30844로 접속한다.

![danger](../img/k8s_dashboard(5).PNG)

보안 위험 가능성이 있다고 뜨는데, `고급`을 눌러서 `위험을 감수하고 계속`으로 우회해서 사용하면 된다.

Kubernetes Dashboard에 접속하면 `토큰`을 입력하거나 `Kubeconfig`를 입력하라고 뜬다. 이것은 Dashboard에 접속 가능한 사람인지 확인하는 것이다.

![dashboard_start](../img/k8s_dashboard(6).PNG)

Service Account는 다음 명령어를 통해 확인 가능하다.

~~~ shell
kubectl get sa -n kubernetes-dashboard
~~~

![dashboard_start](../img/k8s_dashboard(7).PNG)

아래 명령어를 통해 kubernetes-dashboard의 yaml 파일 내용을 열어 kubernetes-dashboard의 token name을 확인 할 수 있다.

~~~ shell
kubectl get sa -n kubernetes-dashboard kubernetes-dashboard -o yaml
~~~

![check_token_name](../img/k8s_dashboard(8).PNG)

token name으로 yaml 파일을 열어주면 token이 나온다.

~~~ shell
kubectl describe secrets -n kubernetes-dashboard kubernetes-dashboard-token-d6z2q
~~~

![check_token](../img/k8s_dashboard(9).PNG)

token을 입력하면 Kubernetes Dashboad에 접속 할 수 있지만 권한이 없어서 아무것도 뜨지 않는다. 

![check_token](../img/k8s_dashboard(10).PNG)

RBAC를 만들어야 권한이 생긴다. kubernetes-dashboard Service Account에 권한을 준다.

~~~ shell
vi kube-dashoboard-role-binding.yaml
# 아래 내용을 추가한다. ----------------------
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: kubernetes-dashboard-rolebinding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: kubernetes-dashboard
  namespace: kubernetes-dashboard
#-------------------------------------------
~~~

그 다음 kubectl로 만들어준다.

~~~
kubectl create -f kube-dashoboard-role-binding.yaml
~~~

cluster-admin에 대한 권한을 kubernetes-dashboard에 줬기 때문에 Dashboard에 내용이 뜨는 것을 확인할 수 있다.

![check_token](../img/k8s_dashboard(11).PNG)

이제 Dashboard를 통해 모니터링을 할 수 있으며, 리소스에 대한 정보를 수정하거나 삭제 할 수 있고, yaml 파일도 수정 할 수 있다.

<br>

---
🔗 **Reference** 
- https://www.inflearn.com/course/%EB%8D%B0%EB%B8%8C%EC%98%B5%EC%8A%A4-%EC%BF%A0%EB%B2%84%EB%84%A4%ED%8B%B0%EC%8A%A4-%EB%A7%88%EC%8A%A4%ED%84%B0
- https://github.com/kubernetes/dashboard
- https://github.com/kubernetes/dashboard/blob/master/docs/user/access-control/creating-sample-user.md