import subprocess

def get_nvidia_gpu_info():
    try:
        # Run the nvidia-smi command
        result = subprocess.run(['nvidia-smi', '--query-gpu=name,driver_version', '--format=csv,noheader'], 
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr.strip()}")
            return None
        
        # Get the GPU name from the output
        nvidia_info = result.stdout.split(',')
        return nvidia_info[0].replace('NVIDIA','').strip(), nvidia_info[1].strip()
    except FileNotFoundError:
        print("nvidia-smi is not found. Ensure that NVIDIA drivers are installed correctly.")
        return None



gpu_info, driver_version = get_nvidia_gpu_info()
if gpu_info:
    print(f"NVIDIA GPU: {gpu_info} ({driver_version})")
