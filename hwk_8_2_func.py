#Task_2
def author_info(firstname, middlename, lastname, birthdate, deathdate, bio):
    initials = f"{firstname[0]}.{middlename[0]}" if middlename else f"{firstname[0]}."
    lifespan = f"({birthdate}-{deathdate})" if deathdate else f"({birthdate}-)"
    info = f"{initials} {lastname} {lifespan} - {bio}"
    print(info)
author_info(firstname="Александр", middlename="Сергеевич", lastname="Пушкин", birthdate="26 мая 1799", deathdate="29 января 1837", bio="русский писатель, поэт, драматург")
author_info(firstname="Иван", middlename="", lastname="Соболь", birthdate="24 августа 1939", deathdate="", bio="израильский драматург, писатель, режиссер")
