# python -m nltk.downloader stopwords
import subprocess
cmd = ["python", "-m" ,"nltk.downloader", "stopwords"]
subprocess.run(cmd)
print("working on nltk")