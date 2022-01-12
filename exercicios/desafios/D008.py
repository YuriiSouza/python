m = float(input("Valor em Metros: "))

km = m/1000;
hm = m/100;
dam = m/10;
dm = m*10;
cm = m*100;
mm = m*1000;

print("Em km: {:.1f}\nEm hm: {:.1f}\nEm dam: {:.1f}\nEm dm: {:.0f}\nEm cm: {:.0f}\nEm mm: {:.0f}".format(km, hm, dam, dm, cm, mm))
