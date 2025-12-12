# Flash Raspberry Pi image
sudo dd if=mechbot-edge-v2.1.img \
  of=/dev/mmcblk0 \
  bs=4M status=progress
