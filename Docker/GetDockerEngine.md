# [Get Docker Engine](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)

- Uninstall old versions
  ~~~
  $ sudo apt-get remove docker docker-engine docker.io containerd runc
  ~~~
- Install Docker Engine
  - Install using the repository
    <br> (1) Update the `apt` package index :
    ~~~
    $ sudo apt-get update
    ~~~
    (2) Install packages to allow `apt` to use a repository over HTTPS :
    ~~~
    $ sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
    ~~~
    (3) Add Docker's official GPG key :
    ~~~
    $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    ~~~
     (4) Use the following command to set up the stable repository. To add the **nlghtly** or **test** repository, add the word `nightly` or `test` after the word `stable` in the commands below. (x86_64/amd64)
    ~~~
    $ sudo add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    $(lsb_release -cs) \
    stable"
    ~~~
  - Install Docker Engine - Community
  <br> (1) Update the `apt` package index : 
       ~~~
       $ sudo apt-get update
       ~~~
       (2) Install the **latest version** of Docker Engine - Community and containerd
       ~~~
       $ sudo apt-get install docker-ce
       ~~~
       (3) Verify that Docker Engine - Community is installed correctly by running the `hello-world` image
       ~~~
       $ sudo docker run hello-world
       ~~~
