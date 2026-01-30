import os
import tarfile
import math

def split_tar_gz(input_file, max_size_gb=5):
    """
    拆分tar.gz文件为多个小于指定大小的文件，每个文件可独立解压
    
    Args:
        input_file (str): 输入tar.gz文件路径
        max_size_gb (int): 每个拆分文件的最大大小(GB)
    """
    # 转换为字节
    max_size = max_size_gb * 1024 * 1024 * 1024
    
    # 检查输入文件是否存在
    if not os.path.exists(input_file):
        print(f"错误: 文件 {input_file} 不存在")
        return
    
    # 检查文件是否为tar.gz格式
    if not input_file.endswith('.tar.gz'):
        print(f"错误: 文件 {input_file} 不是tar.gz格式")
        return
    
    # 获取输入文件大小
    input_size = os.path.getsize(input_file)
    print(f"输入文件大小: {input_size / (1024*1024*1024):.2f} GB")
    
    # 计算需要拆分的文件数量
    num_parts = math.ceil(input_size / max_size)
    print(f"将拆分为 {num_parts} 个文件，每个文件最大 {max_size_gb} GB")
    
    # 读取原始tar.gz文件
    with open(input_file, 'rb') as f:
        for i in range(num_parts):
            # 计算当前部分的大小
            part_size = min(max_size, input_size - i * max_size)
            print(f"创建第 {i+1} 部分，大小: {part_size / (1024*1024*1024):.2f} GB")
            
            # 生成输出文件名
            output_file = f"{input_file}.part{i+1}.tar.gz"
            
            # 写入当前部分
            with open(output_file, 'wb') as out_f:
                out_f.write(f.read(int(part_size)))
            
            print(f"已创建: {output_file}")
    
    print("拆分完成！")
    print("\n注意：")
    print("1. 这些拆分文件可以直接解压，因为tar.gz格式本身支持流式解压")
    print("2. 解压时，每个拆分文件会解压出原始文件的一部分内容")
    print("3. 如果需要完整的原始文件，需要将所有拆分文件合并后再解压")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="拆分tar.gz文件为多个可独立解压的文件")
    parser.add_argument("input_file", help="输入tar.gz文件路径")
    parser.add_argument("--max-size", type=float, default=5, help="每个拆分文件的最大大小(GB)，默认5GB")
    
    args = parser.parse_args()
    split_tar_gz(args.input_file, args.max_size)
