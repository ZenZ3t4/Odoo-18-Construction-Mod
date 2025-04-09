# Odoo18 tk_construction rss

### Connecting to VPS
```
ssh root@212.227.232.51
MyPastedPassword
```
### Copy my script from local to Server directory

Use WinSCP to copy/paste the new script from local to server path root@ubuntu: /usr/cartella_appoggio
Download: https://winscp.net/eng/download.php
![alt text](https://miro.medium.com/v2/resize:fit:500/1*Of7JOwV0wZgDIjgaS4qKlQ.png)

### Copy my script from FTP folder to Odoo18 Docker Container:
```
docker cp /usr/cartella_appoggio/20250409v2_construction_project.py 2ae489527985:/usr/lib/python3/dist-packages/odoo/addons/tk_construction_management/models/
```

### Enter into Docker container image:
```
docker exec -it -u 0 2ae489527985 bash
```

### Rename the OLD script (construction_project.py):
```
mv /usr/lib/python3/dist-packages/odoo/addons/tk_construction_management/models/construction_project.py /usr/lib/python3/dist-packages/odoo/addons/tk_construction_management/models/old_20250409v1_construction_project.py
```

### Rename the NEW script uploaded to our FTP directory in construction_project.py:
```
mv /usr/lib/python3/dist-packages/odoo/addons/tk_construction_management/models/20250409v2_construction_project.py /usr/lib/python3/dist-packages/odoo/addons/tk_construction_management/models/construction_project.py
```

### Exit Docker and restart the container:
```
exit

docker restart 2ae489527985
```
