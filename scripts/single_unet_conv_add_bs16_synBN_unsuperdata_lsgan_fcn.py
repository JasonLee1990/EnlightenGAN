import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=str, default="8097")
parser.add_argument("--train", action='store_true')
parser.add_argument("--test", action='store_true')
parser.add_argument("--predict", action='store_true')
opt = parser.parse_args()

if opt.train:
	os.system("python train.py \
		--dataroot /ssd1/yifan/unsuper_compete \
		--no_dropout \
		--name single_unet_conv_add_bs16_synBN_unsuperdata_lsgan_fcn \
		--model single \
		--dataset_mode unaligned \
		--which_model_netG sid_unet_resize \
		--fineSize 256 \
		--skip 1 \
		--batchSize 16 \
		--use_norm 1 \
        --syn_norm \
		--use_wgan 0 \
		--instance_norm 0 \
		--fcn 1 \
		--gpu_ids 0,1 \
		--display_port=" + opt.port)

elif opt.test:
	for i in range(19):
	        os.system("python test.py \
	        	--dataroot /ssd1/yifan/compete_LOL \
	        	--name single_unet_conv_add_bs16_synBN_unsuperdata_lsgan_fcn \
	        	--model single \
	        	--which_direction AtoB \
	        	--no_dropout \
	        	--dataset_mode pair \
	        	--which_model_netG sid_unet_resize \
	        	--skip 1 \
	        	--use_norm 1 \
	        	--use_wgan 0 \
	        	--instance_norm 0 \
	        	--which_epoch " + str(i*10+10))

elif opt.predict:
	for i in range(19):
	        os.system("python predict.py \
	        	--dataroot /ssd1/yifan/common_dataset \
	        	--name single_unet_conv_add_bs16_synBN_unsuperdata_lsgan_fcn \
	        	--model single \
	        	--which_direction AtoB \
	        	--no_dropout \
	        	--dataset_mode unaligned \
	        	--which_model_netG sid_unet_resize \
	        	--skip 1 \
	        	--use_norm 1 \
	        	--use_wgan 0 \
	        	--instance_norm 0 --resize_or_crop='no'\
	        	--which_epoch " + str(i*10+10))
