# Issues I ran into

After merging the update from @faafeefoo, sync'd my clone and fork, began to edit/test in Pycharm.  
First issue - "ModuleNotFoundError: No module named 'encodings'"  After updating Python to 3.7 the path changed and required me to update Pycharm with new path of interpreter.
Second issue - "ModuleNotFoundError: No module named 'requests'"  After searching that error found need to run 
```
[ADMIN]  C:\publicGitHub> pip install requests
Collecting requests
  Downloading https://files.pythonhosted.org/packages/7d/e3/20f3d364d6c8e5d2353c72a67778eb189176f08e873c9900e10c0287b84b/requests-2.21.0-py2.py3-none-any.whl (57kB)
    100% | 61kB 612kB/s
Collecting idna<2.9,>=2.5 (from requests)
  Downloading https://files.pythonhosted.org/packages/14/2c/cd551d81dbe15200be1cf41cd03869a46fe7226e7450af7a6545bfc474c9/idna-2.8-py2.py3-none-any.whl (58kB)
    100% | 61kB 613kB/s
Collecting certifi>=2017.4.17 (from requests)
  Downloading https://files.pythonhosted.org/packages/9f/e0/accfc1b56b57e9750eba272e24c4dddeac86852c2bebd1236674d7887e8a/certifi-2018.11.29-py2.py3-none-any.whl (154kB)
    100% | 163kB 2.2MB/s
Collecting chardet<3.1.0,>=3.0.2 (from requests)
  Downloading https://files.pythonhosted.org/packages/bc/a9/01ffebfb562e4274b6487b4bb1ddec7ca55ec7510b22e4c51f14098443b8/chardet-3.0.4-py2.py3-none-any.whl (133kB)
    100% | 143kB 2.7MB/s
Collecting urllib3<1.25,>=1.21.1 (from requests)
  Downloading https://files.pythonhosted.org/packages/62/00/ee1d7de624db8ba7090d1226aebefab96a2c71cd5cfa7629d6ad3f61b79e/urllib3-1.24.1-py2.py3-none-any.whl (118kB)
    100% || 122kB 3.3MB/s
Installing collected packages: idna, certifi, chardet, urllib3, requests
Successfully installed certifi-2018.11.29 chardet-3.0.4 idna-2.8 requests-2.21.0 urllib3-1.24.1
```

Once those two items addressed, the sample is working.