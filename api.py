from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page

from ninja import NinjaAPI
from ninja.decorators import decorate_view
from ninja.throttling import AuthRateThrottle
import redis

api = NinjaAPI()


@api.get("/hello")
def hello_world(request):
    return {"message": "Hello, Ninja!"}


@api.get("/redis-test")
def redis_test(request):
    # docker-compose で起動した Redis (localhost:6379) に接続
    # ※ ホストOSから見ると "localhost" or 127.0.0.1 ポート6379
    #   Docker Desktop や環境によってはアドレスが異なる場合もあるので注意
    r = redis.Redis(host="localhost", port=6379, db=0)

    # テスト用キーに値をセット
    r.set("test_key", "Hello Redis!")
    # 値を取得
    value = r.get("test_key").decode("utf-8")
    return {"redis_value": value}


@api.get("/cache-test", throttle=AuthRateThrottle("1/sec"))
@decorate_view(cache_page(30))
def cache_test(request):
    users = list(
        User.objects.values("id", "username", "email", "first_name", "last_name")
    )
    return users
