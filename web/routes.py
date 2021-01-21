def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('add', '/add')
    config.add_route('create', '/create')
    config.add_route('delete', '/delete')
    config.add_route('update', '/update')
    config.add_route('notes', '/notes')
    config.add_route('sign_in', '/sign_in')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
