load_hostdiscovery <- function(file){
  df <- read.delim(file, header = F, sep = " ")
  colnames(df) <- c('time', 'ip')
  df$time <- as.double(df$time)
  df$time <- df$time - df$time[1]
  df$nbrjoined <- 0:(length(df$time)-1)
  return(df)
}

plot_discovery <- function(df, save_img='last.png'){
  img_path <- paste('~/Documents/MASTER1INFO/projet_MAB1-Firewall_for_IoT/Experimentations/outputs/', save_img)
  if(!is.null(save_img)){
    png(img_path, width=700) 
  }
  plot(x=df$time, y=df$nbrjoined, xlab="Temps écoulé depuis l'appel à la procédure de parsing (s)",
       ylab="Nombre d'hôtes découverts", pch=4, col="red", yaxt="n")
  axis(side = 2, at=0:8)
  grid()
  lines(x=df$time, y=df$nbrjoined, type='c')
  abline(h=8, col='green', lwd=1.5)
  text(x=mean(df$time[1:2]), y=8, pos=1, "Nombre réel d'hôtes", col="green")
  if(!is.null(save_img)){
    dev.off() 
  }
}

load_multiple <- function(files){
  res <- 0:8
  for(file in files){
    df <- load_hostdiscovery(file)
    res <- cbind(res, df$time)
  }
  mean_times <- as.data.frame(cbind(0:8, rowMeans(res[, -1])))
  colnames(mean_times) <- c('nbrjoined', 'time')
  return(mean_times)
}

plot_mean_times <- function(files, save_img='lastmean.png'){
  mean_times <- load_multiple(files)
  print(mean_times)
  plot_discovery(mean_times, save_img = NULL)
  plot_discovery(mean_times, save_img = save_img)
}

targets = c(
  '~/Documents/MASTER1INFO/projet_MAB1-Firewall_for_IoT/Experimentations/discovery_logs/explo1.log',
  '~/Documents/MASTER1INFO/projet_MAB1-Firewall_for_IoT/Experimentations/discovery_logs/explo2.log',
  '~/Documents/MASTER1INFO/projet_MAB1-Firewall_for_IoT/Experimentations/discovery_logs/explo3.log',
  '~/Documents/MASTER1INFO/projet_MAB1-Firewall_for_IoT/Experimentations/discovery_logs/explo4.log',
  '~/Documents/MASTER1INFO/projet_MAB1-Firewall_for_IoT/Experimentations/discovery_logs/explo5.log'
  )

plot_mean_times(targets)