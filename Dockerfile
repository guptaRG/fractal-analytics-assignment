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
RUN pip install --no-cache-dir -r requirements/prod

CMD python manage.py collectstatic --noinput \
    && python manage.py migrate \
    && gunicorn -b 0.0.0.0:$PORT --workers $NUM_WORKERS \
        --name fullstack_assignment_platform \
        --access-logfile '-' --error-logfile '-' --log-level $GUNICORN_LOG_LEVEL \
        --access-logformat '%(h)s %(l)s %(u)s %(t)s %(L)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"' \
        core.wsgi
