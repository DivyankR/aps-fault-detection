
### Step 1 - Install the requirements

```bash
pip install -r requirements.txt
```

### Step 2 - Run main.py file

```bash
python main.py
```

### Git version
```bash
git --version
```

### To download dataset
```bash
wget (paste the link of the dataset)
```

### You can clone existing GitHub repository 
```bash
git clone <github_url>
```

### Add your changes made in file to git staging area
```bash 
git add <file_name>
```
Note : You can give file_name to add specific file or use "." to add everything to staging area

### To push changes
```bash 
git push origin main
``` 
Note: origin--> contains url to your github repo
main--> is your branch name

### To push changes forcefully
```bash 
git push origin main -f
```

### To pull changes from GitHub repo
```bash
git pull origin main
```
Note: origin--> contains url to your github repo
main--> is your branch name

.env file has
```
MONGO_DB_URL="mongodb://localhost:27017"
AWS_ACCESS_KEY_ID="aagswdiquyawvdiu"
AWS_SECRET_ACCESS_KEY="sadoiuabnswodihabosdbn"
```

```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker ubuntu
newgrp docker
```
