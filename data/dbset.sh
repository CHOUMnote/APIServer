docker run -p 5432:5432 --name psql -e POSTGRES_PASSWORD=1q2w3e4r -e TZ=Asia/Seoul -v C:/CODE/APIServer/data/db:/var/lib/postgresql/data -d postgres:12.13-alpine

#./data/db:/var/lib/postgresql/data