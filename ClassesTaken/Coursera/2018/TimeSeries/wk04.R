YwSim <- function(phis, sigma=1.0, nIter=10000, seed=FALSE) {
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

ExamineArProcess <- function(data) {
    centered.data <- data - mean(data)
    par(mfrow=c(3, 1))
    plot(data, main='Raw data', col='blue', lwd=3)
    acf(centered.data, main='ACF (centered)', col='red', lwd=3)
    pacf(centered.data, main='PACF (centered)', col='green', lwd=3)
}

ModelArProcess <- function(data, p) {
    centered.data <- data - mean(data)
    model = NULL
    r <- acf(centered.data, plot=F)$acf[2:(2 + p - 1)]
    R <- matrix(1, p, p)
    for (i in 1:(p - 1)) {
        for (j in (1:(p - i))) {
            R[j, j + i] <- r[i]
            R[j + i, j] <- r[i]
        }
    }
    b <- matrix(r ,nrow=p, ncol=1)

    model$phi.hat <- solve(R, b)
    model$c0 <- acf(centered.data, type='covariance', plot=F)$acf[1]
    model$var.hat <- model$c0 * (1 - sum(model$phi.hat * r))
    return(model)
}

