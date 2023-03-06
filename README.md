<h1>3d Deep Learning Python</h1>

<h3>Summary</h3>
This project is to test and learn deep learning practices using pytorch3d and practice 3d analysis.

<h2>Installing with Pip</h2>

Install Microsoft C++ Build Tools

https://github.com/facebookresearch/pytorch3d/blob/main/INSTALL.md

Download the repository using the steps below:

git clone https://github.com/facebookresearch/pytorch3d.git
cd pytorch3d && pip install -e .

Install from local clone on Windows:

Depending on the version of PyTorch, changes to some PyTorch headers may be needed before compilation. These are often discussed in issues in this repository.

After any necessary patching, you can go to "x64 Native Tools Command Prompt for VS 2019" to compile and install

cd pytorch3d
python3 setup.py install

After installing, you can run unit tests

python3 -m unittest discover -v -s tests -t .

