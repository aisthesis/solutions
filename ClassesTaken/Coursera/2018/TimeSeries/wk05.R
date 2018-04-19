GetArimaData <- function(model, n=2000, seed=FALSE) {
    if (seed) {
        set.seed(seed)
    }
    return(arima.sim(model, n))
}

ExamineSeries <- function(data, xlim=NULL) {
    centered.data <- data - mean(data)
    par(mfrow=c(3, 1))
    if (length(xlim)) {
        plot.ts(data, main='Raw data', col='blue', lwd=3, xlim=xlim)
    }
    else {
        plot.ts(data, main='Raw data', col='blue', lwd=3)
    }
    acf(centered.data, main='ACF (centered)', col='red', lwd=3)
    pacf(centered.data, main='PACF (centered)', col='green', lwd=3)
}

ShowAic <- function(data, ar.max.lag=3, ma.max.lag=2) {
    for (ar.lag in 0:ar.max.lag) {
        for (ma.lag in 0:ma.max.lag) {
            if (ar.lag == 0 && ma.lag == 0) {
                next
            }
            print(paste('ar(', ar.lag, '), ma(', ma.lag, '): ', AIC(arima(data, order=c(ar.lag, 0, ma.lag))), sep=''))
        }
    }
}

