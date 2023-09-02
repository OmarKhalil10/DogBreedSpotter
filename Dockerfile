# Use Python37
FROM python:3.7

## Step 1:
# Create a working directory
WORKDIR /app

## Step 2:
# Copy source code to working directory
COPY app.py requirements.txt /app/
COPY templates /app/templates/
COPY static /app/static/
COPY uploads /app/uploads/
COPY ./imagenet-dictionary /app/imagenet-dictionary/
COPY ./dogs-names /app/dogs-names/

## Step 3:
# Install packages from requirements.txt
RUN pip install -r requirements.txt && \
    rm /app/requirements.txt

## Step 4:
# Expose port 5000
EXPOSE 5000
ENV PORT 5000

# Use gunicorn as the entrypoint
CMD exec gunicorn --bind :$PORT app:app --workers 1 --threads 1 --timeout 60