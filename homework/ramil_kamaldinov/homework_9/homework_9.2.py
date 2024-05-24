temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25,
                27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda x: x > 28, temperatures))
h_temp = max(hot_days)
m_temp = min(hot_days)
av_temp = sum(hot_days) / len(hot_days)


print(hot_days)
print(h_temp, m_temp, av_temp)
