import pendulum

dt = pendulum.now()

a = dt.start_of('week')
b = dt.end_of('week')

print(a.to_datetime_string())
print(b.to_datetime_string())

pendulum.week_starts_at(pendulum.FRIDAY)
pendulum.week_ends_at(pendulum.THURSDAY)

a = dt.start_of('week')
b = dt.end_of('week')

print('-----------------')

print(a.to_datetime_string())
print(b.to_datetime_string())
