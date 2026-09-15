from .models import User


def create_user(*, username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    user.save()
    return user

def change_password(*, user, new_password):
    user.set_password(new_password)
    user.save(update_fields=["password"])
    return user
