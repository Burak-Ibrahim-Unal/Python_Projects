sa=int(input("Please write hour:"));
sb=int(input("Please write minute:"));
sc=int(input("Please write second:"));
ea=int(input("Please write hour:"));
eb=int(input("Please write minute:"));
ec=int(input("Please write second:"));

first=3600*sa+60*sb+sc;
end=3600*ea+60*eb+ec

time=end-first;
h=time//3600;
m=time%3600//60;
s=time%3600%60;
print("Time difference is:",h,":",m,":",s);