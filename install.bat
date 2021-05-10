python -m venv venv
venv/Scripts/activate.bat
pip -m install -r requirements.txt

touch run.bat
echo "python client/client.py" > run.bat
