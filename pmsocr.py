import argparse   
import json
import predict

def parse_args():
    """
    :return:进行参数的解析
    """
    description = "you should add those parameter"                
    parser = argparse.ArgumentParser(description=description)      
                                                                  
    parser.add_argument('-i','--image', help = '输入图片地址', type = str)               
    args = parser.parse_args()                                        
    return args

if __name__ == '__main__':
    args = parse_args()
    img_path = args.image
    predict.perdict_stuff_info(img_path)