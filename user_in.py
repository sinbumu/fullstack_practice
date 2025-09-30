from pydantic import BaseModel, ValidationError
from typing import Optional

class UserIn(BaseModel):
    username: str
    age: int

class UserIn2(BaseModel):
    username: str
    age: Optional[int] = None

data = UserIn(username="dustring", age="31")
print("username:",data.username)
print("age:",data.age,type(data.age))

print("as dict:",data.model_dump())

u1 = UserIn2(username="dagam")
print(f'u1.model_dump(): {u1.model_dump()}')

u2 = UserIn2(username="dajin", age="2")
print(f'u2.model_dump(): {u2.model_dump()}')

try:
    u_err = UserIn2(username="jin", age="test")
    print("u_err", u_err)
    print("u_err.momdel_dump():", u_err.momdel_dump())
except ValidationError as e:
    print("ValidationError 발생!")
    print(e)

    print("e.errors()", e.errors())
