# use the official Python image as the base image
FROM python:3.8-slim

# set the working directory
WORKDIR /app

# copy the requirements file into the container
COPY requirements.txt .

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the entire app into the container
COPY . .

# expose port 5001
EXPOSE 5001

# command to run the application
CMD ["python", "app.py"]
