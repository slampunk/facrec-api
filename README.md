Source: https://pyimagesearch.com/2018/06/25/raspberry-pi-face-recognition/

# Setting up

### Requirements
```
python 3
pip
```
Ensure that python is available in your `PATH` by checking the output of the following command
```
$ python -V
Python 3.10.8
```
If the above fails, it may be that you specify the major version of python as follows
```
$ python3 -V
Python 3.10.8
```

### Global installation flow
Dependencies will be installed globally. This is fine if you don't plan on doing any python work in the foreseeable future.
Install the dependencies as follows
```
pip install -r requirements.txt
```

### Virtual environment flow
This flow boots up a local python environment, ensuring that no dependency conflicts occur.

```
$ python -m venv facial-recognition
$ source facial-recognition/bin/activate
$ pip install -r requirements.txt
```
