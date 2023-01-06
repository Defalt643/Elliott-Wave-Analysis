from __future__ import annotations
from models.WavePattern import WavePattern
from models.WaveRules import Impulse, LeadingDiagonal, Correction, TDWave
from models.WaveAnalyzer import WaveAnalyzer
from models.WaveOptions import WaveOptionsGenerator5
from models.helpers import plot_pattern
import pandas as pd
import numpy as np
import time

from klines import getCSV

# df = pd.read_csv('data/btc-usd_1d.csv')
# df = pd.read_csv('data/output.csv')

symbol = 'BTCUSDT'

getCSV(sysmbol=symbol)

df = pd.read_csv('testCSV.csv')

print(type(df))

idx_start = np.argmin(np.array(list(df['Low'])))

wa = WaveAnalyzer(df=df, verbose=False)
wave_options_impulse = WaveOptionsGenerator5(up_to=15)  # generates WaveOptions up to [15, 15, 15, 15, 15]

impulse = Impulse('impulse')
leading_diagonal = LeadingDiagonal('leading diagonal')
correction = Correction('correction')
td_wave = TDWave('td wave')
rules_to_check = [impulse, leading_diagonal,correction,td_wave]

print(f'Start at idx: {idx_start}')
print(f"will run up to {wave_options_impulse.number / 1e6}M combinations.")

# set up a set to store already found wave counts
# it can be the case, that 2 WaveOptions lead to the same WavePattern.
# This can be seen in a chart, where for example we try to skip more maxima as there are. In such a case
# e.g. [1,2,3,4,5] and [1,2,3,4,10] will lead to the same WavePattern (has same sub-wave structure, same begin / end,
# same high / low etc.
# If we find the same WavePattern, we skip and do not plot it

wavepatterns_up = set()

# loop over all combinations of wave options [i,j,k,l,m] for impulsive waves sorted from small, e.g.  [0,1,...] to
# large e.g. [3,2, ...]
for new_option_impulse in wave_options_impulse.options_sorted:

    waves_up = wa.find_impulsive_wave(idx_start=idx_start, wave_config=new_option_impulse.values)

    if waves_up:
        wavepattern_up = WavePattern(waves_up, verbose=True)

        for rule in rules_to_check:

            if wavepattern_up.check_rule(rule):
                if wavepattern_up in wavepatterns_up:
                    continue
                else:
                    title = str(new_option_impulse)+"Symbol: "+str(symbol)
                    wavepatterns_up.add(wavepattern_up)
                    print(f'{rule.name} found: {new_option_impulse.values}')
                    plot_pattern(df=df, wave_pattern=wavepattern_up, title=title)
