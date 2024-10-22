FROM python:3.9
#pecifies the base image as Python 3.9

WORKDIR /code
# Sets the working directory inside the container to /code.

COPY requirement.txt ./
#This line copies the requirements.txt file from your local directory into the container's working directory.

RUN pip install --no-cache-dir -r requirement.txt
#This line installs the Python dependencies listed in requirements.txt using pip. The --no-cache-dir flag prevents caching of the package index.

COPY . .
#This line copies the entire local directory into the container's working directory. This is basically everything in your FastAPI project.

# Expose port yang digunakan oleh Uvicorn
EXPOSE 8000

# Perintah untuk menjalankan aplikasi
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]