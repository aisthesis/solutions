ywSim <- function(phis, sigma=1.0, nIter=10000, seed=FALSE) {
    if (seed) {
        set.seed(seed)
    }
    ar.process <- arima.sim(nIter, model=list(ar=phis), sd=sigma)
    nPhis <- length(phis)
    r <- acf(ar.process, plot=F)$acf[2:(2 + nPhis - 1)]
    R <- matrix(1, nPhis, nPhis)
    for (i in 1:(nPhis - 1)) {
        for (j in (1:(nPhis - i))) {
            R[j, j + i] <- r[i]
            R[j + i, j] <- r[i]
        }
    }
    b <- matrix(r ,nrow=nPhis, ncol=1)
    phi.hat <- solve(R, b)
    print('phi hat:')
    print(phi.hat)

    # estimate variance
    c0 <- acf(ar.process, type='covariance', plot=F)$acf[1]
    var.hat <- c0 * (1 - sum(phi.hat * r))
    print(paste('Variance:', var.hat))

    # plot time series, acf, pacf
    par(mfrow=c(3,1))
    title <- paste('Simulated AR(', nPhis, ')', sep='')
    plot(ar.process, main=title)
    acf(ar.process, main='ACF')
    pacf(ar.process, main='PACF')
}

