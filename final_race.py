import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl()
fig, ax = plt.subplots()

ff1.Cache.enable_cache('Cache')

race = ff1.get_session(2021, 'Abu Dhabi Grand Prix', 'R')
laps = race.load_laps()

ver = laps.pick_driver('VER')
ham = laps.pick_driver('HAM')


ax.plot(ver['LapNumber'], ver['LapTime'], color='blue')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')

ax.set_title("VER vs HAM")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")

plt.show()
