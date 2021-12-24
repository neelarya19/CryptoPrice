web: gunicorn CryptoPice.wsgi --log-file -
celery: celery -A CryptoPrice.celery worker --pool=solo -l info
celerybeat: celery -A CryptoPrice beat -l INFO
celeryworker: celery -A CryptoPrice.celery worker --pool=solo -l info & celery -A CryptoPrice beat -l INFO & wait -n