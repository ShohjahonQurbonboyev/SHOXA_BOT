from aiogram.dispatcher.filters.state import State, StatesGroup




class phonestate(StatesGroup):
    phone = State()

class main(StatesGroup):
    main_menu = State()

class mystate(StatesGroup):
    my = State() 

class changestate(StatesGroup):
    change = State()
    bot = State()
    web = State()

class reklamastate(StatesGroup):
    sorov = State()


class myprojects(StatesGroup):
    change = State()
    

class adminstate(StatesGroup):
    password = State()
    admin_menu = State()
    change_prject = State()
    name = State()
    username = State()
    write_group = State()
    write = State()


class adminwebstate(StatesGroup):
    name = State()
    url = State()


class adminusrstate(StatesGroup):
    change_user = State()


class deletestate(StatesGroup):
    change_delete = State()
    delete = State()


class shikoyatstate(StatesGroup):
    shikoyat = State()



class freelancer(StatesGroup):
    menu = State()
    type = State()
    name = State()
    surname = State()
    age = State()
    technologies = State()
    country = State()
    price = State()
    maqsad = State()
    tasdiq = State()
    manage_admin = State()



class hodim(StatesGroup):
    idora = State()
    technology = State()
    country = State()
    manager_name = State()
    time = State()
    work_time = State()
    price = State()
    ex_data = State()
    tasdiq = State()


class send_msg(StatesGroup):
    number_msg = State()
    xabar = State()


class translaterbn(StatesGroup):
    translate = State()
    to_bn = State()
    to_text = State()