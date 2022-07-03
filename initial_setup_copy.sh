echo [$(date)]: "START"
echo [$(date)]: "creating environment"
conda create -n  NER python=3.9 -y
echo [$(date)]: "activate environment"
conda.bat  activate NER
echo [$(date)]: "install requirements"
pip install -r requirements.txt
echo [$(date)]: "END"