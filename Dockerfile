FROM python:slim-trixie

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Install dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the application on:
EXPOSE 8080

# Run the application
# CMD ["python", "rescue_interactive.py"]
CMD ["python", "oldies_songs.py"]