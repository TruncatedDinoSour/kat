# kat bot

> matrix bot for cats by cats -- @kat:ari.lt

public instance ran by me : <https://matrix.to/#/@kat:ari.lt>

## running

```sh
python3 -m pip install --user --upgrade --break-system-packages virtualenv
python3 -m virtualenv venv
source venv/bin/activate
pip install --upgrade -r requirements.txt
cp kat.example.env kat.env
# edit kat.env with details
source kat.env
python3 src/main.py
```
