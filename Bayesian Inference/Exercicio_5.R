# SME0809 - Exercicio: Agricultura x Urbano
#Nome: Juan L. Montanaro
#N. USP: 11912787

# Dados:
z <- c(rep(0,5), rep(1,5))
x <- c(seq(2,10, 2), seq(4, 12, 2))
y <- c(25, 29, 45, 53, 73, 47, 73, 87, 109, 119)
N = length(x)

# Usando Z == 0:
data <- list('N'=N/2, 'x'=x[1:5], 'y'=y[1:5])

# funcao do modelo:
library(R2OpenBUGS)
modelo <- function(){
  
  # Definindo a distribuição dos dados
  for(i in 1:N){
    mu[i] <- beta0 + beta1*x[i]
    y[i] ~ dnorm(mu[i], tau)
  }
  
  # Modelagem da incerteza a priori
  # utilizando uma priori vaga
  beta0 ~ dnorm(0.0,1.0E-6)
  beta1 ~ dnorm(0.0,1.0E-6)
  tau ~ dgamma(0.001,0.001)
  sigma2 <- 1 / tau
}

# Criando o arquivo para armazenar:
mod <- file.path(tempdir(), "mod2.txt")

# Inserindo o modelo no arquivo
write.model(modelo, mod)

# Parametros iniciais:
params <- c('beta0', 'beta1','tau','sigma2')
inits <- list(
  list(beta0=1, beta1=0.5, tau=1),
  list(beta0=2, beta1=2, tau=10),
  list(beta0=-1, beta1=2, tau=0.5))

# Cadeias de Markov:
out <- bugs(data, inits, params, mod,
            codaPkg=TRUE, n.chains=3,
            n.iter=15000, n.thin=1,
            n.burnin=5000, debug=F)
saida.coda <- read.bugs(out)

# Graficos:
#library(mcmcplots)
#mcmcplot(saida.coda)

#Resumo das estatisticas:
res <- summary(saida.coda)
res$statistics
res$quantiles

# Com os quantis e o resumo das estatisticas, vemos que Beta0 tem chance
#de ser igual a zero estatisticamente.
