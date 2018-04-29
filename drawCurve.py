from autoMetric import *



if __name__=="__main__":
	gtlist = fileList('./groundtruth/kaggle/', '*.bmp')
	cnnproblist = fileList('./probgraph/kaggle/matlab/', '*.jpg')
	unetproblist = fileList('./probgraph/kaggle/unet/','*.jpg')
	resproblist = fileList('./probgraph/kaggle/Resiudal/','*.jpg')
	modelName=['matlab','unet','resunet']


	drawCurve(gtlist,[unetproblist,cnnproblist,resproblist],modelName,'kaggle')
