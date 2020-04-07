# How to install kubernetes on 'Virtualbox'

- Add repository
  ~~~
  $ sudo apt-get update && sudo apt-get install -y apt-transport-https curl
  $ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
  $ cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
  deb http://apt.kubernetes.io/ kubernetes-xenial main
  EOF
  ~~~
  - If `ERROR: This command can only be used by root.` occurs :
    ~~~
    $ sudo su
    ~~~
    ~~~
    $ apt-get update && apt-get install -y apt-transport-https curl
    $ curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
    $ cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
    deb http://apt.kubernetes.io/ kubernetes-xenial main
    EOF
    ~~~
- Install docker, kubeadm
  ~~~
  $ sudo apt-get update
  $ sudo apt-get install docker.io apt-transport-https kubelet kubeadm kubectl
  ~~~
- swap off
  ~~~
  $ sudo swapoff -a
  ~~~
