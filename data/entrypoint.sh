APP=/app
DATA=/data

cd $APP
do
    python manage.py migrate --no-input
done