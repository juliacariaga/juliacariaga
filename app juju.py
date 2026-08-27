app= flash (_name_)
app.config.from_pyfile ("config.app")
jwt= JWTManager (app)
init_db()
app.register_blueprint(user_bp, url_prefixe='/user' \')
 app.regiter_blueprint(fprmulario_bp,urlprefix) '/f'                     
if_name=='and__main__':
app.run(debug=true)