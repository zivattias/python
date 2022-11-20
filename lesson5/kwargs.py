def c(**kwargs):
    print(type(kwargs))
    print(kwargs['first'])
    print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")

def cc(person_id, name, *args, **kwargs):
    print(person_id, name, args, kwargs)

c(first='Python', mid='Full', last='Stack')
cc(345345, 'Valeria', 'hello world', work_address="tel aviv", age=40)