# nouveau 설치 확인
lsmod | grep nouveau

# blacklist 파일 생성
sudo vi /etc/modprobe.d/blacklist-nouveau.conf

# 파일에 다음 내용 입력
blacklist nouveau
options nouveau modset=0

# 명령어 실행 후 재부팅
sudo update-initramfs -u

sudo service gdm stop



# Nvidia Driver 설치하기
sudo add-apt-repository ppa:graphics-drivers/ppa

sudo apt-get update

sudo apt-get install nvidia-driver-435

sudo reboot


# Nvidia Driver 확인하기
nvidia-smi