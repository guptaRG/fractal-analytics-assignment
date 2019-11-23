# This base image uses Debian operating system
FROM python:3.6.8

# This forces python to not buffer output / error
ENV PYTHONUNBUFFERED 1

# This is where we will copy all our code
# Workdir creates the directory if it doesn't exist
WORKDIR /fractal_analytics_platform

# ---------------------------------------------
# From here, the steps are application specific
# ---------------------------------------------

# Now copy the entire code and install all dependencies
# As a best practice, you should pin down version numbers in requirements.txt
COPY . /fractal_analytics_platform
RUN pip install --no-cache-dir -r requirements

CMD python manage.py collectstatic --noinput \
    && python manage.py migrate \
    && python manage.py runserver
