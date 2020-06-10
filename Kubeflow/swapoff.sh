sudo swapoff -a

# 재부팅 했을 때 swap이 다시 활성화되는 것을 막기 위해, swap 관련 부분을 주석 처리해준다.
sudo vi /etc/fstab

#-----------------------------------------------------------------------------------
# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/nvme0n1p1 during installation
UUID=64877307-a40b-4513-9076-9137c1f39219 /               ext4    errors=remount-ro 0       1
# /swapfile                                 none            swap    sw              0       0
#-----------------------------------------------------------------------------------
