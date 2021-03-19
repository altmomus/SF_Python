per_cent = {'TKB': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
money = float(input("введите сумму: "))
a = int(per_cent['TKB']*money/100), int(per_cent['SKB']*money/100), int(per_cent['VTB']*money/100), int(per_cent['SBER']*money/100)
i=max(a)
print("Накопленные проценты за год:", a)
print("Максимальная сумма, которую вы можете заработать:", i)
