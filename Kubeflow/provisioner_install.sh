# Local Path Provisioner 설치
kubectl apply -f https://raw.githubusercontent.com/rancher/local-path-provisioner/master/deploy/local-path-storage.yaml

# storage class를 조회하면 local-path가 기본 storage로 설정이 되어있지 않음을 확인 할 수 있다.
kubectl get storageclass
# 명령어를 입력하면 다음과 같은 내용을 확인 할 수 있다.-----------

# ------------------------------------------------------------

# Local Path를 기본 storage class로 설정
kubectl patch storageclass local-path -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'

# storage class를 다시 조회해보면, Local Path가 기본으로 설정된 것을 확인 할 수 있다.
kubectl get sc