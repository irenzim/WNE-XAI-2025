# wersja CRAN
install.packages("DALEX")
# wersja gtihub
source("https://install-github.me/ModelOriented/DALEX")
# instalacja pakiet?w potrzebnych do u?ywania DALEX
DALEX::install_dependencies()
# pakiety z rodziny DALEX
install.packages('auditor')

install.packages("ingredients")
install.packages("iBreakDown")

#API do pobierania danych z repozytorium Open ML
install.packages("OpenML")

install.packages("farff")
install.packages("readr")

install.packages("DescTools")

install.packages("caret")
install.packages("randomForest")
install.packages("xgb")
install.packages("xgboost")


install.packages("caTools")
install.packages("pROC")
install.packages("OptimalCutpoints")

install.packages("lime")
install.packages("vip")

install.packages("rattle")



install.packages("rlang")
install.packages("devtools")
library(devtools)
devtools::install_github("ModelOriented/rSAFE")

