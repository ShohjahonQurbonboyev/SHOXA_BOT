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



class adminwebstate(StatesGroup):
    name = State()
    url = State()


class adminusrstate(StatesGroup):
    change_user = State()


class deletestate(StatesGroup):
    change_delete = State()
    delete = State()