from src.Domain.user import UserDomain
from src.Infrastructure.Model.user import User
from src.config.data_base import db
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    @staticmethod
    def create_user(name, email, cnpj, celular, password):
        senha_hash = generate_password_hash(password)

        user = User(
            name=name,
            cnpj=cnpj,
            email=email,
            celular=celular,
            password=senha_hash,
            status=True,
        )
        db.session.add(user)
        db.session.commit()
        

        return UserDomain(user.id, user.name, user.email)

    @staticmethod
    def login(email, password):
        user = User.query.filter_by(email=email).first()

        if not user:
            return None, "Usuário não encontrado"

        if not check_password_hash(user.password, password):
            return None, "Senha inválida"

        if user.status == False:
            return None, "Conta não ativada"

        token = create_access_token(identity=str(user.id))
        return token, None
    
    @staticmethod
    def get_user(user_id):
        return User.query.get(user_id)

    @staticmethod
    def update_user(user_id, data):
        user = User.query.get(user_id)

        if not user:
            return False
        
        campos = ["name", "email", "cnpj", "celular", "password"]

        for campo in campos:
            if campo in data:
                setattr(user, campo, data[campo])
        
        if "password" in data:
            user.password = generate_password_hash(data["password"])
        
        db.session.commit()
       
        return UserDomain(user.id, user.name, user.email)
