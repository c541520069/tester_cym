import os
import tarfile
import subprocess
import tempfile

def create_test_tar_gz(output_file, size_mb=10):
    """
    创建一个测试用的tar.gz文件
    
    Args:
        output_file (str): 输出文件路径
        size_mb (int): 文件大小(MB)
    """
    # 创建临时目录
    with tempfile.TemporaryDirectory() as temp_dir:
        # 创建一个大文件
        test_file = os.path.join(temp_dir, 'test.txt')
        with open(test_file, 'wb') as f:
            # 写入指定大小的数据
            f.write(b'x' * (size_mb * 1024 * 1024))
        
        # 创建tar.gz文件
        with tarfile.open(output_file, 'w:gz') as tar:
            tar.add(test_file, arcname='test.txt')
    
    print(f"已创建测试文件: {output_file}")
    print(f"文件大小: {os.path.getsize(output_file) / (1024*1024):.2f} MB")

def test_split_script():
    """
    测试拆分脚本
    """
    # 测试文件路径
    test_file = 'test_10mb.tar.gz'
    
    # 创建测试文件
    create_test_tar_gz(test_file, size_mb=10)
    
    # 运行拆分脚本，设置max-size为2MB（用于测试）
    print("\n运行拆分脚本...")
    result = subprocess.run(
        ['python', 'split_tar_gz.py', test_file, '--max-size', '0.002'],
        capture_output=True,
        text=True
    )
    
    print("拆分脚本输出:")
    print(result.stdout)
    if result.stderr:
        print("错误:")
        print(result.stderr)
    
    # 检查生成的拆分文件
    print("\n生成的拆分文件:")
    for file in os.listdir('.'):
        if file.startswith('test_10mb.tar.gz.part'):
            size_mb = os.path.getsize(file) / (1024*1024)
            print(f"{file}: {size_mb:.2f} MB")
    
    # 清理测试文件
    os.remove(test_file)
    for file in os.listdir('.'):
        if file.startswith('test_10mb.tar.gz.part'):
            os.remove(file)
    
    print("\n测试完成，已清理测试文件")

if __name__ == "__main__":
    test_split_script()
