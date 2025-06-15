View(characters_stats)

#Checking number of rows and columns
nrow(characters_stats)
ncol(characters_stats)

#Tabulation of categorical columns
table(characters_stats$Intelligence)
table(characters_stats$Strength)
table(characters_stats$Speed)

#min-max speed
min(characters_stats$Speed)
max(characters_stats$Speed)

#Checking Missing Values
is.na(characters_stats$abilities)
sum(is.na(characters_stats$abilities))

#Renaming columns
colnames(characters_stats)[colnames(characters_stats)=="Name"]<-"Characters"
View(characters_stats)

colnames(characters_stats)[colnames(characters_stats)=="Intelligence"]<-"Intellect"
View(characters_stats)

colnames(characters_stats)[colnames(characters_stats)=="Alignment"]<-"Type"
View(characters_stats)

#Loki
characters_stats%>%filter(Name=="Loki")->Loki

min(Loki$Speed)
max(Loki$Speed)

mean(Loki$Strength)
mean(Loki$Intelligence)

#Visualizing stats of  Loki
library(ggplot2)

ggplot(data=Loki.aes(x=Speed)+geom_histogram())




